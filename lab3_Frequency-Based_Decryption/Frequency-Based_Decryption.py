def frequency_decrypt():
    # Еталонні частоти літер в англійській мові з умови задачі
    ENGLISH_FREQS = {
        'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56, 'F': 2.17, 'G': 1.80, 'H': 5.27,
        'I': 7.24, 'J': 0.14, 'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47, 'P': 1.91,
        'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15, 'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21,
        'Y': 1.65, 'Z': 0.07
    }

    def get_decoded_text(text, shift):
        # Функція для розшифрування тексту із заданим зсувом
        result = ""
        for char in text:
            if char.isalpha():
                # Визначаємо базу (A або a) для збереження регістру
                start = ord('A') if char.isupper() else ord('a')
                # Зсуваємо назад і використовуємо % 26 для циклічності
                decoded_char = chr(start + (ord(char) - start - shift) % 26)
                result += decoded_char
            else:
                # Символи та цифри залишаються без змін
                result += char
        return result

    def calculate_score(text):
        # Рахуємо, наскільки частоти в тексті схожі на еталонні
        letters_only = [c.upper() for c in text if c.isalpha()]
        if not letters_only:
            return float('inf')
        
        total_letters = len(letters_only)
        # Рахуємо відсоток кожної літери в поточному варіанті тексту
        text_freqs = {l: (letters_only.count(l) / total_letters) * 100 for l in ENGLISH_FREQS}
        
        # Вираховуємо сумарну різницю (Score)
        # Чим менше це число, тим більше текст схожий на англійську
        score = 0
        for char in ENGLISH_FREQS:
            score += abs(text_freqs[char] - ENGLISH_FREQS[char])
        return score

    # Отримуємо зашифроване повідомлення від користувача
    cipher_text = input("Введіть зашифроване повідомлення: ")
    
    best_shift = 0
    min_score = float('inf')
    
    # Перевіряємо всі 26 можливих зсувів
    for shift in range(26):
        current_decoded = get_decoded_text(cipher_text, shift)
        current_score = calculate_score(current_decoded)
        
        # Шукаємо варіант з найменшою різницею частот
        if current_score < min_score:
            min_score = current_score
            best_shift = shift
            
    # Виводимо фінальний результат
    final_text = get_decoded_text(cipher_text, best_shift)
    print(f"\nАналіз завершено!")
    print(f"Найімовірніший ключ зсуву: {best_shift}")
    print(f"Розшифрований текст:\n{final_text}")

if __name__ == "__main__":
    frequency_decrypt()
