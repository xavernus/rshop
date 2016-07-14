from django.shortcuts import render
from .models import Product
from theme.models import Pagination

def index(request, page=0):
	pagination = Pagination(Product, 'shop-index', 'shop', page)
	products = pagination.records
	return render(request, 'index.html', {'products': products, 'pagination': pagination})

