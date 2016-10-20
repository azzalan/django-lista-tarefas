from django.db import models


class Tarefa(models.Model):
    criado = models.DateTimeField(auto_now_add=True, auto_now=False)
    atualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
    nome = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def mudar_status(self):
        self.status = not self.status
        self.save()