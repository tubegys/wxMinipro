from django.shortcuts import render
from message.models import UserMessage
import random
from django.http import HttpResponse


# Create your views here.


def getform(request):
    # all_messages = UserMessage.objects.all()
    user = UserMessage()
    # user.object_id = "id_{}".format(random.randint(0, 10))
    # user.name = "name_{}".format(random.randint(0, 10))
    # user.email = "{}@{}.com".format(random.randint(0, 10),random.randint(0, 10))
    # user.address = "address_{}".format(random.randint(0, 10))
    # user.message = "message_{}".format(random.randint(0, 10))_id = "id_{}".format(random.randint(0, 10))
    if request.method == "POST":
        user.name = request.POST.get('name', "")
        user.email = request.POST.get('email', "")
        user.address = request.POST.get('email', "")
        user.message = request.POST.get('email', "")
        user.save()

    # return render(request, 'message.html')
    return HttpResponse("dddd")
