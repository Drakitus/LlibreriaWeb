# Generated by Django 2.1.7 on 2019-05-11 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='native_language',
            field=models.ForeignKey(help_text='Choose a language', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Choose the genre', to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='Write ISBN, 13 Characters', max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Choose the language', to='catalog.Language'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Write a brief summary of the book', max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Write the title of the book', max_length=128),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Mantenimiento'), ('p', 'Prestado'), ('d', 'Disponible'), ('r', 'Reservado')], default='m', help_text='Disponibility of the book', max_length=1),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text="Write a genre for example 'Adventures'", max_length=64),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(help_text='Introduce Language', max_length=32),
        ),
        migrations.AlterField(
            model_name='library',
            name='address',
            field=models.CharField(help_text='Put the direction', max_length=64),
        ),
        migrations.AlterField(
            model_name='library',
            name='postal_code',
            field=models.CharField(help_text='Put the postal code', max_length=5),
        ),
    ]
