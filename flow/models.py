from django.db import models

class Mahasiswa(models.Model):
  nama = models.CharField(max_length=100)
  kelas = models.TextField()

  def __str__(self):
    return f"{self.nama}"
  
class Dosen(models.Model):
  nama = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.nama}"
  