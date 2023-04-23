# Generated by Django 4.0.3 on 2022-06-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0020_alter_add_farmer_table_adhar'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_vendor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('vid', models.CharField(max_length=6)),
                ('location', models.CharField(max_length=50)),
                ('adhar', models.CharField(max_length=12)),
                ('logger_id', models.IntegerField()),
            ],
        ),
    ]
