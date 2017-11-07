from django.db import models
from .helpers import RandomFileName

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
	image = models.ImageField(upload_to=RandomFileName('resources_images'),
							  default='media/default.png',
							  blank=True)

	def __str__(self):
		return self.name

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url
# Create your models here.
