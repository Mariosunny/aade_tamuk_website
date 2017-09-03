from django.db import models

class Slide(models.Model):

	position = models.IntegerField()
	title = models.CharField(max_length=64)
	body = models.TextField(max_length=256)
	link = models.URLField()
	image = models.ImageField(upload_to='uploads/')

	def __str__(self):

		return self.title


class NewsPost(models.Model):

	title = models.CharField(max_length=128)
	content = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(blank=True, upload_to='uploads/')

	def __str__(self):

		return self.title


class RegisteredMember(models.Model):

	name = models.CharField(max_length=128)
	email = models.EmailField(unique=True)
	phone_number = models.CharField(max_length=16)
	tshirt_size = models.IntegerField()

	def __str__(self):

		return self.name


class Officer(models.Model):

	name = models.CharField(max_length=128)
	year = models.IntegerField()
	position = models.IntegerField()
	picture = models.ImageField()

	def __str__(self):

		return self.name


class Event(models.Model):

	title = models.CharField(max_length=128)
	location = models.CharField(max_length=256, blank=True, null=True)
	details = models.TextField(blank=True, null=True)
	date = models.DateTimeField()

	def __str__(self):

		return self.title


class Album(models.Model):
	def __str__(self):
		return 'Album: ' + self.name
	name = models.CharField(max_length=128, default='Album')
	description = models.TextField(blank=True, null=True)
	category = models.IntegerField()

	def __str__(self):

		return self.name


class Picture(models.Model):

	album = models.ForeignKey("Album")
	image = models.ImageField(upload_to='uploads/')
	caption = models.TextField(blank=True, null=True)

	def __str__(self):

		return self.caption
