from django.db import models


class Coordinates(models.Model):
    class Meta:
        ordering = ['latitude', 'longitude']

    latitude = models.FloatField(default=-23.554189, blank=False, null=False)
    longitude = models.FloatField(default=-46.662206, blank=False, null=False)
    geometry = models.ForeignKey('Geometry', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.latitude, self.longitude
