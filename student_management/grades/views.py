from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Grade
from django.urls import reverse_lazy

class GradeHomeView(TemplateView):
    template_name = 'grades/grade_home.html'

class GradeListView(ListView):
    model = Grade
    template_name = 'grades/grade_list.html'
    context_object_name = 'grades'

class GradeCreateView(CreateView):
    model = Grade
    fields = ['course', 'student_name', 'grade']

class GradeDetailView(DetailView):
    model = Grade
    template_name = 'grades/grade_detail.html'
    context_object_name = 'grade'

class GradeUpdateView(UpdateView):
    model = Grade
    fields = ['course', 'student_name', 'grade']

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades/grade_confirm_delete.html'
    success_url = reverse_lazy('grades:grade_list')