# Template tag
from datetime import date, timedelta

from django import template
from bookings.models import Booking
register = template.Library()


from datetime import date, timedelta

#source:<https://djangosnippets.org/snippets/129/>

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)


def month_cal(year=date.today().year, month=date.today().month):
    booking_list = Booking.objects.filter(
    checkin_date__gte==first_day_of_calendar, checkin_date__lte=last_day_of_calendar
    )

    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())

    month_cal = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['booking'] = False
        for booking in booking_list:
            if day >= booking.checkin_date.date() and day <= booking.checkout_date.date():
                cal_day['booking'] = True
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False  
        week.append(cal_day)
        if day.weekday() == 6:
            month_cal.append(week)
            week = []
        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers}

register.inclusion_tag('month_cal.html')(month_cal)

"""
Put this in your template (in my case agenda/month_cal.html):

<table class="cal_month_calendar">
<tr>
{% for day in headers %}
<th>{{ day|date:"D"|slice:":2" }}</th>
{% endfor %}
</tr>
{% for week in calendar %}
<tr>
{% for day in week %}
<td{% if not day.in_month %} class="cal_not_in_month"{% endif %}>{% if day.event %}<a href="/calendar/{{ day.day|date:"Y/m" }}/">{{ day.day|date:"j" }}</a>{% else %}{{ day.day|date:"j" }}{% endif %}</td>
{% endfor %}
</tr>
{% endfor %}
</table>

"""
