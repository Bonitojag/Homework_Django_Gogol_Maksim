from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=125, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Ведите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категрии"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=125, verbose_name="Продукт", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


    def __str__(self):
        return self.name
