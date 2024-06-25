from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'rest_category'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'address'
        managed = True
        verbose_name = 'address'
        verbose_name_plural = 'address'

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}"


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    qrcode = models.TextField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'restaurant'
        managed = True
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.name