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

class Ahmadnagar(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=10, blank=True, null=True)
    school_nam = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=13, blank=True, null=True)
    cluster_na = models.CharField(max_length=22, blank=True, null=True)
    village_na = models.CharField(max_length=21, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahmadnagar'


class Akola(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=5, blank=True, null=True)
    school_nam = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=25, blank=True, null=True)
    village_na = models.CharField(max_length=24, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'akola'


class Amravati(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=8, blank=True, null=True)
    school_nam = models.CharField(max_length=72, blank=True, null=True)
    block_name = models.CharField(max_length=15, blank=True, null=True)
    cluster_na = models.CharField(max_length=23, blank=True, null=True)
    village_na = models.CharField(max_length=22, blank=True, null=True)
    pincode = models.CharField(max_length=15, blank=True, null=True)
    unnamed_7 = models.IntegerField(db_column='unnamed:_7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amravati'


class Aurangabad(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=24, blank=True, null=True)
    school_nam = models.CharField(max_length=87, blank=True, null=True)
    block_name = models.CharField(max_length=10, blank=True, null=True)
    cluster_na = models.CharField(max_length=26, blank=True, null=True)
    village_na = models.CharField(max_length=24, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aurangabad'

class Beed(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=3, blank=True, null=True)
    school_nam = models.CharField(max_length=74, blank=True, null=True)
    block_name = models.CharField(max_length=9, blank=True, null=True)
    cluster_na = models.CharField(max_length=24, blank=True, null=True)
    village_na = models.CharField(max_length=26, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beed'


class Bhandara(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=8, blank=True, null=True)
    school_nam = models.CharField(max_length=72, blank=True, null=True)
    block_name = models.CharField(max_length=9, blank=True, null=True)
    cluster_na = models.CharField(max_length=17, blank=True, null=True)
    village_na = models.CharField(max_length=21, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bhandara'


class Buldhana(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=7, blank=True, null=True)
    school_nam = models.CharField(max_length=76, blank=True, null=True)
    block_name = models.CharField(max_length=13, blank=True, null=True)
    cluster_na = models.CharField(max_length=19, blank=True, null=True)
    village_na = models.CharField(max_length=31, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buldhana'


class Chandrapur(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=10, blank=True, null=True)
    school_nam = models.CharField(max_length=78, blank=True, null=True)
    block_name = models.CharField(max_length=10, blank=True, null=True)
    cluster_na = models.CharField(max_length=32, blank=True, null=True)
    village_na = models.CharField(max_length=27, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chandrapur'


class Dhule(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=5, blank=True, null=True)
    school_nam = models.CharField(max_length=59, blank=True, null=True)
    block_name = models.CharField(max_length=12, blank=True, null=True)
    cluster_na = models.CharField(max_length=13, blank=True, null=True)
    village_na = models.CharField(max_length=18, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dhule'

class Gadchiroli(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=10, blank=True, null=True)
    school_nam = models.CharField(max_length=56, blank=True, null=True)
    block_name = models.CharField(max_length=10, blank=True, null=True)
    cluster_na = models.CharField(max_length=15, blank=True, null=True)
    village_na = models.CharField(max_length=23, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gadchiroli'


class Hingoli(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=7, blank=True, null=True)
    school_nam = models.CharField(max_length=83, blank=True, null=True)
    block_name = models.CharField(max_length=14, blank=True, null=True)
    cluster_na = models.CharField(max_length=20, blank=True, null=True)
    village_na = models.CharField(max_length=27, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hingoli'

class Jalgaon(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=7, blank=True, null=True)
    school_nam = models.CharField(max_length=75, blank=True, null=True)
    block_name = models.CharField(max_length=16, blank=True, null=True)
    cluster_na = models.CharField(max_length=25, blank=True, null=True)
    village_na = models.CharField(max_length=29, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jalgaon'


class Jalna(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=5, blank=True, null=True)
    school_nam = models.CharField(max_length=98, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=18, blank=True, null=True)
    village_na = models.CharField(max_length=22, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jalna'


class Kolhapur(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=8, blank=True, null=True)
    school_nam = models.CharField(max_length=80, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=29, blank=True, null=True)
    village_na = models.CharField(max_length=32, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kolhapur'


class Latur(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=5, blank=True, null=True)
    school_nam = models.CharField(max_length=98, blank=True, null=True)
    block_name = models.CharField(max_length=15, blank=True, null=True)
    cluster_na = models.CharField(max_length=35, blank=True, null=True)
    village_na = models.CharField(max_length=34, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'latur'

class Mumbaifull(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    school_cod = models.BigIntegerField(blank=True, null=True)
    distname = models.CharField(max_length=17, blank=True, null=True)
    school_nam = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mumbaifull'


class Nagpur(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=83, blank=True, null=True)
    block_name = models.CharField(max_length=15, blank=True, null=True)
    cluster_na = models.CharField(max_length=34, blank=True, null=True)
    village_na = models.CharField(max_length=23, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagpur'


class Nanded(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=81, blank=True, null=True)
    block_name = models.CharField(max_length=13, blank=True, null=True)
    cluster_na = models.CharField(max_length=16, blank=True, null=True)
    village_na = models.CharField(max_length=25, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nanded'


class Nandurbar(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=9, blank=True, null=True)
    school_nam = models.CharField(max_length=71, blank=True, null=True)
    block_name = models.CharField(max_length=17, blank=True, null=True)
    cluster_na = models.CharField(max_length=15, blank=True, null=True)
    village_na = models.CharField(max_length=24, blank=True, null=True)
    pincode = models.CharField(max_length=9, blank=True, null=True)
    unnamed_7 = models.IntegerField(db_column='unnamed:_7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nandurbar'


class Nashik(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=89, blank=True, null=True)
    block_name = models.CharField(max_length=12, blank=True, null=True)
    cluster_na = models.CharField(max_length=26, blank=True, null=True)
    village_na = models.CharField(max_length=26, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nashik'


class Osmanabad(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=9, blank=True, null=True)
    school_nam = models.CharField(max_length=99, blank=True, null=True)
    block_name = models.CharField(max_length=9, blank=True, null=True)
    cluster_na = models.CharField(max_length=13, blank=True, null=True)
    village_na = models.CharField(max_length=23, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'osmanabad'


class Parbhani(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=8, blank=True, null=True)
    school_nam = models.CharField(max_length=77, blank=True, null=True)
    block_name = models.CharField(max_length=12, blank=True, null=True)
    cluster_na = models.CharField(max_length=17, blank=True, null=True)
    village_na = models.CharField(max_length=23, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parbhani'


class Pune(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=4, blank=True, null=True)
    school_nam = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=9, blank=True, null=True)
    cluster_na = models.CharField(max_length=33, blank=True, null=True)
    village_na = models.CharField(max_length=27, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pune'


class Raigad(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=21, blank=True, null=True)
    school_nam = models.CharField(max_length=88, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=24, blank=True, null=True)
    village_na = models.CharField(max_length=31, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raigad'


class Ratnagiri(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=9, blank=True, null=True)
    school_nam = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=24, blank=True, null=True)
    village_na = models.CharField(max_length=28, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratnagiri'


class Sangli(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=95, blank=True, null=True)
    block_name = models.CharField(max_length=34, blank=True, null=True)
    cluster_na = models.CharField(max_length=25, blank=True, null=True)
    village_na = models.CharField(max_length=29, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    unnamed_7 = models.IntegerField(db_column='unnamed:_7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangli'


class Satara(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=81, blank=True, null=True)
    block_name = models.CharField(max_length=13, blank=True, null=True)
    cluster_na = models.CharField(max_length=18, blank=True, null=True)
    village_na = models.CharField(max_length=29, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satara'

class Sindhudurg(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.CharField(max_length=1, blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=10, blank=True, null=True)
    school_nam = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=23, blank=True, null=True)
    village_na = models.CharField(max_length=24, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sindhudurg'


class Solapur(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=7, blank=True, null=True)
    school_nam = models.CharField(max_length=99, blank=True, null=True)
    block_name = models.CharField(max_length=13, blank=True, null=True)
    cluster_na = models.CharField(max_length=25, blank=True, null=True)
    village_na = models.CharField(max_length=27, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solapur'


class Thane(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=5, blank=True, null=True)
    school_nam = models.CharField(max_length=71, blank=True, null=True)
    block_name = models.CharField(max_length=20, blank=True, null=True)
    cluster_na = models.CharField(max_length=21, blank=True, null=True)
    village_na = models.CharField(max_length=20, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thane'


class Wardha(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=74, blank=True, null=True)
    block_name = models.CharField(max_length=10, blank=True, null=True)
    cluster_na = models.CharField(max_length=15, blank=True, null=True)
    village_na = models.CharField(max_length=28, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wardha'


class Washim(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=6, blank=True, null=True)
    school_nam = models.CharField(max_length=71, blank=True, null=True)
    block_name = models.CharField(max_length=11, blank=True, null=True)
    cluster_na = models.CharField(max_length=18, blank=True, null=True)
    village_na = models.CharField(max_length=21, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'washim'


class Yavatmal(models.Model):
    geom = gis_models.PointField(blank=True, null=True)
    field1 = models.IntegerField(blank=True, null=True)
    unnamed_0 = models.IntegerField(db_column='unnamed:_0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    school_cod = models.BigIntegerField(blank=True, null=True)
    clrooms = models.IntegerField(blank=True, null=True)
    toiletb = models.IntegerField(blank=True, null=True)
    toilet_g = models.IntegerField(blank=True, null=True)
    mealsinsch = models.IntegerField(blank=True, null=True)
    electric_y = models.IntegerField(blank=True, null=True)
    library_yn = models.IntegerField(blank=True, null=True)
    pground_yn = models.IntegerField(blank=True, null=True)
    bookinlib = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    medchk_yn = models.IntegerField(blank=True, null=True)
    ramps_yn = models.IntegerField(blank=True, null=True)
    computer = models.IntegerField(blank=True, null=True)
    distname = models.CharField(max_length=8, blank=True, null=True)
    school_nam = models.CharField(max_length=62, blank=True, null=True)
    block_name = models.CharField(max_length=13, blank=True, null=True)
    cluster_na = models.CharField(max_length=18, blank=True, null=True)
    village_na = models.CharField(max_length=24, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yavatmal'
