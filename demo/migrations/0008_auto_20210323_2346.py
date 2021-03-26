# Generated by Django 3.1.7 on 2021-03-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ccsFormData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40)),
                ('surname', models.CharField(blank=True, max_length=40)),
                ('email', models.CharField(blank=True, max_length=40)),
                ('phone', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='number',
        ),
        migrations.RemoveField(
            model_name='character',
            name='book',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookNumber',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
    ]