# Generated by Django 3.0.5 on 2020-06-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0007_auto_20200628_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, upload_to='exam_image'),
        ),
    ]
