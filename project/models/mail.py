from google.appengine.api import mail


def send_register_mail(email_address):
    mail.send_mail(sender='ioana.bogdan25@gmail.com',
                   to=email_address,
                   subject="Your account has been approved",
                   body="""Congrats, your account has been created.""")


def send_booking_confirmed_mail(email_address):
    mail.send_mail(sender='ioana.bogdan25@gmail.com',
                   to=email_address,
                   subject="Reservation reviewed!",
                   body="""Your reservation has been reviewed!""")
