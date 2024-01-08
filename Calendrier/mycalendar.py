import calendar
from datetime import datetime

def print_calendar(appointments):
	now = datetime.now()
	year = now.year
	month = now.month

# Créer un objet de calendrier texte
	cal = calendar.TextCalendar(calendar.MONDAY)
	calendrier_mois = cal.formatmonth(year, month)

	print(calendrier_mois)

	print("Rendez-vous de ce mois:")
	for date, events in appointments.items():
		date_obj = datetime.strptime(date, "%Y-%m-%d")
		if date_obj.year == year and date_obj.month == month:
			print(f"{date}: {', '.join(events)}")
			