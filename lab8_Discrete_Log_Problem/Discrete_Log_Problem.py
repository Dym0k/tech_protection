import math

def solve_discrete_log(g, h, q):
    """
    Розв'язує рівняння g^x ≡ h (mod q) за допомогою алгоритму BSGS.
    Складність: O(sqrt(q))
    """
    m = math.ceil(math.sqrt(q))
    
    # --- Крок дитини (Baby steps) ---
    # Обчислюємо g^j mod q для j від 0 до m і зберігаємо в словник
    baby_steps = {}
    current = 1
    for j in range(m):
        if current not in baby_steps:
            baby_steps[current] = j
        current = (current * g) % q
        
    # --- Підготовка до кроку велетня ---
    # Потрібно g^(-m) mod q. 
    # В Python 3.8+ pow(a, -1, q) обчислює модульну інверсію.
    # g^(-m) = (g^m)^(-1)
    gm = pow(g, m, q)
    try:
        giant_stride = pow(gm, -1, q)
    except ValueError:
        return None  # Інверсії не існує, якщо g і q не взаємно прості

    # --- Крок велетня (Giant steps) ---
    # Обчислюємо target = h * (g^-m)^i mod q
    target = h
    for i in range(m):
        if target in baby_steps:
            # Ми знайшли збіг! x = i*m + j
            x = i * m + baby_steps[target]
            return x
        target = (target * giant_stride) % q
        
    return None

def verify_result(g, x, q, h):
    """
    Перевіряє, чи дійсно g^x mod q == h
    """
    if x is None:
        print("❌ Помилка: Розв'язок не знайдено.")
        return False
    
    # Використовуємо вбудоване швидке піднесення до степеня
    result = pow(g, x, q)
    if result == h:
        print(f"✅ Перевірка пройдена: {g}^{x} mod {q} = {h}")
        return True
    else:
        print(f"❌ Помилка: {g}^{x} mod {q} = {result}, а очікувалось {h}")
        return False

# --- Приклад використання ---
# Умова: log_18(65) в Z_163 (g=18, h=65, q=163)
G = 18
H = 65
Q = 163

print(f"Шукаємо найменше x для: {G}^x ≡ {H} (mod {Q})")
x_found = solve_discrete_log(G, H, Q)

if x_found is not None:
    print(f"Знайдений секретний ключ X: {x_found}")
    verify_result(G, x_found, Q, H)
else:
    print("Розв'язок не знайдено.")
