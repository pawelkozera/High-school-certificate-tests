# Generated by Django 3.0.5 on 2020-07-27 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0026_auto_20200727_1556'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exams_Info',
            new_name='ExamsInfo',
        ),
        migrations.RenameModel(
            old_name='Text_To_Question',
            new_name='TextToQuestion',
        ),
    ]
