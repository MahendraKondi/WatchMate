# Generated by Django 5.0.7 on 2024-08-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streamplatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=200)),
                ('website', models.URLField(max_length=50)),
            ],
        ),
    ]
