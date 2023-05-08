# Generated by Django 3.2.7 on 2023-05-07 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('grade', models.IntegerField(choices=[(0, 'F'), (1, 'D'), (2, 'C'), (3, 'B'), (4, 'A')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_grades', to='courses.course')),
            ],
        ),
    ]