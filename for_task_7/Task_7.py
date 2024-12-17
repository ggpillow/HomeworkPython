import csv

class Customer:
    def __init__(self, name, sex, age, device_type, browser, bill, region):
        self.name = name
        self.sex = sex
        self.age = age
        self.device_type = device_type
        self.browser = browser
        self.bill = bill
        self.region = region

    def describe(self):
        gender = "женского пола" if self.sex == 'female' else "мужского пола"
        device = self.get_device()
        description = (f"Пользователь {self.name} {gender}, {self.age} лет совершил{'' if self.sex == 'male' else 'а'} покупку "
                       f"на {self.bill} у.е. с {device} браузера {self.browser}. "
                       f"Регион, из которого совершалась покупка: {self.region}.")
        return description

    def get_device(self):
        devices = {
            'mobile': "мобильного",
            'tablet': "планшета",
            'laptop': "ноутбука",
            'desktop': "стационарного компьютера"
        }
        return devices.get(self.device_type, "неизвестного устройства")

class CustomerManager:
    def __init__(self, filename):
        self.filename = filename
        self.customers = []

    def load_data(self):
        try:
            with open(self.filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    customer = Customer(name=row['name'], sex=row['sex'], age=row['age'],
                                        device_type=row['device_type'], browser=row['browser'],
                                        bill=row['bill'], region=row['region'])
                    self.customers.append(customer)
        except FileNotFoundError:
            print("Файл не найден")
        except Exception as e:
            print(f"Произошла ошибка при загрузке данных: {e}")

    def write_descriptions(self, output_filename):
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                for customer in self.customers:
                    description = customer.describe()
                    file.write(description + "\n")
            print("Описания сохранены в файл", output_filename)
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")

def main():
    manager = CustomerManager('web_clients_correct.csv')
    manager.load_data()
    manager.write_descriptions('client_descriptions.txt')


main()