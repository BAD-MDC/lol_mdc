from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()             # content 컬럼
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Champion_stats(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    hp=models.IntegerField()
    hp_perlevel=models.IntegerField()
    mp=models.IntegerField()
    mp_perlevel=models.IntegerField()
    armor=models.IntegerField()
    armor_perlevel=models.IntegerField()
    spellblock=models.IntegerField()
    spellblock_perlevel=models.IntegerField()
    hpregen=models.IntegerField()
    hpregen_perlevel=models.IntegerField()
    mpregen=models.IntegerField()
    mpregen_perlevel=models.IntegerField()
    crit=models.IntegerField()
    crit_perlevel=models.IntegerField()
    attackdamage=models.IntegerField()
    attackdamage_perlevel=models.IntegerField()
    attackspeed=models.IntegerField()
    attackspeed_perlevel=models.IntegerField()