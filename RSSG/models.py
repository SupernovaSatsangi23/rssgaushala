from django.db import models

# Create your models here.

class Home(models.Model):
	title = models.TextField()
	announcements = models.TextField()

class Alpha(models.Model):
	profile_img = models.ImageField(upload_to='alpha_profile')
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	since = models.CharField(max_length=4)
	to = models.CharField(max_length=4)

	def __str__(self):
		return self.name

# you forgot to do migrations dude !!
class About(models.Model):
	content_1 = models.TextField()
	content_2 = models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='gallery')

	# to show up like this in the admin page

class Gallery(models.Model):
	image_array_1 = models.ImageField(default='default.jpg', upload_to='gallery')
	image_array_2 = models.ImageField(default='default.jpg', upload_to='gallery')
	image_array_3 = models.ImageField(default='default.jpg', upload_to='gallery')
	vid = models.FileField(upload_to='gallery')

class History(models.Model):
	image = models.ImageField(upload_to='history')
	title = models.TextField()
	year = models.CharField(max_length=4)
	context = models.TextField()

	def __str__(self):
		return self.title

class Operations(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='ops')
	name = models.TextField()
	implementation_year = models.CharField(max_length=5)
	purpose_of_this_op = models.TextField()
	explanation = models.TextField()

	def __str__(self):
		return self.name

