#hour=int(input("Hora de inicio (Horas):   "))
#mins=int(input("Minuto de inicio (Minutos):   "))
#dura=int(input("Duracion del evento (minutos):   "))
#minutos=str((mins+dura)%60)
#horas=str(((hour*60+mins+dura)//60)%24)
#print("Hora:   "+horas+":"+minutos)

hora=int(input("Introduzca la hora de inicio: "))
minutos=int(input("Introduzca los minutos de la hora de inicio: "))
duracion=int(input("Introduzca la duracion del partidoen minutos: "))

hora_final=((hora*60+duracion+minutos)//60)%24

minutos_finales=(duracion+minutos)%60

print(f"Hora de inicio:  {hora}:{minutos}, Duracion del partido: {duracion} minutos. Hora de finalizacion del partido: {hora_final}:{minutos_finales}")