# Generated by Django 3.1 on 2020-09-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200927_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(related_name='blogs', to='blog.Tag', verbose_name='タグ'),
        ),
    ]
