import requests
import logging
import os
import random
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler


def readConfig():
    '''
    reading environment variables
    '''
    if os.path.exists('.env') == True:
        load_dotenv()
        return logging.info("Environment file has been read")
    else:
        return logging.info(".env file not present, falling back to normal Environment")
    
def sendViaTelegram(appieNotification):
    '''
    setting up api connection for sending Telegram messages
    '''
    bot_token = os.environ['telegram_bot_token']
    bot_chatID = os.environ['telegram_chat_id']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + appieNotification
    response = requests.get(send_text)
    logging.info(response.json)
    return

def generate_random_turns():
    people = ["Christian", "Emilia", "Raul"]
    chores = ["Common Area", "Kitchen", "Bathroom"]
    random.shuffle(chores)

    return people, chores


def weekly_turns():
    people, chores = generate_random_turns()
    message = "This week's chores: ✨\n"
    for (person, chore) in zip(people, chores):
        message += f"📌 {person} - {chore}\n"
    message += "\n Don't forget to react to this message when you finish your task! 🧹"
    sendViaTelegram(message)

    

def main():
    try:
        logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

        readConfig()
        
        scheduler = BlockingScheduler()
        scheduler.configure(timezone='Europe/Amsterdam')
        scheduler.add_job(weekly_turns, 'cron', day_of_week='mon', hour=9, minute=00)

        scheduler.start()
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main()

