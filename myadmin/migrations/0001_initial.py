# Generated by Django 3.2.4 on 2021-07-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('catnm', models.CharField(max_length=100)),
                ('caticonnm', models.CharField(max_length=100)),
            ],
        ),
    ]
