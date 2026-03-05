import cv2
import numpy as np
import random

# Ті ж самі параметри, що й при шифруванні
ROWS, COLS = 12, 16 
SEED = 44257

def decrypt():
    # 1. Завантаження зашифрованого кадру
    img = cv2.imread("scrambled.png")
    if img is None:
        print("Помилка: Файл scrambled.jpg не знайдено!")
        return

    h, w, _ = img.shape
    bh, bw = h // ROWS, w // COLS

    # 2. Витягуємо перемішані блоки
    scrambled_blocks = []
    for r in range(ROWS):
        for c in range(COLS):
            scrambled_blocks.append(img[r*bh:(r+1)*bh, c*bw:(c+1)*bw])

    # 3. Генерація того ж самого ключа
    gen = random.Random(SEED)
    perm = list(range(len(scrambled_blocks)))
    gen.shuffle(perm)

    # 4. Відновлення (зворотна логіка)
    res_img = np.zeros_like(img)
    for i in range(len(scrambled_blocks)):
        # Ми знаємо, що оригінальний блок зараз лежить на позиції perm[i]
        source_idx = perm[i]
        r, c = divmod(i, COLS)
        res_img[r*bh:(r+1)*bh, c*bw:(c+1)*bw] = scrambled_blocks[source_idx]

    cv2.imwrite("restored.png", res_img)
    print("Готово! Оригінал відновлено у файл 'restored.png'")

if __name__ == "__main__":
    decrypt()
