import hashlib

def crack(hash_to_crack):
    # Перебираємо всі можливі варіанти PIN-коду від 0 до 99999
    for i in range(100000):
        pin = f"{i:05d}"
        current_hash = hashlib.md5(pin.encode()).hexdigest()
        
        if current_hash == hash_to_crack:
            return pin 
            
    return None 

if __name__ == "__main__":
    filename = "hash_db.txt"
    
    try:
        # Відкриваємо файл у режимі читання "r" (read)
        with open(filename, "r") as file:
            # Читаємо вміст файлу. 
            # Метод .strip() дуже важливий: він видаляє невидимі символи (наприклад, перехід на новий рядок \n), 
            # які могли випадково потрапити у файл і зламати б порівняння рядків.
            target_hash = file.read().strip()
            
        print(f"Зчитано хеш з файлу: {target_hash}")
        
        # Запускаємо нашу функцію
        cracked_pin = crack(target_hash)
        
        if cracked_pin:
            print(f"Знайдений PIN-код: {cracked_pin}")
        else:
            print("Не вдалося знайти відповідний 5-значний PIN-код.")
            
    # Обробка помилки, якщо файл ще не створено
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено. Спочатку запустіть програму генерації хешу!")
        
