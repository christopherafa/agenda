from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    local_evento = models.TextField(blank = True, null = True)
    data_criacao = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #Renomeadno a tabela
    class Meta:
        db_table = 'evento'
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        data_evento = str(self.data_evento.strftime('%d/%m/%Y %H:%M'))
        if self.local_evento != None:
            local_evento = self.local_evento
        else:
            local_evento = "Sem local definido"
        return  data_evento + " - Local: " + local_evento

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
