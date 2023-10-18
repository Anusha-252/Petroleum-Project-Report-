import requests
from django.core.management.base import BaseCommand
from home.models import Country, PetroleumProduct, Sale

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Fetch data from the API
        url = "https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json"
        response = requests.get(url)
        dataa = response.json()
        for data in dataa:
            country, _ = Country.objects.get(name=data['country'])
            product, _ = PetroleumProduct.objects.get(name=data['petroleum_product'])
            Sale.objects.create(
                country=country,
                product=product,
                year=data['year'],
                sales=data['sale']
            )