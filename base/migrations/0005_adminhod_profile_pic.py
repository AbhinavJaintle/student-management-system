# Generated by Django 4.0.5 on 2022-07-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminhod',
            name='profile_pic',
            field=models.ImageField(default='avatar.svg', upload_to='media/profiles'),
        ),
    ]
