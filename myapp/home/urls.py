from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('report/', views.report, name="report"),
    path('total-sales/', views.total_sales_by_petroleum, name='total_sales'),
    path('country_sales/',views.top_and_lowest_countries_sales, name='top_lowest_sales'),
    path('average-sales/', views.average_sales_by_interval, name='average_sales'),
]