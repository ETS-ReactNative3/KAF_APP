# Generated by Django 3.1.3 on 2021-02-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_auto_20210208_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='friend_refferal',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]