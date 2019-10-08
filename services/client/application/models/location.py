from django.db import models


class Location(models.Model):
    class Meta:
        ordering = ['coordinates']

    street = models.CharField(max_length=127, blank=False, null=False)
    street_number = models.IntegerField(blank=True, null=False)
    info = models.CharField(max_length=127, blank=False, null=False)
    neighborhood = models.CharField(max_length=127, blank=True, null=True)
    city = models.CharField(max_length=127, blank=True, null=True)
    state = models.CharField(max_length=63, blank=True, null=True)
    country = models.CharField(max_length=63, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    coordinates = models.ForeignKey('Coordinates', related_name='address_coordinates', null=False, blank=False,
                                    on_delete=models.PROTECT)
    zone = models.ForeignKey('Zone', related_name='address_zone', null=True, blank=True,
                             on_delete=models.PROTECT)

    def __str__(self):
        return "{s}, {sn} - {n}, {c} - {state}, {zc} ({info})".format(
            s=self.street, sn=self.street_number, n=self.neighborhood, c=self.city, state=self.state, zc=self.zip_code,
            info=self.info)

    def get_coordinates(self):
        return self.coordinates.__str__()

    def json(self):
        try:
            coordinates = self.coordinates.json() if self.coordinates else None

            zone = self.zone.json() if self.zone else None

            return {
                "id": self.id,
                "street": self.street,
                "street_number": self.street_number,
                "info": self.info,
                "neighborhood": self.neighborhood,
                "city": self.city,
                "state": self.state,
                "country": self.country,
                "zip_code": self.zip_code,
                "coordinates": coordinates,
                "zone": zone
            }

        except Exception as e:
            print("Exception on Locations json: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def handler(dictionary):
        from application.models.coordinates import Coordinates
        try:
            street = dictionary.get("street")
            street_number = dictionary.get("street_number", None)
            if not street_number:
                street_number = 42
            info = "N/A"
            neighborhood = dictionary.get("neighborhood")
            city = dictionary.get("city")
            state = dictionary.get("state")
            country = dictionary.get("country")
            zip_code = dictionary.get("zip_code")
            # coordinates = Coordinates.handler(dictionary=dictionary.get("coordinates"))

            return Location(
                street=street, street_number=street_number, info=info, neighborhood=neighborhood, city=city,
                state=state, country=country, zip_code=zip_code, coordinates=None, zone=None
            )
        except Exception as e:
            print("Error on Location handler:  {} {}".format(type(e), e))
            raise e
