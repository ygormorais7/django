from django.db import models

# Create your models here.
# CLASSES QUE REPRESENTAM TABELAS NO BANCO DE DADOS

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.question_text
    
    # Facilita para filtrar questoes criada a menos de 1 dia
    def publicado_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text