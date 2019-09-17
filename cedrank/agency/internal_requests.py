from cedrank.settings import client, from_number


def send_sms_to(worker_phone, message_body):
    try:
        client.messages.create(
            body=message_body,
            from_=from_number,
            to=worker_phone
        )
    except:
        print('Message not send.')
