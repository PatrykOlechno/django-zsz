from django.db import models
import datetime

class Member(models.Model):
    class Degree(models.TextChoices):
        MAGISTER = 'mgr'
        MAGISTER_INZ = 'mgr inż.'
        LICENCJAT = 'lic.'
        INZYNIER = 'inż.'
        KSIADZ = 'ks.'
        KSIADZ_LIC = 'ks. lic.'
        KSIADZ_MGR = 'ks. mgr'
        BRAK = ''

    degree = models.CharField(
        max_length = 9,
        choices = Degree.choices,
        default = Degree.BRAK,
        blank = True
    )
    name = models.CharField(max_length = 100)
    cadence = models.ManyToManyField('Cadence')
    position = models.ManyToManyField('Position')

    def __str__(self):
        return self.name

class Cadence(models.Model):
    year = datetime.datetime.now().year
    start = models.IntegerField(default = year - 1)
    end = models.IntegerField(default = year)

    def timestamp(self):
        return '{}/{}'.format(self.start, self.end)

    def __str__(self):
        return self.timestamp()

class Position(models.Model):
    position = models.CharField(max_length = 100)

    def __str__(self):
        return self.position
