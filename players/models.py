from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class Player(models.Model):
    first_name = models.TextField(max_length=1000)
    last_name = models.TextField(max_length=1000)
    gender =  models.CharField(max_length=100)
    dob = models.CharField(max_length=254)
    sport = models.ForeignKey(Sport,related_name="playersport",on_delete=models.PROTECT)
    country = models.ForeignKey(Country,related_name="playercountry",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Tours(models.Model):
    name = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tournament_Season(models.Model):
    snid = models.ForeignKey(Season,related_name="seasonid",on_delete=models.PROTECT)
    tsname = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tsname

class Tournament(models.Model):
    trnid = models.AutoField(primary_key=True)
    trnname = models.TextField(max_length=1000)
    bwftrnid = models.TextField(max_length=1000)
    sptid = models.ForeignKey(Sport,related_name="sport",on_delete=models.PROTECT)
    cntid = models.ForeignKey(Country,related_name="country",on_delete=models.PROTECT)
    turid = models.ForeignKey(Tours,related_name="comptype",on_delete=models.PROTECT)
    snid = models.ForeignKey(Season,related_name="compseason",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.trnname
