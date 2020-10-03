from django.shortcuts import render

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random



from encyclopedia import util

def index(request):
    #list of entries
    entries = util.list_entries()
    if request.method == "POST":
    #grabing input value that user submitted
        result = request.POST['search']
        search = []
        if result in entries:
            return redirect(f"http://127.0.0.1:8000/{result}")
        else:
            for entry in entries:
                if result in entry:
                    search.append(result)

            return render(request, "encyclopedia/search.html",{
                    "searches": search
                })
