# Generated by Django 3.0.5 on 2020-07-18 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0010_auto_20200718_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text_question',
        ),
        migrations.AddField(
            model_name='text_to_question',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pytania.Question'),
            preserve_default=False,
        ),
    ]
