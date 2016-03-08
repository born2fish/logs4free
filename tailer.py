# -*- coding: utf-8 -*-
import sys
import time
import os
from datetime import datetime
from apache_an.models import ApacheLogLine
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "log4free.settings")

HTTP_METHODS = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']
SECONDS_INTERVAL = 0.5


def tail(filename):
    time.sleep(SECONDS_INTERVAL)
    with open(filename, 'r') as o:
        try:
            return o.readlines()[-1]
        except:
            return "no data in log " + filename


def count_overlapping_substrings(haystack, needle):
    count = 0
    i = -1
    while True:
        i = haystack.find(needle, i + 1)
        if i == -1:
            return count
        count += 1


class LogLiner:

    def __init__(self):
        pass

    from_ip = None
    date_time = None
    req_type = None
    req_uri = None
    req_proto = None
    req_status = None
    from_url = None
    user_agent = ""

    @staticmethod
    def clean(value):
        return str(value).replace("\"", "").replace("[", "")

    @staticmethod
    def save_ll(from_ip, date_time, req_type, req_uri, req_proto, req_status, from_url, user_agent):
        line = ApacheLogLine(from_ip=from_ip, date_time=date_time, req_type=req_type,
                             req_uri=req_uri, req_protocol=req_proto, req_status=req_status, from_url=from_url,
                             user_agent=user_agent)
        try:
            last_line = ApacheLogLine.objects.all().order_by('-id')[0]
        except Exception as line_add_ex:
            print line_add_ex
            last_line = None
            pass

        try:
            if last_line is None:
                line.save()
            else:
                if last_line.date_time != date_time:
                    line.save()
                    print "[INFO]: log line saved"
        except Exception as a:
            print a
            pass

    def parse_and_save_ll(self, line_of_log):
        log_lines = line_of_log.split(" ")
        self.user_agent = ""
        for idx, l in enumerate(log_lines):
            # print l, idx
            # ip
            if count_overlapping_substrings(l, ".") == 3:
                try:
                    int(l.replace('.', ''))
                    self.from_ip = l
                except Exception as e:
                    pass
            # date
            if count_overlapping_substrings(l, ":") == 3:
                if count_overlapping_substrings(l, "/") == 2:
                    self.date_time = datetime.strptime(self.clean(l).lower(), '%d/%b/%Y:%H:%M:%S')
                    self.date_time = timezone.make_aware(self.date_time, timezone.get_current_timezone())
            # req type
            if self.clean(l) in HTTP_METHODS:
                self.req_type = self.clean(l)
            # uri
            if idx == 6:
                self.req_uri = l
            # proto
            if idx == 7:
                self.req_proto = self.clean(l)
            # status
            if idx == 8:
                try:
                    self.req_status = int(l)
                except:
                    pass
            # from url
            if idx == 10:
                self.from_url = self.clean(l)
                if "http://" in self.from_url:
                    pass
                else:
                    self.from_url = "/"
            if 11 <= idx <= 18:
                self.user_agent = self.user_agent + " " + l
                self.user_agent = self.clean(self.user_agent)
        if self.from_ip is not None and self.req_status is not None:
            self.save_ll(self.from_ip, self.date_time, self.req_type, self.req_uri,
                         self.req_proto, self.req_status, self.from_url, self.user_agent)

try:
    path = sys.argv[1]
    logLiner = LogLiner()
    while True:
        log_line = tail(path)
        # save_log_line(log_line)
        logLiner.parse_and_save_ll(log_line)
except IndexError as ie:
    print "[ERROR]: Missed file log path;"
