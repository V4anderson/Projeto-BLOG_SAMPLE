from django.db import models
from django.contrib.auth import get_user_model

class SamplePostBlog(models.Model):
    title = models.CharField("",max_length=50)
    data = models.DateField("Data",auto_now_add=True)
    hora = models.TimeField("Hora",auto_now_add=True)
    descricao = models.TextField("")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class DestaquePostBlog(models.Model):
    title = models.CharField("",max_length=50)
    data = models.DateField("Data",auto_now_add=True)
    hora = models.TimeField("Hora",auto_now_add=True)
    descricao = models.TextField("")
    imagem = models.TextField("",blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
