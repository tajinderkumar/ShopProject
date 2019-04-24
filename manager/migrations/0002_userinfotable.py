# Generated by Django 2.0.6 on 2019-04-03 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfoTable',
            fields=[
                ('tbuseremail', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('tbusername', models.CharField(max_length=255)),
                ('tbuserpassword', models.CharField(max_length=255)),
                ('tbusermob', models.BigIntegerField()),
                ('tbuseraltmob', models.CharField(max_length=255)),
                ('tbuserimage', models.CharField(max_length=255)),
                ('tbuserpan', models.CharField(default='buyer', max_length=255)),
                ('tbuserpanimage', models.CharField(max_length=255, null=True)),
                ('tbuseradhar', models.CharField(default='adhar', max_length=255)),
                ('tbuseradharimage', models.CharField(max_length=255, null=True)),
                ('tbisactive', models.BooleanField(default=True)),
                ('tbuseraddress', models.CharField(max_length=255)),
                ('tbuserpincode', models.IntegerField()),
                ('tbuserroleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.roletable')),
            ],
        ),
    ]