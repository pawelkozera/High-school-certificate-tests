# Generated by Django 3.0.5 on 2020-07-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytania', '0024_auto_20200727_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=200)),
                ('exam_year', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
