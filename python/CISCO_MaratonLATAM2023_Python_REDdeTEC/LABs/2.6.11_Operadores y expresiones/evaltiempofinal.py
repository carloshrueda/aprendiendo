hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
newMins = mins + dura
newHour = newMins // 60

hour += newHour
# while (hour >= 24):
#     hour -= 24
if (hour >= 24):
    hour = hour - ((hour // 24) * 24)
mins = newMins -(newHour*60)
print(f"{hour}:{mins}")