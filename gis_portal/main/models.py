from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class School(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    school_nam = models.CharField(max_length=100, blank=True, null=True)
    schcd = models.BigIntegerField(blank=True, null=True)
    schcat = models.CharField(max_length=23, blank=True, null=True)
    schmgt = models.CharField(max_length=33, blank=True, null=True)
    estdyear = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=24, blank=True, null=True)
    block_name = models.CharField(max_length=34, blank=True, null=True)
    village_na = models.CharField(max_length=34, blank=True, null=True)
    pincode = models.CharField(max_length=15, blank=True, null=True)
    bldstatus = models.CharField(max_length=9, blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    field_22 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school'
