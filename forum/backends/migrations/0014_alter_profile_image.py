# Generated by Django 4.1 on 2022-10-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0013_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/media/profile_picture/defolt_user1.png', upload_to='profile_picture'),
        ),
    ]
