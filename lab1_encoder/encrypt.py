import cv2
import numpy as np
import random

# Параметри сітки
ROWS, COLS = 12, 16 
SEED = 44257

def encrypt():
    # 1. Завантаження кадру
    img = cv2.imread("input.png")
    if img is None:
        print("Помилка: Файл input.png не знайдено!")
        return

    # 2. Підгонка розміру під сітку
    h, w, _ = img.shape
    new_h, new_w = (h // ROWS) * ROWS, (w // COLS) * COLS
    img = cv2.resize(img, (new_w, new_h))
    bh, bw = new_h // ROWS, new_w // COLS

    # 3. Розбиття на блоки
    blocks = []
    for r in range(ROWS):
        for c in range(COLS):
            blocks.append(img[r*bh:(r+1)*bh, c*bw:(c+1)*bw])

    # 4. Генерація ключа (LFSR/Random)
    gen = random.Random(SEED)
    perm = list(range(len(blocks)))
    gen.shuffle(perm)

    # 5. Створення шифрованого зображення
    res_img = np.zeros_like(img)
    for i in range(len(blocks)):
        target_idx = perm[i]
        tr, tc = divmod(target_idx, COLS)
        res_img[tr*bh:(tr+1)*bh, tc*bw:(tc+1)*bw] = blocks[i]

    cv2.imwrite("scrambled.png", res_img)
    print("Готово! Зашифроване зображення збережено як 'scrambled.png'")

if __name__ == "__main__":
    encrypt()
