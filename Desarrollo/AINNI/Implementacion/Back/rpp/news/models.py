from django.db import models


# Create your models here.
class New(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300, verbose_name='Título')
    sub_title = models.CharField(max_length=600, verbose_name='Copete')
    body = models.TextField(verbose_name='Cuerpo')
    image = models.ImageField(upload_to='news/image', null=True, blank=True)
    is_enabled = models.BooleanField(default=True, verbose_name='Habilitado')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
