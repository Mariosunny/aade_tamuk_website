from django.db import models


class NewsPost(models.Model):

	title = models.CharField(max_length=128)
	content = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.title


class RegisteredMember(models.Model):

	name = models.CharField(max_length=128)
	email = models.EmailField()
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

	number = models.IntegerField()
	description = models.TextField()


class Picture(models.Model):

	album = models.ForeignKey("Album")
	image = models.ImageField(upload_to='uploads/')
	caption = models.TextField()