# -*- coding: utf-8 -*-
from datetime import datetime

from django import template
import locale

register = template.Library()


@register.filter("timestamp")
def timestamp(value):
    try:
        return datetime.fromtimestamp(value)
    except AttributeError:
        return ''

@register.filter("mod")
def mod(value):
    try:
        return value % 2
    except AttributeError:
        return ''

@register.filter("str_transfer")
def str_transfer(value):
    try:
        return value.replace('<', '').replace('>', '').replace('/', '').replace('\n', '<br />')
    except AttributeError:
        return ''

@register.filter("date_day")
def date_day(value):
    try:
        return datetime.fromtimestamp(value).day
    except AttributeError:
        return ''

@register.filter("get_range")
def get_range( value ):
    try:
        return range(value)
    except:
        return []


@register.filter("time_detect")
def time_detect(value):
    try:
        date_time = datetime.fromtimestamp(value)
        if date_time.time().hour == 11:
            return "X"
    except AttributeError:
        return ''


@register.filter("monthes")
def monthes(value):
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return value.strftime("%d %B")
    except AttributeError:
        return ''


@register.filter("paging_back")
def paging_back(value):
    try:
        if value >= 2:
            return int(value) - 1
        else:
            return 1
    except AttributeError:
        return 1


@register.filter("paging_forward")
def paging_forward(value):
    try:
        return int(value) + 1
    except AttributeError:
        return 1

@register.filter("temperature")
def temperature(value):
    try:
        return round(value - 273.15, 1)
    except AttributeError:
        return ''


@register.filter("icon")
def icon(value):
    try:
        return value[0]['icon']
    except AttributeError:
        return 'no icon'


@register.filter("weather_id")
def weather_id(value):
    try:
        return value[0]['id']
    except:
        return 'no status'


@register.filter("forecast_temp")
def forecast_temp(value):
    try:
        return value[0]['id']
    except AttributeError:
        return 'no status'


@register.filter("pressure")
def pressure(value):
    try:
        return int(value * 0.75006375541921)
    except AttributeError:
        return ''



@register.filter("status")
def status(value):
    try:
        if value == 200:
            return u"гроза, небольшой дождь"
        if value == 201:
            return u"гроза с дождем"
        if value == 202:
            return u"гроза с проливным дождем"
        if value == 210:
            return u"слабая гроза"
        if value == 211:
            return u"гроза"
        if value == 212:
            return u"сильная гроза"
        if value == 221:
            return u"адовая гроза"
        if value == 230:
            return u"гроза, слабый моросящий дождь"
        if value == 231:
            return u"гроза, моросящий дождь"
        if value == 232:
            return u"гроза, сильный моросящий дождь"
        if value == 300:
            return u"слабая морось"
        if value == 301:
            return u"морось"
        if value == 302:
            return u"сильная морось"
        if value == 310:
            return u"слабый моросящий дождь"
        if value == 311:
            return u"моросящий дождь"
        if value == 312:
            return u"сильный моросящий дождь"
        if value == 313:
            return u"ливень и изморось"
        if value == 314:
            return u"сильный ливень и изморось"
        if value == 321:
            return u"проливной моросящий дождь"
        if value == 500:
            return u"небольшой дождь"
        if value == 501:
            return u"дождь"
        if value == 502:
            return u"сильный дождь"
        if value == 503:
            return u"очень сильный дождь"
        if value == 504:
            return u"очень сильный дождь"
        if value == 511:
            return u"ледяной дождь"
        if value == 520:
            return u"слабый проливной дождь"
        if value == 521:
            return u"проливной дождь"
        if value == 522:
            return u"сильный проливной дождь"
        if value == 531:
            return u"сильнейший ливень"
        if value == 600:
            return u"небольшой снегопад"
        if value == 601:
            return u"снегопад"
        if value == 602:
            return u"сильный снегопад"
        if value == 611:
            return u"слякоть"
        if value == 612:
            return u"дождь и слякоть"
        if value == 615:
            return u"небольшой дождь и снег"
        if value == 616:
            return u"дождь и снег"
        if value == 620:
            return u"небольшой мокрый снег"
        if value == 621:
            return u"снегопад"
        if value == 622:
            return u"сильный мокрый снег"
        if value == 701:
            return u"туман"
        if value == 711:
            return u"смог"
        if value == 721:
            return u"дымка"
        if value == 731:
            return u"песчаная буря"
        if value == 741:
            return u"туманно"
        if value == 751:
            return u"песок"
        if value == 761:
            return u"пыль"
        if value == 752:
            return u"вулканический пепел"
        if value == 771:
            return u"шквал"
        if value == 781:
            return u"торнадо"
        if value == 800:
            return u"ясно"
        if value == 801:
            return u"слегка облачно"
        if value == 802:
            return u"облачно"
        if value == 803:
            return u"пасмурно с прояснениями"
        if value == 804:
            return u"пасмурно"
        if value == 900:
            return u"торнадо"
        if value == 901:
            return u"тропический шторм"
        if value == 902:
            return u"ураган"
        if value == 903:
            return u"мороз"
        if value == 904:
            return u"жара"
        if value == 905:
            return u"ветренно"
        if value == 906:
            return u"град"
        if value == 951:
            return u"ШТИЛЬ"
        if value == 952:
            return u"ТИХИЙ ВЕТЕР"
        if value == 953:
            return u"ЛЕГКИЙ ВЕТЕР"
        if value == 954:
            return u"СЛАБЫЙ ВЕТЕР"
        if value == 955:
            return u"умеренный ветер"
        if value == 956:
            return u"свежий ветер"
        if value == 957:
            return u"сильный ветер"
        if value == 958:
            return u"очень сильный ветер"
        if value == 959:
            return u"штормовой ветер"
        if value == 960:
            return u"ШТОРМ"
        if value == 961:
            return u"сильный ШТОРМ"
        if value == 962:
            return u"опасный ШТОРМ"
    except AttributeError:
        return ''


@register.filter("deg")
def deg(value):
    try:
        val = int((value / 22.5) + .5)
        arr = ["n.png", "nne.png", "ne.png", "nee.png", "e.png", "ees.png", "es.png", "ess.png", "s.png", "ssw.png",
               "sw.png", "sww.png", "w.png", "nww.png", "nw.png", "nnw.png"]
        return arr[(val % 16)]
    except:
        return ''
