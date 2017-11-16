from django.db import models
from django.conf import settings

class Post(models.Model):
	post_title = models.CharField(max_length=200)
	post_body = models.TextField()
	post_author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
	)
	pub_date = models.DateTimeField('date published')