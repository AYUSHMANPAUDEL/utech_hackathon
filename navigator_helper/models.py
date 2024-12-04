from django.db import models

# Create your models here.
class Hotels(models.Model):
    name = models.TextField()
    latitude = models.TextField()  # Corrected typo from latitiude to latitude
    longitude = models.TextField()
    hotel_image1 = models.ImageField(upload_to="media/hotel_images")
    hotel_image2 = models.ImageField(upload_to="media/hotel_images")
    hotel_image3 = models.ImageField(upload_to="media/hotel_images")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"