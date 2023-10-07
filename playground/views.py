from django.core.mail import send_mail, mail_admins, EmailMessage ,BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
# Create your views here.

def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Karl'}
        )
        message.send(['karl@from.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', { 'name' : 'Karl'})
