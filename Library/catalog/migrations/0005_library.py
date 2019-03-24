# Generated by Django 2.1.7 on 2019-03-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Inserte la direccion', max_length=64)),
                ('postal_code', models.CharField(help_text='Inserte el codigo postal', max_length=5)),
                ('lat', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
            ],
        ),
    ]
