from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим их в консоль
    for product in latest_products:
        print(f'Product ID: {product.id}, Name: {product.name}, Price: {product.price}')

    return render(request, 'catalog/home.html', {'latest_products': latest_products})


from .models import Contact

def contact(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, message=message)
        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {message}")
        return HttpResponse("Спасибо за ваше сообщение!")

    return render(request, 'catalog/contact.html', {'contacts': contacts})
