# Generated by Django 3.1.2 on 2020-10-20 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(default='2020-10-20')),
                ('grz', models.CharField(max_length=9, unique=True)),
                ('is_our', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Propusk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, ''), (1, 'ББ'), (2, 'БА')], default=0, null=True)),
                ('serial_num', models.CharField(blank=True, max_length=8, null=True)),
                ('date_from', models.DateField(blank=True)),
                ('date_to', models.DateField(blank=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, ''), (1, 'Активен'), (2, 'Закончился'), (3, 'Аннулирован')], default=0, null=True)),
                ('days_to_end', models.CharField(blank=True, max_length=250)),
                ('annul_date', models.DateField(blank=True)),
                ('proverka_date', models.DateField(default='2020-10-20')),
                ('is_our', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_type', models.PositiveSmallIntegerField(choices=[(0, 'Не определен'), (1, 'Создатель'), (2, 'Без ограничений'), (3, 'Всё производство'), (4, 'Производство'), (5, 'Работа с Клиентами'), (6, 'Отдел продаж')], default=0)),
                ('birthday', models.DateField(blank=True)),
                ('activity', models.IntegerField(blank=True, default=0)),
                ('cars_in_work', models.IntegerField(blank=True, default=0)),
                ('salary', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
