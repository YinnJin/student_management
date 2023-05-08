from django.db import models
from django.urls import reverse
from courses.models import Course

app_label = 'grades'

class Grade(models.Model):
    GRADE_CHOICES = [
        (0, 'F'),
        (1, 'D'),
        (2, 'C'),
        (3, 'B'),
        (4, 'A')
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    grade = models.IntegerField(choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.course.title} - {self.student_name} - {self.get_grade_display()}"

    def get_absolute_url(self):
        return reverse('grades:grade_detail', args=[str(self.id)])