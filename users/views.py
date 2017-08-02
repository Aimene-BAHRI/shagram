# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import ContactByMailForm

# Create your views here.

#Contact-Us form handling
def contact_us(request):
    sent = False

    if request.method == 'POST':
        form = ContactByMailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message_to_send = "Sender: <strong>{} ({})</strong>.<br>Content:<br><br> {}".format(cd['name'],cd['email'], cd['message'])
            email_subject = "[Fundation website] {}".format(cd['subject'])
            msg = EmailMessage(email_subject, message_to_send,cd['email'], ["{}".format(settings.EMAIL_HOST_USER),],reply_to=[cd['email']])
            msg.content_subtype = "html"
            msg.send()
            sent = True
    else:
        form = ContactByMailForm()

    return render(request, 'contact/contact-us.html', {'form': form,'sent': sent})
