from django.shortcuts import render, HttpResponse
import json
# Create your views here.
def home(request):
    return render(request, 'index.html')
    #text = """
    #<h1><b>"Hello World!" Это задание из Модуля 1</b></h1>
    #<i><u>Автор:</u> Никита Тимофеев</i>
    #"""
    #return HttpResponse(text)
def about(request):
    return HttpResponse("Никита Тимофеев")

with open("countries.json", "r") as f:
    countries = json.load(f)

with open("countries.json", "r") as f:
    language = json.load(f)

def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries_list.html', context)

def languages(request):
    context = {'language': language}
    return render(request, 'languages.html', context)

def country_page(request, id):
    for country in countries:
        if country['id'] == id:
            context = {
                'country': country
            }
            return HttpResponse("тест")

            #return render(request, 'country_page.html', context)

            #text = f"""<h2>{country['country']}</h2>
            #язык: {languages['languages']}
            #"""
            #return HttpResponse(text)
            #context = {
                #'item': item
            #}
            #return render(request, 'item-page.html', context)