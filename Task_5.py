from datetime import datetime, timedelta

def mainApp():
    while True:
        user_date = input("Введите дату в формате dd-mm-yyyy (для завершения программы введите q): ").strip()
        
        if user_date.lower() == 'q':
            print("Конец программы")
            break
        
        try:
            data_new = datetime.strptime(user_date, '%d-%m-%Y')
            
            day_without_zero = str(data_new.day)
            
            date_mosc = data_new.strftime(f'%A, %B {day_without_zero}, %Y')
            print(f"The Moscow Times — {date_mosc}")
            
            date_guardian = data_new.strftime('%A, %d.%m.%y')
            print(f"The Guardian — {date_guardian}")
            
            date_daily = data_new.strftime('%A, %d %B %Y')
            print(f"Daily News — {date_daily}")
            
            continue
            
        except ValueError:
            print("Неверный формат даты!")
            
mainApp()