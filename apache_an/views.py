from django.views import generic
from models import ApacheLogLine
from log4free.paging_support import paginate
from django.core import serializers


# Create your views here.
class ApacheLogsPage(generic.ListView):
    model = ApacheLogLine
    template_name = "apache_an/index.html"
    context_object_name = "meta"

    def get_context_data(self, **kwargs):
        request = self.request
        all_logs = ApacheLogLine.objects.all().order_by('-id')
        logs = paginate(all_logs, request)
        context = super(ApacheLogsPage, self).get_context_data(**kwargs)
        context['logs'] = logs
        context['page'] = "all"
        return context


class ApacheErrorsPage(generic.ListView):
    model = ApacheLogLine
    template_name = "apache_an/errors.html"
    context_object_name = "meta"

    def get_context_data(self, **kwargs):
        request = self.request
        all_logs = ApacheLogLine.objects.filter(req_status='404').order_by('-id')
        logs = paginate(all_logs, request)
        context = super(ApacheErrorsPage, self).get_context_data(**kwargs)
        context['logs'] = logs
        context['page'] = "errors"
        return context


class LastLogPage(generic.ListView):
    model = ApacheLogLine
    template_name = "apache_an/log_line.json"
    context_object_name = "meta"

    def get_context_data(self, **kwargs):
        # request = self.request
        last_line = ApacheLogLine.objects.all().order_by('-id')[0]
        context = super(LastLogPage, self).get_context_data(**kwargs)

        context['l'] = serializers.serialize('json', [last_line])
        return context
