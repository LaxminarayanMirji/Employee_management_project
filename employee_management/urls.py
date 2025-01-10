from django.contrib import admin
from django.urls import path
from employee.views import records_view, search_view, sort_view, create_view, edit_view, delete_view, edit_emp_view, delete_emp_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', records_view),
    path('search/', search_view),
    path('sort/', sort_view),

    path('emp_create/', create_view),
    path('emp_edit/', edit_view),
    path('emp_delete/', delete_view),

    path('edit/<int:id>/', edit_emp_view),
    path('delete/<int:id>/', delete_emp_view),

    path('records/', records_view, name='records'),
]
