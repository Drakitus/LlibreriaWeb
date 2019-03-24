# Generated by Django 2.1.7 on 2019-03-24 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_date_publicated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(help_text='Escribe un idioma', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='native_language',
            field=models.OneToOneField(help_text='Selecciona el lenguage nativo de escritura del autor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Selecciona los idiomas que esta escrito el libro', to='catalog.Language'),
        ),
    ]