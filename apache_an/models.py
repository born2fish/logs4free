from django.db import models


class ApacheLogLine(models.Model):
    from_ip = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    req_type = models.CharField(max_length=7)
    req_uri = models.CharField(max_length=2000)
    req_protocol = models.CharField(max_length=10)
    req_status = models.IntegerField(default=None)
    from_url = models.CharField(max_length=500)
    user_agent = models.CharField(max_length=2000)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.date_time) + " / " + str(self.from_ip) + " | " + str(self.req_status)

    def __unicode__(self):
        return str(self.date_time) + " / " + str(self.from_ip) + " | " + str(self.req_status)
