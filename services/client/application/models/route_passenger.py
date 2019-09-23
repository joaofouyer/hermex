from django.db import models


class RoutePassenger(models.Model):
    class Meta:
        ordering = ['pk']

    pick_up = models.ForeignKey('RouteStop', blank=False, null=False, on_delete=models.PROTECT,
                                related_name='passenger_pickup')
    drop_off = models.ForeignKey('RouteStop', blank=False, null=False, on_delete=models.PROTECT,
                                 related_name='passenger_dropoff')
