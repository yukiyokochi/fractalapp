# Generated by Django 3.1 on 2020-09-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_blog_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='タグ')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='タグ'),
        ),
    ]
