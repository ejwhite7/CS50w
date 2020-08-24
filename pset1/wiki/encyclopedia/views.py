from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
import markdown2
from . import util


class NewEntryForm(forms.Form):
    entryTitle = forms.CharField(label="Entry Title:")
    entryContent= forms.CharField(widget=forms.Textarea,label="Entry Content:")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(util.get_entry(entry)), 
        "title": entry   
    })

def new(request):

    if request.method == "POST":

        form = NewEntryForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data['entryTitle']
            newEntry = form.cleaned_data['entryContent']

            entries = util.list_entries()

            if title in entries:
                
                return render(request, 'encyclopedia/new.html', {
                'form': form
            })

            else:

                util.save_entry(title, newEntry)

                return entry(request, title)
      
    return render(request, "encyclopedia/new.html", {
        'form': NewEntryForm()
    })


def edit(request, entry):
    return render(request, "encyclopedia/edit.html", {
        
    })

def random(request, entry):
    return render(request, "encyclopedia/entry.html", {

    })
