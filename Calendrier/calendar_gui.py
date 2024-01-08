import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime
# Importez vos fonctions de gestion des rendez-vous ici
from main import load_appointments, save_appointments, add_appointment

class CalendarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calendrier")
        self.geometry("600x400")

        # Charger les rendez-vous
        self.appointments_file = "appointments.json"
        self.appointments = load_appointments(self.appointments_file)

        # Afficher le calendrier
        self.display_calendar()

    def display_calendar(self):
        now = datetime.now()
        cal = calendar.monthcalendar(now.year, now.month)

        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day != 0:
                    day_str = f"{now.year}-{now.month:02}-{day:02}"
                    color = "green" if day_str in self.appointments else "white"
                    btn = tk.Button(self, text=str(day), bg=color, 
                                    command=lambda d=day_str: self.show_appointments(d))
                    btn.grid(row=i, column=j)

    def show_appointments(self, date):
        appointments_str = "\n".join(self.appointments.get(date, ["Pas de rendez-vous"]))
        messagebox.showinfo("Rendez-vous", f"Rendez-vous pour {date}:\n{appointments_str}")

# Exécuter l'application
if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
