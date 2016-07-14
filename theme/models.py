from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from rshop import settings
import math

class Pagination:
	def __init__(self, model_name, route_name, default_route, page_route, page=0,):
		if page > 0:
			page = int(page) - 1
		self.records_count = model_name.objects.count()
		self.pages_count = int(math.ceil(self.records_count/settings.PRODUCTS_PER_PAGE)+1)
		start_offset = page*settings.PRODUCTS_PER_PAGE
		end_offset = (page + 1)*settings.PRODUCTS_PER_PAGE

		self.records = model_name.objects.all()[start_offset:end_offset]

		if self.pages_count > 1:
			self.pages = []
			self.pages.append((1, reverse('shop')))

			for i in range(1, self.pages_count):
				self.pages.append((i+1, reverse('shop-index', kwargs={'page': i+1})))
		else:
			self.pages = False
