def enigma_simulator(operation, shift_start, rotors, message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if operation == "ENCODE":
        # 1. Caesar Shift з інкрементом
        res = ""
        for i, char in enumerate(message):
            index = alphabet.find(char)
            new_index = (index + shift_start + i) % 26
            res += alphabet[new_index]
        
        # 2. Прохід через 3 ротори (0 -> 1 -> 2)
        for rotor in rotors:
            temp = ""
            for char in res:
                index = alphabet.find(char)
                temp += rotor[index]
            res = temp
        return res

    elif operation == "DECODE":
        # 1. Зворотний прохід через ротори (2 -> 1 -> 0)
        res = message
        for rotor in reversed(rotors):
            temp = ""
            for char in res:
                index = rotor.find(char)
                temp += alphabet[index]
            res = temp
            
        # 2. Зворотний Caesar Shift з інкрементом
        final_message = ""
        for i, char in enumerate(res):
            index = alphabet.find(char)
            # Використовуємо % 26, щоб залишатися в межах алфавіту
            new_index = (index - shift_start - i) % 26
            final_message += alphabet[new_index]
        return final_message

# Дані з прикладу
rotors_list = [
    "BDFHJLCPRTXVZNYEIWGAKMUSQO", # Rotor 0
    "AJDKSIRUXBLHWTMCQGZNPYFVOE", # Rotor 1
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ"  # Rotor 2
]

#Test 1

# Вхідні дані для шифрування
input_message = "AAA"
start_shift = 4

# Виклик функції та збереження результату
encoded_result = enigma_simulator("ENCODE", start_shift, rotors_list, input_message)

# Вивід результату в консоль
print("--- ТЕСТ №1: ШИФРУВАННЯ ---")
print(f"Початкове повідомлення: {input_message}")
print(f"Стартовий зсув: {start_shift}")
print(f"Результат (Cipher): {encoded_result}")

#Test 2

decode_shift = 4

# Виклик функції для повернення оригіналу

dec_result = enigma_simulator("DECODE", decode_shift, rotors_list, encoded_result)

# Вивід результату в консоль
print("\n--- ТЕСТ №2: РОЗШИФРУВАННЯ ---")
print(f"Зашифрований текст: {encoded_result}")
print(f"Стартовий зсув: {decode_shift}")
print(f"Розшифроване повідомлення: {dec_result}")

#Test 3

# Вхідні дані для розшифрування
cipher_text = "PQSACVVTOISXFXCIAMQEM"
decode_shift = 9

# Виклик функції для повернення оригіналу
decoded_result = enigma_simulator("DECODE", decode_shift, rotors_list, cipher_text)

# Вивід результату в консоль
print("\n--- ТЕСТ №3: РОЗШИФРУВАННЯ ---")
print(f"Зашифрований текст: {cipher_text}")
print(f"Стартовий зсув: {decode_shift}")
print(f"Розшифроване повідомлення: {decoded_result}")
