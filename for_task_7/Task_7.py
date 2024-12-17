import csv

def load_data(filename):
    """ Загружает данные из CSV-файла """
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных: {e}")
        return []

def create_description(customer):
    """ Формирует описание для одного покупателя """
    gender = "женского пола" if customer['sex'] == 'female' else "мужского пола"
    device_change = device(customer['device_type'])
    description = f"Пользователь {customer['name']} {gender}, {customer['age']} лет совершил{'' if customer['sex'] == 'male' else 'а'} покупку на {customer['bill']} у.е. с {device} браузера {customer['browser']}. Регион, из которого совершалась покупка: {customer['region']}."
    return description

def device(device):
    devices = {
        'mobile': "мобильного",
        'tablet': "планшета",
        'laptop': "ноутбука",
        'desktop': "стационарного компьютера"
    }
    return devices.get(device, "неизвестного устройства")  # Возвращаем по умолчанию "неизвестное устройство", если тип не определен

def write_descriptions(descriptions, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for description in descriptions:
                file.write(description + "\n")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

def main():
    data = load_data('web_clients_correct.csv')
    if not data:
        return

    descriptions = [create_description(customer) for customer in data]

    write_descriptions(descriptions, 'client_descriptions.txt')
    print("Описания сохранены в файл 'client_descriptions.txt'.")

main()