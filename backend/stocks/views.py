from django.shortcuts import render
from django.http import JsonResponse
from stocks.models import Stocks


def search(request):
    query = request.GET
    q = Stocks.objects
    q = q.filter(symbol=query.get("symbol"))
    q = q.order_by('date')
    stocks = list(q.values())
    return JsonResponse(stocks, safe=False)

def symbols(request):
    q = Stocks.objects.values('symbol').order_by('symbol').distinct()
    symbols = list(q)
    return JsonResponse(symbols, safe=False)

