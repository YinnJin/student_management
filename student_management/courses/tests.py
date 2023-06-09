from django.test import TestCase
from .models import Course

class CourseModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Course.objects.create(title='Mathematics', description='Calculus and Algebra', instructor='John Doe', price='100.00')

    def test_title_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_instructor_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('instructor').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title(self):
        course = Course.objects.get(id=1)
        expected_object_name = course.title
        self.assertEqual(expected_object_name, str(course))

    def test_get_absolute_url(self):
        course = Course.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(course.get_absolute_url(), '/courses/1/')

    def test_course_creation(self):
        course = Course.objects.create(
            title='Physics', 
            description='Mechanics and Thermodynamics', 
            instructor='Jane Doe', 
            price='150.00'
        )
        self.assertEqual(course.title, 'Physics')
        self.assertEqual(course.description, 'Mechanics and Thermodynamics')
        self.assertEqual(course.instructor, 'Jane Doe')
        self.assertEqual(course.price, '150.00')

    def test_course_edit(self):
        course = Course.objects.get(id=1)
        course.instructor = 'Jane Doe'
        course.save()
        updated_course = Course.objects.get(id=1)
        self.assertEqual(updated_course.instructor, 'Jane Doe')

    def test_course_delete(self):
        course = Course.objects.get(id=1)
        course_id = course.id
        course.delete()
        with self.assertRaises(Course.DoesNotExist):
            Course.objects.get(id=course_id)