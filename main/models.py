from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Car(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
    grz = models.CharField(max_length=9, unique=True)
    is_our = models.BooleanField(default=True)

    def __str__(self):
        return self.grz


class Propusk(models.Model):
    NONE = 0
    ACTIVE = 1
    END = 2
    ANNUL = 3
    STATUS_TYPE = (
        (NONE, ''),
        (ACTIVE, 'Активен'),
        (END, 'Закончился'),
        (ANNUL, 'Аннулирован'),
    )
    NONE = 0
    BB = 1
    BA = 2
    SERIAL_TYPE = (
        (NONE, ''),
        (BB, 'ББ'),
        (BA, 'БА'),
    )
    serial_type = models.PositiveSmallIntegerField(choices=SERIAL_TYPE, default=0, blank=True, null=True)
    serial_num = models.CharField(max_length=8,blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_from = models.DateField(blank=True)
    date_to = models.DateField(blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, default=0, blank=True, null=True)
    days_to_end = models.CharField(max_length=250, blank=True)
    annul_date = models.DateField(blank=True)
    proverka_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
    is_our = models.BooleanField(default=False)

    def __str__(self):

        propusk = self.car.grz + ' ' + self.serial_type + ' ' + self.serial_num
        return propusk


class Profile(models.Model):
    NOTHING = 0
    SUPER = 1
    NO_LIMITS = 2
    PRODUCTION = 3
    PRODUCTION_WORKER = 4
    CLIENT_WORKER = 5
    SALE_WORKER = 6
    PERMISSIONS_TYPE = (
        (NOTHING, 'Не определен'),
        (SUPER, 'Создатель'),
        (NO_LIMITS, 'Без ограничений'),
        (PRODUCTION, 'Всё производство'),
        (PRODUCTION_WORKER, 'Производство'),
        (CLIENT_WORKER, 'Работа с Клиентами'),
        (SALE_WORKER, 'Отдел продаж')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission_type = models.PositiveSmallIntegerField(choices=PERMISSIONS_TYPE, default=0)
    birthday = models.DateField(blank=True)
    activity = models.IntegerField(default=0, blank=True)
    cars_in_work = models.IntegerField(default=0, blank=True)
    salary = models.IntegerField(blank=True)

    def __str__(self):
        return self.user


    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


# class Client(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     name = models.CharField(max_length=100)
#     name2 = models.CharField(max_length=200, blank=True)
#     email = models.EmailField(max_length=100, blank=True)
#     email2 = models.EmailField(max_length=100, blank=True)
#     tel = models.CharField(max_length=100, blank=True)
#     tel2 = models.CharField(max_length=100, blank=True)
#     tel3 = models.CharField(max_length=100, blank=True)
#     NONE = 0
#     OUR = 1
#     POTENTIAL = 2
#     WAS_OUR = 3
#     STATUS_TYPE = (
#         (NONE, 'не наш'),
#         (OUR, 'наш'),
#         (POTENTIAL, 'Потенциальный'),
#         (WAS_OUR, 'был наш'),
#     )
#     status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, default=0, blank=True)
#     comment = models.TextField()
#
#     def __str__(self):
#         return self.name
#
# class YearRequest(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     date_request = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     number = models.CharField(max_length=6)
#
#     def __str__(self):
#         return self.number
#
# class TempRequest(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     date_request = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     number = models.CharField(max_length=6)
#
#     def __str__(self):
#         return self.number
#
# class EmailRecive(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     NONE = 0
#     MKAD = 1
#     MOSCOW = 2
#     PGRUZOVOY = 3
#     RABOTAOGON = 4
#     EMAIL_TYPE = (
#         (NONE, ''),
#         (MKAD, 'мкадпропуск'),
#         (MOSCOW, 'москоупропуск'),
#         (PGRUZOVOY, 'пгрузовой'),
#         (RABOTAOGON, 'работаогонь')
#     )
#     recive_to = models.PositiveSmallIntegerField(choices=EMAIL_TYPE, default=0)
#
#     def __str__(self):
#         return self.recive_to
#
# class Prod_Card_Comment(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     text = models.TextField()
#     is_client_know = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.text
#
# class NeedToDo(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     text = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.text
#
#
# class Firma(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     name = models.CharField(max_length=100)
#     INN = models.CharField(max_length=20, blank=True)
#     director = models.CharField(max_length=100, blank=True)
#
#
#
# class ProdCard(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     NONE = 0
#     NEW = 1
#     WAIT = 2
#     LETS_START =3
#     INWORK = 4
#     READY = 5
#     OUT = 6
#     ANNUL = 7
#     STATUS_TYPE = (
#         (NONE, ''),
#         (NEW, 'новая'),
#         (WAIT, 'ожидание'),
#         (LETS_START, 'на подачу'),
#         (INWORK, 'в работе'),
#         (READY, 'готово'),
#         (OUT, 'отказ'),
#         (ANNUL, 'аннулирован'),
#     )
#     DK_NOT_US = 0
#     DK_OUR = 1
#     DK = (
#         (DK_NOT_US, ''),
#         (DK_OUR, 'ДК')
#     )
#     NONE = 0
#     MKAD6 = 1
#     MKAD12 = 2
#     TTK6 = 3
#     TTK12 = 4
#     SK6 = 5
#     SK12 = 6
#     TEMP = 7
#     TYPES = (
#         (NONE, ''),
#         (MKAD6, 'МКАД6'),
#         (MKAD12, 'МКАД12'),
#         (TTK6, 'ТТК6'),
#         (TTK12, 'ТТК12'),
#         (SK6, 'СК6'),
#         (SK12, 'СК12'),
#         (TEMP, 'Временный'),
#     )
#     create_date = models.DateField(default=datetime.date.today().strftime("%Y-%m-%d"))
#     car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
#     propusk_id = models.ForeignKey(Propusk, on_delete=models.DO_NOTHING, blank=True)
#     profile_id = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True)
#     propusk_type = models.PositiveSmallIntegerField(choices=TYPES, default=0)
#     status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, default=0)
#     dk = models.PositiveSmallIntegerField(choices=DK, default=0, blank=True)
#     year_request_id = models.ForeignKey(YearRequest, on_delete=models.DO_NOTHING, blank=True)
#     temp_request_id = models.ForeignKey(TempRequest, on_delete=models.DO_NOTHING, blank=True)
#     email_recive_id = models.ForeignKey(EmailRecive, on_delete=models.DO_NOTHING, blank=True)
#     comment_id = models.ForeignKey(Prod_Card_Comment, on_delete=models.DO_NOTHING, blank=True)
#     need_to_do_id = models.ForeignKey(NeedToDo, on_delete=models.DO_NOTHING, blank=True)
#
#     def __str__(self):
#         result = self.car_id + ' ' + self.status
#         return result
#
#
# class Settings(models.Model):
#     DARK = 0
#     LIGHT = 1
#     THEME_TYPE = (
#         (LIGHT, 'Светлая тема'),
#         (DARK, 'Темная тема')
#     )
#     theme = models.PositiveSmallIntegerField(choices=THEME_TYPE, default=0, blank=True)
#     user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     info_text = models.CharField(max_length=100, blank=True)

# class Image(models.Model):
#     image = models.ImageField(upload_to='media', blank=True)
#     url = models.URLField()
#     def __str__(self):
#         return self.url