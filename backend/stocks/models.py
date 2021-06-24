from django.db import models


class Stocks(models.Model):
    class Meta:
        verbose_name_plural = "stocks"
        unique_together = ('symbol', 'date',)
    symbol = models.CharField(max_length=100)
    series = models.CharField(max_length=10)
    price_open = models.DecimalField(max_digits=15, decimal_places=2)
    price_close = models.DecimalField(max_digits=15, decimal_places=2)
    price_last = models.DecimalField(max_digits=15, decimal_places=2)
    price_prev_close = models.DecimalField(max_digits=15, decimal_places=2)
    price_low = models.DecimalField(max_digits=15, decimal_places=2)
    price_high = models.DecimalField(max_digits=15, decimal_places=2)
    tottrd_qty = models.IntegerField()
    tottrd_value = models.DecimalField(max_digits=15, decimal_places=2)
    total_trades = models.IntegerField()
    isin = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return "Stocks [symbol=%s date=%s]" % (self.symbol, self.date)
