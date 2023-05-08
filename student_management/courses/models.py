from django.db import models
from django.urls import reverse

class Course(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[str(self.id)])
