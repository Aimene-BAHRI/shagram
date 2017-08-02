# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactByMailForm

# Create your views here.

#Contact-Us form handling
def contact_us(request):
    sent = False

    if request.method == 'POST':
        form = ContactByMailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'],cd['email'], ["{}".format(settings.EMAIL_HOST_USER),])
            sent = True
    else:
        form = ContactByMailForm()

    return render(request, 'contact/contact-us.html', {'form': form,'sent': sent})
