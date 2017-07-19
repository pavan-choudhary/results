from django.db import models

class batch(models.Model):
	batchy =models.CharField(max_length=20)

	def __str__(self):
		return self.batchy

class semester(models.Model):
	batchyear =models.ForeignKey(batch,on_delete=models.CASCADE,related_name='batchyear')
	sem=models.CharField(max_length=20)

	def __str__(self):
		return  "Sem "+self.sem +"("+ self.batchyear.batchy +")"