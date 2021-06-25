from django.shortcuts import render
from django.http import JsonResponse
from stocks.models import Stocks
from dateutil.parser import parse

def search(request):
    query = request.GET
    q = Stocks.objects
    q = q.filter(symbol=query.get("symbol"))
    if query.get("from"):
        q = q.filter(date__gte=parse(query.get("from")))
    if query.get("to"):
        q = q.filter(date__lte=parse(query.get("to")))
    q = q.order_by('date')
    stocks = list(q.values())
    return JsonResponse(stocks, safe=False)

def symbols(request):
    q = Stocks.objects.values('symbol').order_by('symbol').distinct()
    symbols = list(q)
    return JsonResponse(symbols, safe=False)

