from django.test import TestCase
from django.urls import reverse
from courses.models import Course
from grades.models import Grade

class GradeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a course
        course = Course.objects.create(title='Test Course')
        
        # Create a grade
        Grade.objects.create(course=course, student_name='Jane Smith', grade=4)
    
    def test_student_name_label(self):
        grade = Grade.objects.first()
        field_label = grade._meta.get_field('student_name').verbose_name
        self.assertEquals(field_label, 'student name')
    
    def test_course_label(self):
        grade = Grade.objects.first()
        field_label = grade._meta.get_field('course').verbose_name
        self.assertEquals(field_label, 'course')
    
    def test_grade_label(self):
        grade = Grade.objects.first()
        field_label = grade._meta.get_field('grade').verbose_name
        self.assertEquals(field_label, 'grade')
    
    def test_grade_display(self):
        grade = Grade.objects.first()
        grade_display = grade.get_grade_display()
        self.assertEquals(grade_display, 'A')
    
    def test_absolute_url(self):
        grade = Grade.objects.first()
        url = reverse('grades:grade_detail', args=[str(grade.id)])
        self.assertEquals(url, f'/grades/{grade.id}/')

    def test_grade_edit(self):
        grade = Grade.objects.first()
        grade.grade = 3
        grade.save()
        updated_grade = Grade.objects.get(id=grade.id)
        self.assertEquals(updated_grade.grade, 3)

    def test_grade_delete(self):
        grade = Grade.objects.first()
        grade_id = grade.id
        grade.delete()
        with self.assertRaises(Grade.DoesNotExist):
            Grade.objects.get(id=grade_id)