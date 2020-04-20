from django.db import models

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

    def __str__(self):
        return self.name

class Cadence(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    start = models.IntegerField()
    end = models.IntegerField()

    def timestamp(self):
        return '{}/{}'.format(start, end)

    def __str__(self):
        timestamp = '{}-{}'.format(start, end)
        return self.timestamp

class Position(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    position = models.CharField(max_length = 100)

    def __str__(self):
        return self.position
