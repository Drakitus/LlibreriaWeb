# Generated by Django 2.1.7 on 2019-03-24 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('second_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Escribe el titulo del libro que desea guardar e.j: THE 100', max_length=128)),
                ('summary', models.TextField(help_text='Escribe un breve resumen del libro', max_length=500)),
                ('isb', models.CharField(help_text='Escribe un ISBN valido (13 caracteres)', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Escribe un genero literario e.j: Aventuras', max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Selecciona un genero literario', to='catalog.Genre'),
        ),
    ]
