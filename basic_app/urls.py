
from django.urls import path, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name="schools"),
    path('create/', views.SchoolCreateView.as_view(), name="create"),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name="detail"),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name="delete")
]
