from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime


class WaterConYear(models.Model):
    year = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(3000)
    ])
    consumption = models.FloatField(validators=[
        MinValueValidator(0), MaxValueValidator(10000)
    ])

    square_consumption = models.FloatField(
        validators=[
            MinValueValidator(0)
        ],
        null=True
    )

    def __unicode__(self):
        return 'Water Consumption by year'

    def __len__(self):
        return self.objects.count()

    def add_values(self, list_of_tuples):
        for year, con in list_of_tuples:
            self.objects.update_or_create(
                year=year,
                consumption=con,
                square_consumption=con**2
            )

    def get_all_as_tuple(self):
        return [(year, con, con2) for year, con, con2 in self.objects.all()]

    def get_all_as_dict(self):
        return [
            {
                'year': year,
                'con': con,
                'con2': con2
            }
            for year, con, con2 in self.objects.all()
        ]


def csv_file_path(instance, filename):
    name, format = filename.split('.')
    new_filename = name + datetime.now().strftime('%Y-%m-%d') + format
    return 'csv/' + new_filename


class UploadedCSV(models.Model):
    name = models.CharField(max_length=128)
    date_upload = models.DateField(default=datetime.now)
    file = models.FileField(upload_to=csv_file_path)
