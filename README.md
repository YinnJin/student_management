# Student Management System

This is a simple student management system built with Django.

## Installation

1. Clone the repository.
2. Install the required dependencies using pip: `pip install -r requirements.txt`.
3. Create a database by running the following command: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Visit `http://localhost:8000` in your web browser.

### URLs

- `/`: displays the home page.
- `/courses/`: displays a list of all courses.
- `/courses/add/`: allows users to create a new course.
- `/courses/<int:pk>/`: displays the details of a specific course.
- `/grades/`: displays a list of all grades.
- `/grades/add/`: allows users to create a new grade.
- `/grades/<int:pk>/`: displays the details of a specific grade.

## Course Model

The `Course` model represents a course that can be taken by students. It has the following fields:

- `title` (CharField): the title of the course
- `description` (TextField): a description of the course
- `instructor` (CharField): the teacher of the course
- `price` (DecimalField): the cost of the course

## Grade Model

The `Grade` model represent a grade given to the student from there assignment for the course. It has the following fields:

- `GRADE_CHOICES` (): letter grades
- `course` (ForeignKey): what course the student got the grade from
- `student_name` (CharField): name of the student
- `grade` (IntegerField): letter grades given to the student

### Technologies Used

- Django
- HTML
- CSS

## License

This project is licensed under the MIT License. See the [LICENSE] file for details.
