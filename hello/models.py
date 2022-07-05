from distutils.command.upload import upload
from multiprocessing.reduction import register
from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    register_date = models.DateTimeField(help_text='登録日')
    icon_image = models.ImageField(upload_to='')
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'