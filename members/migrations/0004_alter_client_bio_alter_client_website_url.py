# Generated by Django 4.2.4 on 2023-09-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bio',
            field=models.TextField(default='No bio'),
        ),
        migrations.AlterField(
            model_name='client',
            name='website_url',
            field=models.CharField(blank=True, default='https://', max_length=255, null=True),
        ),
    ]
