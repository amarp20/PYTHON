def dias_en_mes(year, month):

  dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if not int(year) or not int(month):
    return None
  if year <= 0 or month <= 0 or month > 12:
    return None
  if month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    else:
        return 28
   

year=int(input("Introduce un año: "))
month=int(input("Introduce el numero de un mes: "))

dias_por_mes[month - 1]