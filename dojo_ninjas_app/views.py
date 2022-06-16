from ast import Delete
from multiprocessing import context
from os import stat
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    dojos = Dojo.objects.all()
    context ={
        'dojos':dojos
    }
    return render(request, "index.html", context)

def new_dojo(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        name_val = request.POST["name"]
        city_val = request.POST["city"]
        state_val = request.POST["state"]
        new_dojo = Dojo.objects.create(name = name_val, city = city_val, state = state_val)
        return redirect("/")

def add_ninja(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        fname_val = request.POST["fname"]
        lname_val = request.POST["lname"]
        dojo_val = Dojo.objects.get(id=request.POST["dojo"])
        new_dojo = Ninja.objects.create(dojo_id = dojo_val, first_name = fname_val, last_name = lname_val)
        return redirect("/")

def del_dojo(request,id):
    _del = Dojo.objects.get(id= id)
    _del.delete()
    return redirect("/")
