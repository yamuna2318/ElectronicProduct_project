from django.db import models

class commondata(models.Model):
    name = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    header_img = models.ImageField(null=True, blank=True, upload_to="images/")
    processor = models.TextField(blank=True, null=True)
    RAM = models.TextField(blank=True, null=True)
def __str__(self):
    return  self.name

class mobilesdata(commondata):
    screensize = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
def __str__(self):
    return self.screensize

class laptopsdata(commondata):
    HD_capacity=models.TextField(blank=True,null=True)
def __str__(self):
    return self.HD_capacity