# Generated by Django 3.0.5 on 2020-07-27 13:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0025_exams_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='exams_info',
            name='length_of_test',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='question',
            name='exam_date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pytania.Exams_Info'),
        ),
    ]
