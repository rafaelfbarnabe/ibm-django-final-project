# Generated by Django 3.1.3 on 2022-07-18 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='choices',
            field=models.ManyToManyField(to='onlinecourse.Choice'),
        ),
    ]
