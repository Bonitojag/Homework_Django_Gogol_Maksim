import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    @staticmethod
    def json_read_data():
        with open('catalog.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        data = self.json_read_data()

        # Сначала обрабатываем категории
        for item in data:
            if item['model'] == 'catalog.category':
                category_for_create.append(
                    Category(
                        pk=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields'].get('description', ''),
                    )
                )

        # Сохраняем категории в базу данных
        Category.objects.bulk_create(category_for_create)

        # Теперь обрабатываем продукты
        for item in data:
            if item['model'] == 'catalog.product':
                product_for_create.append(
                    Product(
                        pk=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields'].get('description', ''),
                        image=item['fields'].get('image', ''),
                        category=Category.objects.get(pk=item['fields']['category']),
                        price=item['fields']['price'],
                    )
                )

        # Сохраняем продукты в базу данных
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))

