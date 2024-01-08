import json
from mycalendar import print_calendar

# Charger les rendez-vous depuis le fichier JSON
def load_appointments(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Enregistrer les rendez-vous dans le fichier JSON
def save_appointments(appointments, filename):
    with open(filename, "w") as file:
        json.dump(appointments, file, indent=4)

# Ajouter un rendez-vous
def add_appointment(appointments, date, description):
    if date in appointments:
        appointments[date].append(description)
    else:
        appointments[date] = [description]
        
def add_appointment_interactively(appointments, filename):
    # Demander la date et la description du rendez-vous
    date = input("Entrez la date du rendez-vous (format YYYY-MM-DD): ")
    description = input("Entrez la description du rendez-vous: ")

    # Ajouter le rendez-vous
    add_appointment(appointments, date, description)

    # Sauvegarder les modifications
    save_appointments(appointments, filename)

# Utilisation
appointments_file = "appointments.json"
appointments = load_appointments(appointments_file)

print_calendar(appointments)
add_appointment_interactively(appointments, appointments_file)
