from django.urls import path
from .views import GradeListView, GradeCreateView, GradeDetailView, GradeUpdateView, GradeDeleteView, GradeHomeView

app_name = 'grades'

urlpatterns = [
    path('', GradeHomeView.as_view(), name='grade_home'),
    path('list/', GradeListView.as_view(), name='grade_list'),
    path('add/', GradeCreateView.as_view(), name='grade_add'),
    path('<int:pk>/', GradeDetailView.as_view(), name='grade_detail'),
    path('<int:pk>/edit/', GradeUpdateView.as_view(), name='grade_edit'),
    path('<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
]