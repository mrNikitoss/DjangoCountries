from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    text = """
    <h1><b>"Hello World!" Это задание из Модуля 1</b></h1>
    <i><u>Автор:</u> Никита Тимофеев</i> 
    """
    return HttpResponse(text)
def about(request):
    return HttpResponse("Никита Тимофеев")