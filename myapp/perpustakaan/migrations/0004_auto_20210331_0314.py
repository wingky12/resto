# Generated by Django 3.1.7 on 2021-03-31 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_auto_20210325_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover'),
        ),
        migrations.AddField(
            model_name='buku',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
