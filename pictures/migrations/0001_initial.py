# Generated by Django 4.0.4 on 2022-05-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[(1, 'Night'), (2, 'Landscape'), (3, 'Urban'), (4, 'Architecture'), (5, 'Portrait'), (6, 'Other')], default=6, max_length=2)),
                ('location', models.CharField(max_length=10)),
                ('picture_url', models.CharField(max_length=300)),
                ('camera', models.CharField(max_length=30)),
                ('settings', models.CharField(max_length=50)),
            ],
        ),
    ]
