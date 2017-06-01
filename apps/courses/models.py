from __future__ import unicode_literals

from django.db import models

class Description(models.Model):
	description = models.TextField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
	  return "id: " + str(self.id) + ", description: " + self.description
class Course(models.Model):
	name = models.CharField(max_length=40)
	description = models.OneToOneField(Description)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
	  return "id: " + str(self.id) + ", description: " + self.description
