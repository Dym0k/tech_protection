import hashlib

def generate_and_save():
    # Просимо користувача ввести PIN-код
    pin = input("Введіть 5-значний PIN-код для хешування: ")
    
    # Невеличка перевірка, щоб переконатися, що введено саме 5 цифр
    if len(pin) != 5 or not pin.isdigit():
        print("Помилка: PIN-код має складатися рівно з 5 цифр!")
        return

    # Перетворюємо PIN у байти та генеруємо MD5 хеш
    hashed_pin = hashlib.md5(pin.encode()).hexdigest()
    
    # Зберігаємо хеш у файл. Режим "w" (write) створить файл або перезапише існуючий
    filename = "hash_db.txt"
    with open(filename, "w") as file:
        file.write(hashed_pin)
        
    print(f"Успіх! Хеш {hashed_pin} збережено у файл {filename}.")

if __name__ == "__main__":
    generate_and_save()
    
