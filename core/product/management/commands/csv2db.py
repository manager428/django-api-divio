import csv
from django.core.management import BaseCommand
from core.product.models import Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Load a products csv file into the database'

    def handle(self, *args, **options):
        if Product.objects.exists():
            print('Products data already loaded...exiting.')
            print(Product.objects.count())
            return
        print('Creating product Data')
        for row in csv.reader(open('core/product/management/commands/MOCK_DATA.csv')):
            product = Product()
            product.name = str(row[0])
            product.description = str(row[1])
            try:
                price = Decimal(row[2])
                product.price = price
                stock = int(row[3])
                product.stock = stock
                product.save()
            except Exception as e:
                print(str(e))
