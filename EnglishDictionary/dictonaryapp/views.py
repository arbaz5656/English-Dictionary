from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.

def index(request):
    return render(request,"index.html")

def word(request):
    search0=request.GET.get('search')
    dictonary0=PyDictionary()
    meaning0=dictonary0.meaning(search0)
    synonyms0=dictonary0.synonym(search0)
    antonyms0=dictonary0.antonym(search0)
    context={
        'mean':meaning0['Noun'][0],
        'syno':synonyms0,
        'anto':antonyms0
    }
    return render(request,"word.html",context)
