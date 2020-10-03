from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random


from . import util

class SearchForm(forms.Form):
    Title = forms.CharField(label="Title")
    Contents = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}))

#list funtions here

#def layout():
    #return render(request, "encyclopedia/layout.html", {
        #"form": SearchForm()})

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries":util.list_entries()
    })

def create(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            Title = form.cleaned_data["Title"]
            Contents = form.cleaned_data["Contents"]
            return util.save_entry(Title, Contents)
        else:
            return render(request, "encyclopedia/create.html", {
                "form": SearchForm()
            })

    return render(request, "encyclopedia/create.html", {
        "form": SearchForm()
    })

def title(request, title):
    if request.method == "POST":
        #grabing input value that user submitted
        search = request.POST['search']
        return redirect(request, f"http://127.0.0.1:8000/wiki/{search}")
    else:
        return render(request, "encyclopedia/title.html", {
            "title":title,
            "get":util.get_entry(title)
        })

def edit(request, title):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            Title = form.cleaned_data["Title"]
            Contents = form.cleaned_data["Contents"]
            return util.replace_entry(Title,Contents)
        else:
            return render(request, "encyclopedia/edit.html", {
                "form": SearchForm()
            })
    return render(request, "encyclopedia/edit.html", {
        "title":title,
        "form": SearchForm(initial={'Title':title, "Contents":util.get_entry(title)})

    })

def random_page(request):
    entries = util.list_entries()
    choice = random.choice(entries)
    return redirect(f"http://127.0.0.1:8000/wiki/{choice}")

def search(request):
    #list of entries
    entries = util.list_entries()
    if request.method == "POST":
    #grabing input value that user submitted
        result = request.POST['search']
        search = []
        if result in entries:
            return redirect(f"http://127.0.0.1:8000/wiki/{result}")
        else:
            for entry in entries:
                if result in entry:
                    search.append(result)

            return render(request, "encyclopedia/search.html",{
                    "searches": search
                })
