import pymongo

from .models import Account



data = [
       ['Year', 'Sales', 'Expenses', 'Items Sold', 'Net Profit'],
       ['2004', 1000, 400, 100, 600],
       ['2005', 1170, 460, 120, 310],
       ['2006', 660, 1120, 50, -460],
       ['2007', 1030, 540, 100, 200],
       ]

def create_demo_accounts():
    Account.objects.all().delete()
    # Create some rows
    Account.objects.create(year="2004", sales=1000,
                           expenses=400, ceo="Welch")
    Account.objects.create(year="2005", sales=1170,
                           expenses=460, ceo="Jobs")
    Account.objects.create(year="2006", sales=660,
                           expenses=1120, ceo="Page")
    Account.objects.create(year="2007", sales=1030,
                           expenses=540, ceo="Welch")
    Account.objects.create(year="2008", sales=2030,
                           expenses=1540, ceo="Zuck")
    Account.objects.create(year="2009", sales=2230,
                           expenses=1840, ceo="Cook")

