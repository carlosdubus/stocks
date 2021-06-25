from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stocks
import requests, zipfile, io, csv
from dateutil.parser import parse
from decimal import Decimal
from datetime import datetime, timedelta
import time

HEADERS = {
    "referer": "https://www1.nseindia.com/products/content/equities/equities/archieve_eq.htm"
}

def build_url(date):
    month = date.strftime("%b").upper()
    return "https://www1.nseindia.com/content/historical/EQUITIES/%s/%s/cm%s%s%sbhav.csv.zip" % (
        date.year,
        month,
        '%02d' % date.day,
        month,
        date.year
    )

def row_to_model(row):
    # 0 SYMBOL	1 SERIES	2 OPEN	3 HIGH	4 LOW	5 CLOSE	6 LAST	7 PREVCLOSE	8 TOTTRDQTY	9 TOTTRDVAL	10 TIMESTAMP	11 TOTALTRADES	12 ISIN
    # ['MBLINFRA', 'EQ', '19.05', '19.4', '17.65', '18.4', '18.5', '18.5', '123249', '2288644.65', '28-APR-2021', '839', 'INE912H01013', '']
    return Stocks(
        symbol=row[0],
        series=row[1],
        price_open=Decimal(round(float(row[2]), 2)),
        price_high=Decimal(round(float(row[3]), 2)),
        price_low=Decimal(round(float(row[4]), 2)),
        price_close=Decimal(round(float(row[5]), 2)),
        price_last=Decimal(round(float(row[6]), 2)),
        price_prev_close=Decimal(round(float(row[7]), 2)),
        tottrd_qty=int(row[8]),
        tottrd_value=Decimal(round(float(row[9]), 2)),
        date=parse(row[10]).date(),
        total_trades=int(row[11]),
        isin=row[12]
    )

def parse_csv(csv_file):
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    next(csv_reader, None) # skip headers
    for row in csv_reader:
        try:
            yield (row, row_to_model(row))
        except Exception as e:
            print("ERROR: Could not process row: %s because %s", (row, e))
        

def parse_url(zip_url):
    r = requests.get(zip_url, stream=True, headers=HEADERS)
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        zfile = z.infolist()[0]
        with z.open(zfile.filename, "r") as csv_file:
            csv_file = io.TextIOWrapper(csv_file, encoding='utf8', newline='')
            for stocks in parse_csv(csv_file):
                yield stocks


def upsert_stocks(stocks):
    Stocks.objects.filter(symbol=stocks.symbol, date=stocks.date).delete()
    return stocks.save()

def import_date(date):
    # skip weekends, no data for weekends
    if date.weekday() >= 5:
        return
    try:
        url = build_url(date)
        print(url)
        for row, stocks in parse_url(url):
            upsert_stocks(stocks)
    except Exception as e:
        print(e)

class Command(BaseCommand):
    help = """Imports stocks from https://www1.nseindia.com
    Example:
      python manage.py import --from=2020-01-01
    """

    def add_arguments(self, parser):
        today = datetime.now()
        last_30 = datetime.now() - timedelta(31)
        parser.add_argument('--from', nargs='?', help='From date. (2021-01-01)', default=last_30.strftime('%Y-%m-%d'))
        parser.add_argument('--to', nargs='?', help='To date.', default=today.strftime('%Y-%m-%d'))

    def handle(self, *args, **options):
        date_from = parse(options["from"])
        date_to = parse(options["to"])
        cur_date = date_from
        while cur_date < date_to:
            import_date(cur_date)
            cur_date += timedelta(1)
            time.sleep(5) # do not get blocked
