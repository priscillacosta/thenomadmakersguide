from django.db import models

class Resource(models.Model):
	MAKER_BRAND = 'MB'
	EVENT = 'EV'
	STORE = 'ST'
	SPACE = 'SP'
	CATEGORY_CHOICES = (
		(MAKER_BRAND, 'Maker or Brand'),
		(EVENT, 'Event'),
		(STORE, 'Store'),
		(SPACE, 'Space'),
	)
	name = models.CharField(max_length=100, blank=True)
	url = models.URLField(blank=True)
	local = models.CharField(max_length=250, blank=True)
	category = models.CharField(max_length=100,
				choices=CATEGORY_CHOICES,
				default=MAKER_BRAND,
				blank=True)

	def __str__(self):
 		return self.name


# Create your models here.
