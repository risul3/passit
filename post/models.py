from django.db import models
from django.conf import settings

class Tag(models.Model):
	tag_name = models.CharField(max_length=50)

	def __str__(self):
		return self.tag_name

	class Meta:
		ordering = ('tag_name',)

class Post(models.Model):
	post_title = models.CharField(max_length=200)
	post_body = models.TextField()
	post_author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
	)
	slug = models.SlugField(
		allow_unicode=True,
		unique=True,
	)
	tags = models.ManyToManyField(Tag)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.post_title

	class Meta:
		ordering = ('pub_date',)