from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

DATABASE=dict()
def home(request):
    return render(request,"index.html")
def upload(request):
    global  DATABASE
    if request.method == "GET":
        return render(request,"upload.html")
    if len(DATABASE) == 0 and request.method == "POST":
        # name = request.POST["csvfile"]
        file = request.FILES['csvfile'].read().decode('utf-8').splitlines()
        for i in file:
            string  = i.split(";")
            DATABASE[string[0]] = string[1:]
        return HttpResponse("uploade to the memory")
    else:
        return HttpResponse("the file is already uploades to the memory")








# main functionalty starts here



@api_view(['POST'])
def getBinInformation(request):
    global DATABASE
    bin = request.data["bin"]
    print(bin)
    if DATABASE.get(bin) != None:

        context = {
            "status_code":200,
            "msg":"Data Found",
            "data":DATABASE[bin],
        }
        return Response(context)
    context = {
        "status_code":200,
        "msg":"Data Not Found",
        "data":[]
    }
    return Response(context)
