from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course
from django.urls import reverse_lazy

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'instructor', 'price']

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'instructor', 'price']

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:course_list')
