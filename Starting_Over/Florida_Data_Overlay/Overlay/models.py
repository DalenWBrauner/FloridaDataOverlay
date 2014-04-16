from django.db import models

class Births(models.Model):
    year = models.IntegerField("Year")
    county = models.CharField("County",max_length=20)
    mothersAge = models.IntegerField("Mother's Age")
    mothersEdu = models.CharField("Mother's Education",max_length=50)
    source = models.URLField("Source")
    isRepeat = models.BooleanField("Is a Repeat Birth")
    births = models.IntegerField("Births")

    def __unicode__(self):
        s = "In " + self.county + " county, " + str(self.year)
        s += ", there were " + str(self.births)
        if self.isRepeat:   s += " repeat births to "
        else:               s += " first births to "
        s += str(self.mothersAge) + "-year-old mothers who "
        s += self.mothersEdu + ", according to " + self.source
        return s
