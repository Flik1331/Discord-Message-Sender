import requests
import time

def amount_messages():
    while True:
        txt = input("How many do you want to send? ")

        if txt.isnumeric():
            print("Is a number:", txt)
            check_webhook(txt)
            return int(txt)
        else:
            print("Not a number, try again.")

def check_webhook(txt):
        webhook = input("Webhook: ")

        if webhook.startswith("https://discord.com/api/webhooks/"):
            print("Correct ✔")
            message_text(webhook, txt)
            return int(txt)
        else:
            print("This is not a webhook❌", webhook)

def message_text(webhook, txt):
    message = input("Message: ")
    message_delay(message, webhook, txt)

def message_delay(message, webhook, txt):
        
        delay = input("Delay:")
        moro(message, webhook, delay, txt)

def moro(message, webhook, delay, txt):
    x = 0
    while x < int(txt): 
        send_message(message, webhook)
        x = x + 1
        time.sleep(int(delay))

def send_message(message, webhook):
        print(webhook)
        data = {'content': message}
        requests.post(webhook, json=data)

amount_messages()
