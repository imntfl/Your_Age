#import 
from datetime import date

dr = input("Введите дату вашего рождения в формате(ГГГГ-MM-ДД): ")
dr = date.fromisoformat(dr)

vozrast = int((dr.today() - dr).days / 365.25)

print("Вам ", vozrast, " лет")
