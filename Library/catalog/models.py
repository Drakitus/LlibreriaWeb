from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 64,help_text = "Escribe un genero literario e.j: Aventuras")

    def __str__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=32,help_text="Escribe un idioma")

    def __str__(self):
        return self.language

class Author(models.Model):
    first_name = models.CharField(max_length=32)

    second_name = models.CharField(max_length=32)

    native_language = models.OneToOneField(Language,on_delete=models.SET_NULL,null=True,help_text="Selecciona el lenguage nativo de escritura del autor")

    def __str__(self):
        return '%s  %s' % (self.first_name,self.second_name)


class Book (models.Model):

    title = models.CharField( max_length= 128, help_text="Escribe el titulo del libro que desea guardar e.j: THE 100")

    author = models.ForeignKey(Author,on_delete=models.SET_DEFAULT,default=1)

    summary = models.TextField(max_length=500,help_text="Escribe un breve resumen del libro")

    isb = models.CharField('ISBN',max_length=13,help_text="Escribe un ISBN valido (13 caracteres)")

    genre = models.ManyToManyField(Genre,help_text="Selecciona un genero literario")

    language = models.ManyToManyField(Language,help_text="Selecciona los idiomas que esta escrito el libro")

    date_publicated = models.DateField(null=True,blank=True)

    def __str__(self):
        return '%s - %s' % (self.title,self.author)

    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])


