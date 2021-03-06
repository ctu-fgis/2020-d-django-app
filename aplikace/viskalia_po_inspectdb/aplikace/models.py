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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    action_flag = models.PositiveSmallIntegerField()
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


class Zaklad(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu')  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek')  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ')  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni')  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor')  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor')  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace')  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru')  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50)  # Field name made lowercase.
    datum_zprac = models.DateField(db_column='Datum_zprac')  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek')  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka')  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument')  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zaklad'
