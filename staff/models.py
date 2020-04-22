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

    def get_cadences(self):
        return '\n | \n'.join([str(c) for c in self.cadence.all()])

    def get_positions(self):
        return '\n | \n'.join([str(p) for p in self.position.all()])

    def __str__(self):
        return self.name

    get_cadences.short_description = 'Cadences'
    get_positions.short_description = 'Positions'


class Cadence(models.Model):
    year = datetime.datetime.now().year
    start = models.IntegerField(default = year - 1)
    end = models.IntegerField(default = year)

    class Meta:
        ordering = ['-end']

    def timestamp(self):
        return '{}/{}'.format(self.start, self.end)

    def __str__(self):
        return self.timestamp()

class Position(models.Model):
    position = models.CharField(max_length = 100)

    def __str__(self):
        return self.position
