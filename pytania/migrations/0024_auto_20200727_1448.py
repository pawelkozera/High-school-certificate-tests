# Generated by Django 3.0.5 on 2020-07-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0023_auto_20200727_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]
