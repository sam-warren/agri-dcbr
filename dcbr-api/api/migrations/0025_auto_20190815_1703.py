# Generated by Django 2.2 on 2019-08-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20190815_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_factor_operation',
            name='perm_id_other',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
