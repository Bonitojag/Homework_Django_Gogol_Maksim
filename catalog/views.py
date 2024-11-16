from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product, Contact, Category

def home(request):
    """
    Отображает главную страницу с категорями и продуктами

    Запрашивает все категории и продукты из базы данных,
    осуществляет пагинацию продуктов (по 3 на страницу) и
    выбирает последние 5 продуктов для отображения.
    Возвращает контекст с категориями, текущей страницей продуктов
    и последними 5 продуктами.
    :param request: Объект HTTP-запроса.
    :return: Возвращает шаблон 'catalog/home.html' м контекстом
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    last_five_products = Product.objects.order_by('-created_at')[:5]
    print(last_five_products)
    context = {"categories": categories, "products": page_obj, "last_five_products": last_five_products,}
    return render(request, 'catalog/home.html', context)

def category_products(request, category_id):
    """
    Отображает продукты находящиеся в определенной категории

    Находит категорию по ID и извлекает все продукты,
    относящиеся к этой категории. Возвращает контекст
    с категорией и соответствующими продуктами.

    :param request: Объект HTTP-запроса
    :param category_id: ID категории для которой нужно отображать продукты
    :return: Возвращает шаблон 'catalog/category_products.html' с контекстом
    """
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    context = {'category': category, 'products': products}
    return render(request, 'catalog/category_products.html', context)

def contact(request):
    """
    Отображает страницу для отправки сообщения

    Если запрос POST, создает новый контакт с данными из формы.
    В противном случае отображает список всех контактов.

    :param request: Объект HTTP-запроса
    :return: Возвращает шаблон 'catalog/contact.html' с контекстом.
            Или сообщение об успешной отправке.
    """
    contacts = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, message=message)
        return HttpResponse("Спасибо за ваше сообщение!")

    context = {'contacts': contacts}
    return render(request, 'catalog/contact.html', context)

def product_detail(request, pk):
    """
    Отображает страницу с деталями о конкретном продукте.

    Находит продукт по первичному ключу и передает его в контекст.
    :param request: Объект HTTP-запроса
    :param pk: Первичный ключ
    :return: Возвращает шаблон 'catalog/product_detail.html' с контекстом.
    """
    product = get_object_or_404(Product, pk=pk)
    context = {'object': product}
    return render(request, 'catalog/product_detail.html', context)

def create_product(request):
    """
    Отображает страницу для обработки и создания нового продукта.

    Если запрос POST, проверяет форму на валидность и сохраняет новый продукт.
    В противном случае отображает пустую форму для создания продукта.

    :param request: Объект HTTP-запроса
    :return: Возвращает шаблон 'catalog/create_product.html' с контекстом.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Продукт успешно создан!")
    else:
        form = ProductForm()
    return render(request, 'catalog/create_product.html', {'form': form})
