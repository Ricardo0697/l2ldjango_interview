from django.urls import path

from . import views
# from .format_date  import format_date

urlpatterns = [
    path('', views.index, name='index'),
    # path('format_date' , format_date)
]
