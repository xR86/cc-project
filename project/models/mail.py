# comment everything to test locally
from google.appengine.api import mail
from google.cloud import translate

def send_register_mail(email_address):
    mail.send_mail(sender='ioana.bogdan25@gmail.com',
                   to=email_address,
                   subject="Your account has been approved",
                   body="""Congrats, your account has been created.""")


def translate_text_with_model(target, text, model=translate.NMT):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, model=model)
    return result['translatedText']


def send_booking_confirmed_mail(email_address, lang):
    english_body = "Your reservation has been reviewed!"
    english_title = "Reservation reviewed!"
    mail.send_mail(sender='ioana.bogdan25@gmail.com',
                   to=email_address,
                   subject=translate_text_with_model(lang, english_title),
                   body=translate_text_with_model(lang, english_body))

