# Generated by Django 3.1.3 on 2021-02-08 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20210208_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='adus_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.consumer'),
        ),
    ]
