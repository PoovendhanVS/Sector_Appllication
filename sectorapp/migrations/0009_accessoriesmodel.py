# Generated by Django 4.2.2 on 2023-07-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectorapp', '0008_country_state_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoriesModel',
            fields=[
                ('Acc_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Acc_Name', models.CharField(max_length=100)),
                ('Item_Id', models.IntegerField()),
            ],
        ),
    ]
