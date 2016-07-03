# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    image = models.ImageField('Изображение')
    parent = models.OneToOneField('self', null=True, blank=True)

class Product(models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    article = models.CharField('Артикул', max_length=255, unique=True)
    image = models.ImageField('Изображение')
    price = models.FloatField('Цена')
    quantity = models.IntegerField('Количество')
    category = models.ForeignKey(Category, null=True, blank=True)

class Tag(models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    products = models.ManyToManyField(Product)

class Order(models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    date = models.DateTimeField('Дата')
    price = models.FloatField('Сумма')
    user = models.ForeignKey(User)
    products = models.ManyToManyField(Product)

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User)
