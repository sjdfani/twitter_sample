# Generated by Django 3.2 on 2023-02-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='cover/', verbose_name='Cover photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Profile photo'),
        ),
    ]
