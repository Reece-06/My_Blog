# Generated by Django 5.0 on 2024-08-25 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_author_email_address_alter_author_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(upload_to='images'),
        ),
    ]