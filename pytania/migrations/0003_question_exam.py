# Generated by Django 3.0.5 on 2020-06-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0002_question_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.CharField(default='matura', max_length=10),
            preserve_default=False,
        ),
    ]