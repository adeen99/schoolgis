# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AccountsRegister(models.Model):

    class Meta:
        managed = False
        db_table = 'accounts_register'


class Ahmadnagar(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahmadnagar'


class Akola(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'akola'


class Amravati(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aurangabad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Beed(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beed'


class Bhandara(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bhandara'


class Buldhana(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buldhana'


class Chandrapur(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chandrapur'


class Dhule(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dhule'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gadchiroli(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gadchiroli'


class Hingoli(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hingoli'


class Jalgaon(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jalgaon'


class Jalna(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jalna'


class Kolhapur(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kolhapur'


class Latur(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'latur'


class MaharashtraAdministrative(models.Model):
    geom = models.MultiLineStringField(srid=0, blank=True, null=True)
    name = models.CharField(max_length=38, blank=True, null=True)
    admin_leve = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maharashtra_administrative'


class MainMap(models.Model):

    class Meta:
        managed = False
        db_table = 'main_map'


class Mumbaifull(models.Model):
    geom = models.PointField(blank=True, null=True)
    school_cod = models.BigIntegerField(blank=True, null=True)
    distname = models.CharField(max_length=17, blank=True, null=True)
    school_nam = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mumbaifull'


class Nagpur(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagpur'


class Nanded(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nanded'


class Nandurbar(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nashik'


class Osmanabad(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'osmanabad'


class Parbhani(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parbhani'


class Pune(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pune'


class Raigad(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raigad'


class Ratnagiri(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratnagiri'


class Sangli(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satara'


class School(models.Model):
    geom = models.PointField(blank=True, null=True)
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


class Sindhudurg(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sindhudurg'


class Solapur(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solapur'


class Thane(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thane'


class Wardha(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wardha'


class Washim(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'washim'


class Yavatmal(models.Model):
    geom = models.PointField(blank=True, null=True)
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
    unnamed_7 = models.CharField(db_column='unnamed:_7', max_length=-1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yavatmal'
