# Generated by Django 4.2 on 2023-04-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]