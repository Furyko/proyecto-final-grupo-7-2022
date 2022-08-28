from calendar import HTMLCalendar
from .models import Evento

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, categoria=None):
        self.year = year
        self.month = month
        self.categoria = categoria
        super(Calendar, self).__init__()

    """Formatea un día como un td. Filtra eventos por día."""
    def formatday(self, day, events):
        events_per_day = events
        d = ''
        if day != 0:
            for event in events_per_day:
                if event.fecha.day == day:
                    d += f'<li> {event.nombre} </li>'
                    return f"<td class='event-day'><button><span class='date'>{day}</span><ul> {d} </ul></button></td>"
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    """Formatea una semana como tr"""
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    """Formatea un mes como un table. Filtra eventos por año y mes"""
    def formatmonth(self, withyear=True):
        if self.month < 10:
            events = Evento.objects.filter(fecha__contains=str(self.year) + "-" + "0" + str(self.month))
        else:
            events = Evento.objects.filter(fecha__contains=str(self.year) + "-" + str(self.month))
        calendar = f'<table id="calendar" class="calendar">\n'
        calendar += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        calendar += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f'{self.formatweek(week, events)}\n'
        calendar += f'</table>'
        return calendar
