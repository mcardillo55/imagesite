from django.shortcuts import render
from django.http import HttpResponse
import base64
import time


# Create your views here.

def getHash():
	return base64.b64encode(str(time.time()))[:-2]

def submit(request):
	return HttpResponse(getHash())