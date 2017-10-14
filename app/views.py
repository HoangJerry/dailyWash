from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.conf import settings

# from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

