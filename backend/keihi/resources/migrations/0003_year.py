# Generated by Django 5.0.6 on 2024-06-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_remove_month_month_id_123636_idx_alter_month_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Year',
                'verbose_name_plural': 'Years',
                'db_table': 'year',
            },
        ),
    ]
