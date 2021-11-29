# Generated by Django 3.2.9 on 2021-11-29 20:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taxfree.validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax_free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(db_index=True, max_length=64, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters.')], verbose_name='company')),
                ('vat_rate', models.IntegerField(db_index=True, max_length=40, verbose_name='vat_rate')),
                ('date_of_purchase', models.DateTimeField(db_index=True, max_length=10, verbose_name='date_of_purchase')),
                ('vat_code', models.CharField(db_index=True, max_length=13, validators=[taxfree.validation.Validation.check_vat_code], verbose_name='vat_code')),
                ('date_of_tax_ref', models.DateTimeField(db_index=True, max_length=10, verbose_name='date_of_tax_ref')),
                ('country', models.IntegerField(choices=[(1, 'Germany'), (2, 'Italy'), (3, 'France')], verbose_name='country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
