import datetime
from astral import Location

def print_sun_info(_location, _date):
    print('Information for %s/%s\n' % (_location.name, _location.region))
    print('Date: %s' % _date)
    print('Timezone:  %s' % _location.timezone)
    print('Position:  %.02f / %.02f\n' % (_location.latitude, _location.longitude))

    _sun = _location.sun(date=_date, local=True)
    _daylight = _location.daylight(date=_date, local=True)

    print('Morgendaemmerung:   %s' % str(_sun['dawn'].time()))
    print('Sonnenaufgang:      %s' % str(_sun['sunrise'].time()))
    print('Sonnenhoechststand: %s' % str(_sun['noon'].time()))
    print('Sonnenuntergang:    %s' % str(_sun['sunset'].time()))
    print('Abenddaemmerung:    %s\n' % str(_sun['dusk'].time()))
    print('Tageslaenge:        %s' % (_daylight[1] - _daylight[0]))
    return


exposition = 'Nord-West'
today = datetime.date.today()
location = Location(('Zwischenflueh-Buehl', 'Diemtigen', 46.611727, 7.536737, 'Europe/Zurich', 1062))
location.solar_depression = 'civil'

print_sun_info(location, today)

