
from django.urls import path
from . import views

urlpatterns = [
    # domain.com/tests
    path('', views.index, name='index'),
    # domain.com/tests/12121
    path('<int:t_id>', views.t_detail, name="t_detail")
]
