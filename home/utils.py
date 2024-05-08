from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
  subject = "This is Mail from Django"
  message = "Hey hope you are doing well. this is just a test message from django server"
  from_email = settings.EMAIL_HOST_USER
  recipient_list = ["shaneef2905@gmail.com"]
  send_mail(subject, message, from_email, recipient_list)
