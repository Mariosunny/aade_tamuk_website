from django.db import models


class NewsPost(models.Model):

	title = models.CharField(max_length=128)
	content = models.TextField()
	date = models.DateTimeField()
	category = models.IntegerField()


class RegisteredMember(models.Model):

	name = models.CharField(max_length=128)
	email = models.EmailField()
	phone_number = models.CharField(max_length=16)
	tshirt_size = models.IntegerField()


class Officer(models.Model):

	name = models.CharField(max_length=128)
	year = models.IntegerField()
	position = models.IntegerField()
	picture = models.ImageField()


class Event(models.Model):

	title = models.CharField(max_length=128)
	details = models.TextField()
	date = models.DateTimeField()