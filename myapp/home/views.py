from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Sale
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum

def index(request):
    return render(request, 'index.html')


def report(request):
    sales_data = Sale.objects.all()

    records_per_page = 20
    paginator = Paginator(sales_data, records_per_page)
    page = request.GET.get('page')  


    try:
        # Get the records for the current page
        sales_data = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, display the first page
        sales_data = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, display the last page
        sales_data = paginator.page(paginator.num_pages)
    
    context = {
        'sales_data' : sales_data

    }
    
    return render(request, 'report.html', context)

def total_sales_by_petroleum(request):
    # Query the database to calculate total sales for each petroleum product
    total_sales = Sale.objects.values('product__name').annotate(total_sale=Sum('sales'))
    return render(request, 'total_sales.html', {'total_sales': total_sales})

# def country_status(request):
#     from django.db.models import Sum
# from your_app.models import Sale

from django.shortcuts import render
from home.models import Sale
from django.db.models import Sum

def top_and_lowest_countries_sales(request):
    # Find the top 3 countries with the highest total sales
    top_highest_sales = Sale.objects.values('country__name').annotate(total_sale=Sum('sales')).order_by('-total_sale')[:3]

    # Find the top 3 countries with the lowest total sales
    top_lowest_sales = Sale.objects.values('country__name').annotate(total_sale=Sum('sales')).order_by('total_sale')[:3]

    context = {
        'top_highest_sales': top_highest_sales,
        'top_lowest_sales': top_lowest_sales,
    }

    return render(request, 'country_sales.html', context)


def average_sales_by_interval(request):
    intervals = [
        (2007, 2010),
        (2011, 2014),
    ]

    # Initialize a list to store the results
    results = []

    # Calculate the average sales for each product and interval
    for start_year, end_year in intervals:
        average_sales = (
            Sale.objects.filter(year__gte=start_year, year__lte=end_year, sales__gt=0)
            .values('product__name')
            .annotate(average_sale=Sum('sales') / (end_year - start_year + 1))
        )

        for item in average_sales:
            result = {
                'Product': item['product__name'],
                'Year': f"{start_year}-{end_year}",
                'Avg': item['average_sale'],
            }
            results.append(result)

    # Sort the results by product name
    results.sort(key=lambda x: x['Product'])

    context = {'results': results}
    return render(request, 'average_sales.html', context)