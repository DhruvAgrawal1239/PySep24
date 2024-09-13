# Generated by Django 5.1.1 on 2024-09-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('disease', models.CharField(max_length=125)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
