# Generated by Django 3.2.4 on 2021-07-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcatid', models.AutoField(primary_key=True, serialize=False)),
                ('catid', models.IntegerField()),
                ('subcatnm', models.CharField(max_length=100)),
                ('subcaticonnm', models.CharField(max_length=100)),
            ],
        ),
    ]
