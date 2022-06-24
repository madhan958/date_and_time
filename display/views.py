from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    date = str(datetime.now().date())
    time = str(datetime.now().time())
    html = f'''
    <html>
    <body> 
        <h1> Date and Time is as below </h1>
        <h3> Date : {date}</h3>
        <h3> time : {time}</h3>
    </body>
    </html>
    '''
    return HttpResponse(html)