from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
import markdown2
import random
from . import util
import re

class NewEntryForm(forms.Form):
    entryTitle = forms.CharField(label="Entry Title:")
    entryContent= forms.CharField(widget=forms.Textarea,label="Entry Content:")

class EditEntry(forms.Form):
    entryTitle = forms.CharField(widget = forms.HiddenInput(), required = True)
    entryContent = forms.CharField(widget=forms.Textarea,label="Entry Content:")

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry=None):
    try:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(util.get_entry(entry)), 
            "title": entry   
        })
    except:
        return render(request, "encyclopedia/404.html", status=404)

def new(request):

    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['entryTitle']
            newEntry = form.cleaned_data['entryContent']
            entries = util.list_entries()
            if title in entries:
                return render(request, 'encyclopedia/new.html', {
                'form': form,
                'error': '<div class="alert alert-warning">This entry already exists!</div>'
            })
            else:
                util.save_entry(title, newEntry)
                return entry(request, title)

    return render(request, "encyclopedia/new.html", {
        'form': NewEntryForm()
    })

def randomPage(request):
    
    randEntries = util.list_entries()
    randEntry = random.choice(randEntries)
    return redirect('entry', entry=randEntry)

def edit(request):

    page = request.GET.get('page')

    if request.method == "POST":
        form = EditEntry(request.POST)
        if form.is_valid():
            entryTitle = form.cleaned_data['entryTitle']
            entryContent = form.cleaned_data['entryContent']
            util.save_entry(entryTitle, entryContent)
            return redirect('entry', entry=entryTitle)

    return render(request, "encyclopedia/edit.html", {
        'title': page,
        'form': EditEntry(initial={'entryTitle':page,'entryContent':util.get_entry(page)})
    })

def search(request):

    search = request.GET.get('q')
    entries = util.list_entries()
    
    for i in entries:
        if search.lower() == i.lower():
            return render(request, "encyclopedia/entry.html", { 
                "entry": markdown2.markdown(util.get_entry(search)), 
                "title": search
            })

    results = [i for i in entries if re.search(search, i, flags=re.IGNORECASE)]

    return render(request, "encyclopedia/search.html", { 
        'entries': results,
        'search': search
    })

def handler404(request, exception):
    return render(request, "encyclopedia/404.html", status=404)

def handler500(request):
    return render(request, "encyclopedia/404.html", status=500)