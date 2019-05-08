from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Msg

def index(request):
        msg = Msg.objects.all()
        return render(request, "index.html",{"msg":msg})

def create(request):
    if request.method == "POST":
        message = Msg()
        message.name = request.POST.get("name")
        message.save()
    return HttpResponseRedirect("/")

