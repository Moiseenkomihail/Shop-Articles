# Generated by Django 4.2.6 on 2023-10-22 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
