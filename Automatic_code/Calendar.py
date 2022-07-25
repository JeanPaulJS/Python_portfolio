import calendar
from operator import length_hint
from pathlib import Path


meses_años = list(calendar.month_name[1:])
#La lista de calendar especifica los meses del año (EN INGLES)
dia_semana = ['Dia 1', 'Dia 10', 'Dia 20','Dia 30']
#dia_semana es una lista que se puede modificar con un bucle por ejemplo, de manera general se usa cuatro para simplificar el proceso


c = calendar.TextCalendar(calendar.SUNDAY)
#anio = int(input("Ingrese el año que desea conocer: "))
#mes = int(input("Ingrese el numero de mes de calendario: ")) 
#c.prmonth(anio, mes)
cal = calendar.Calendar(calendar.SUNDAY)
cal_data = cal.yeardays2calendar(2017, 3)
print(cal_data)