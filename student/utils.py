import os 
from twilio.rest import Client

account_sid='AC07c66706b00891446808cdc2c928e602'
auth_token='5cda46301074d5652886ba353ef57c29'
client=Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    message=client.messages.create(
        body=f'Hi! Your user and verification code is {user_code}',
        from_='+15712537139',
        to=f'{phone_number}')
    print(message.sid)

account_sid2='AC0b3ef57ce07e9f0bd56a05fc80640e0f'
auth_token2='81a090efd10fcba0cc58dc5cccfe12c5'
client2=Client(account_sid2,auth_token2)

def whatsapp(phoneNumber,message):
    message=client2.messages.create(to='whatsapp:'+str(phoneNumber),
                                    from_='whatsapp:+14155238886',
                                    body=message)
                                                    
