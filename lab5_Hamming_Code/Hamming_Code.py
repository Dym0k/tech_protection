def encode(text):
    """
    Перетворює текст у бінарний вигляд і потроює кожен біт.
    """
    encoded_str = ""
    
    for char in text:
        # 1. Перетворюємо символ на ASCII код (напр. 'h' -> 104)
        ascii_val = ord(char)
        
        # 2. Перетворюємо ASCII код на 8-бітний рядок (напр. 104 -> '01101000')
        binary_str = format(ascii_val, '08b')
        
        # 3 & 4. Потроюємо кожен біт і додаємо до загального результату
        for bit in binary_str:
            encoded_str += bit * 3
            
    return encoded_str


def decode(bits):
    """
    Виправляє помилки у бінарному рядку та перетворює його назад у текст.
    """
    corrected_bits = ""
    
    # 1 & 2. Розбиваємо вхідний рядок на групи по 3 біти і "голосуємо"
    # Йдемо по рядку з кроком 3
    for i in range(0, len(bits), 3):
        triplet = bits[i:i+3]
        
        # Метод більшості: якщо одиниць 2 або 3, значить правильний біт - 1.
        # Якщо нулів більше - значить правильний біт - 0.
        if triplet.count('1') >= 2:
            corrected_bits += '1'
        else:
            corrected_bits += '0'

    decoded_text = ""
    
    # 3. Розбиваємо виправлені біти на групи по 8 (байти)
    # Йдемо по рядку з кроком 8
    for i in range(0, len(corrected_bits), 8):
        byte_str = corrected_bits[i:i+8]
        
        # 4. Перетворюємо 8 біт у десяткове число (ASCII)
        ascii_val = int(byte_str, 2)
        
        # 5. Перетворюємо ASCII число у символ
        decoded_text += chr(ascii_val)
        
    return decoded_text


# --- Блок тестування ---
if __name__ == "__main__":
    original_text = "hey"
    print(f"Початковий текст: '{original_text}'")
    
    # Тестуємо кодування
    encoded_bits = encode(original_text)
    print(f"Закодовані дані: {encoded_bits}")
    
    # Тестуємо декодування ідеального рядка
    print(f"Декодування ідеального рядка: '{decode(encoded_bits)}'")
    
    # Імітуємо перешкоди: псуємо кілька бітів (перетворюємо 1 на 0 і навпаки)
    # Змінимо 1-й, 5-й та 15-й біти для наочності
    damaged_bits = list(encoded_bits)
    damaged_bits[0] = '1' # Був '0'
    damaged_bits[4] = '0' # Був '1'
    damaged_bits[14] = '1' # Був '0'
    damaged_bits_str = "".join(damaged_bits)
    
    print(f"\nДані ПІСЛЯ перешкод:  {damaged_bits_str}")
    
    # Пробуємо розшифрувати пошкоджені дані
    restored_text = decode(damaged_bits_str)
    print(f"Декодування пошкоджених даних: '{restored_text}'")
    

