print("---Convertir segundos a hora (23:59:59)---")
import datetime
seg = float(input("Por favor ingrese la cantidad de segundos: "))
print("{0:g}".format(seg), "segundos en horas, minutos y segundos son: ", datetime.timedelta(seconds=seg),".")