from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {message}")
        return HttpResponse("Спасибо за ваше сообщение!")

    return render(request, 'catalog/contact.html')
