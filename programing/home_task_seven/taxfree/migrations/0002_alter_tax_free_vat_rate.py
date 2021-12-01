# Generated by Django 3.2.9 on 2021-11-29 21:06

from django.db import migrations, models
import taxfree.validation


class Migration(migrations.Migration):

    dependencies = [
        ('taxfree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax_free',
            name='vat_rate',
            field=models.IntegerField(db_index=True, max_length=40, validators=[taxfree.validation.Validation.check_vat_rate], verbose_name='vat_rate'),
        ),
    ]
