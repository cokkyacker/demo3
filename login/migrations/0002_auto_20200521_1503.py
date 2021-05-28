# Generated by Django 3.0.5 on 2020-05-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64)),
                ('email', models.EmailField(default='', max_length=254)),
                ('birthday', models.DateField()),
                ('thumb', models.CharField(default='', max_length=128)),
                ('gender', models.IntegerField(default=1)),
                ('hobby', models.CharField(max_length=128)),
                ('pos', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='userinfo',
            field=models.CharField(default='', max_length=100),
        ),
    ]