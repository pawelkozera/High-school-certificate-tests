# Generated by Django 3.0.5 on 2020-07-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0020_auto_20200719_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('zamkniete', 'zamkniete'), ('otwarte', 'otwarte')], default='', max_length=50),
            preserve_default=False,
        ),
    ]
