from django.db import models

# Create your models here.


class ANNResult(models.Model):
    si = models.PositiveSmallIntegerField()
    ta = models.PositiveSmallIntegerField()
    br = models.PositiveSmallIntegerField()
    lv = models.PositiveSmallIntegerField()
    qr = models.PositiveSmallIntegerField()
    lt = models.PositiveSmallIntegerField()
    st = models.PositiveSmallIntegerField()
    be = models.PositiveSmallIntegerField()
    tx = models.PositiveSmallIntegerField()
    ec = models.PositiveSmallIntegerField()

    def __str__(self):
        return "DATA ke - {}".format(self.id)


class CNNResult(models.Model):
    af = models.PositiveSmallIntegerField()
    hr = models.FloatField()
    hc = models.PositiveSmallIntegerField()
    re = models.PositiveSmallIntegerField()
    qp = models.PositiveSmallIntegerField()
    ql = models.PositiveSmallIntegerField()
    ss = models.PositiveSmallIntegerField()
    sc = models.PositiveSmallIntegerField()
    si = models.PositiveSmallIntegerField()
    sn = models.PositiveSmallIntegerField()
    sl = models.PositiveSmallIntegerField()
    qi = models.FloatField()
    qc = models.FloatField()
    tw = models.PositiveSmallIntegerField()
    tl = models.PositiveSmallIntegerField()
    td = models.FloatField()
    vs = models.PositiveSmallIntegerField()
    ae = models.PositiveSmallIntegerField()
    js = models.PositiveSmallIntegerField()
    uw = models.PositiveSmallIntegerField()

    def __str__(self):
        return "DATA ke - {}".format(self.id)
