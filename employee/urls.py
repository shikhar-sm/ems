from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('all_employees/',views.all_employees),
    path('employee_list/<int:d_id>/', views.department_employee_list),
    path('employee/<str:e_id>/', views.employee_with_id),
    path('create_employee/',views.create_employee),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]