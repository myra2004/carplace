from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MediaFile(BaseModel):
    file = models.FileField(upload_to='files')
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='media_files', null=True, blank=True)

    def __str__(self):
        return self.file.name


class ContactMessage(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.name}'s contact message"