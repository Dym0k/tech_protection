def solve_robber_city(hex1, hex2, hex3):
    # 1. Перетворюємо Hex-рядки у набори байтів
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)
    bytes3 = bytes.fromhex(hex3)
    
    # 2. Масив для збереження розшифрованих символів
    result_message = ""
    
    # 3. Проходимо по кожному байту повідомлень одночасно
    # Формула: M = Message1 XOR Message2 XOR Message3
    for b1, b2, b3 in zip(bytes1, bytes2, bytes3):
        # Виконуємо XOR
        decoded_byte = b1 ^ b2 ^ b3
        # Перетворюємо числовий код ASCII назад у символ
        result_message += chr(decoded_byte)
        
    return result_message

# --- ПІДСТАВЛЕНІ ДАНІ (Приклад для слова ATTACK) ---
# Message1 (M ^ K1)
m1 = "51444451535b" 
# Message2 (M ^ K1 ^ K2)
m2 = "50454550525a"
# Message3 (M ^ K2)
m3 = "40555540424a"

# Запуск взлому
clear_text = solve_robber_city(m1, m2, m3)

print("--- ВЗЛОМ ROBBERCITY ---")
print(f"Перехоплено M1: {m1}")
print(f"Перехоплено M2: {m2}")
print(f"Перехоплено M3: {m3}")
print("-" * 25)
print(f"РОЗШИФРОВАНО: {clear_text}")
