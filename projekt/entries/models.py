# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    first_name = models.CharField(max_length=30)
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


class Dkraje(models.Model):
    dch1 = models.BigIntegerField()
    dch2 = models.BigIntegerField()
    dch3 = models.BigIntegerField()
    dch4 = models.BigIntegerField()
    dch5 = models.BigIntegerField()
    dch6 = models.BigIntegerField()
    dch7 = models.BigIntegerField()
    dch8 = models.BigIntegerField()
    dch9 = models.BigIntegerField()
    dch10 = models.BigIntegerField()
    dch11 = models.BigIntegerField()
    dch12 = models.BigIntegerField()
    dch13 = models.BigIntegerField()
    dch14 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dkraje'


class Iautorsky(models.Model):
    jmeno = models.TextField()
    vyzkum = models.BooleanField()
    teren = models.BooleanField()
    technicky = models.BooleanField()
    kreslil = models.BooleanField()
    fotografoval = models.BooleanField()
    cislo_nove = models.TextField()

    class Meta:
        managed = False
        db_table = 'iautorsky'


class Iautorsky2(models.Model):
    jmeno = models.TextField()
    kraj = models.TextField()
    okres = models.TextField()
    lokalita = models.TextField()
    cp = models.TextField()

    class Meta:
        managed = False
        db_table = 'iautorsky2'


class Ijmeno(models.Model):
    jmeno = models.TextField()

    class Meta:
        managed = False
        db_table = 'ijmeno'


class Ikraj(models.Model):
    kraj = models.TextField()

    class Meta:
        managed = False
        db_table = 'ikraj'


class Ilokalita(models.Model):
    lokalita = models.TextField()

    class Meta:
        managed = False
        db_table = 'ilokalita'


class Imistni(models.Model):
    lok = models.TextField()
    kraj = models.TextField()
    okres = models.TextField()
    lokalita = models.TextField()
    cp = models.TextField()
    cislo_nove = models.TextField()
    cislo_stare = models.TextField()

    class Meta:
        managed = False
        db_table = 'imistni'


class Iokres(models.Model):
    okres = models.TextField()

    class Meta:
        managed = False
        db_table = 'iokres'


class Itrid1(models.Model):
    popis1 = models.TextField()

    class Meta:
        managed = False
        db_table = 'itrid1'


class Itrid2(models.Model):
    popis2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'itrid2'


class Itrid3(models.Model):
    popis3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'itrid3'


class Itrid4(models.Model):
    popis4 = models.TextField()

    class Meta:
        managed = False
        db_table = 'itrid4'


class Itrid5(models.Model):
    popis5 = models.TextField()

    class Meta:
        managed = False
        db_table = 'itrid5'


class NsfoxkamPlan(models.Model):
    inv_cis_stare = models.TextField()
    inv_cis_nove = models.TextField()
    lokalita = models.TextField()
    cp = models.TextField()
    kraj = models.TextField()
    okres = models.TextField()
    tridici1kat = models.TextField()
    tridici2kat = models.TextField()
    tridici3kat = models.TextField()
    tridici4kat = models.TextField()
    tridici5kat = models.TextField()
    zamereni = models.TextField()
    vyzkum = models.TextField()
    teren = models.TextField()
    technicky = models.TextField()
    kreslil = models.TextField()
    fotografoval = models.TextField()
    rozsah = models.TextField()
    soubor = models.TextField()
    gps = models.TextField()

    class Meta:
        managed = False
        db_table = 'nsfoxkam_plan'


class Table16(models.Model):
    col_1 = models.CharField(db_column='COL 1', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_2 = models.IntegerField(db_column='COL 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_3 = models.CharField(db_column='COL 3', max_length=26, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_4 = models.CharField(db_column='COL 4', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_5 = models.CharField(db_column='COL 5', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_6 = models.CharField(db_column='COL 6', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_7 = models.CharField(db_column='COL 7', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_8 = models.CharField(db_column='COL 8', max_length=27, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_9 = models.CharField(db_column='COL 9', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_10 = models.CharField(db_column='COL 10', max_length=13, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_11 = models.CharField(db_column='COL 11', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_12 = models.CharField(db_column='COL 12', max_length=54, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_13 = models.CharField(db_column='COL 13', max_length=23, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_14 = models.CharField(db_column='COL 14', max_length=23, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_15 = models.CharField(db_column='COL 15', max_length=23, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_16 = models.CharField(db_column='COL 16', max_length=23, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_17 = models.CharField(db_column='COL 17', max_length=23, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_18 = models.CharField(db_column='COL 18', max_length=91, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_19 = models.CharField(db_column='COL 19', max_length=17, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_20 = models.CharField(db_column='COL 20', max_length=29, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'table 16'


class Zzz(models.Model):
    zb = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'zzz'
