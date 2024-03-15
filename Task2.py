# Додаємо коментарі українською мовою до коду

def draw_tree(ax, origin, angle, length, level, max_level):
    """
    Функція для малювання дерева за допомогою рекурсії.

    Параметри:
    ax -- об'єкт matplotlib axes, на якому буде намальовано дерево.
    origin -- кортеж (x, y) початкової точки гілки.
    angle -- кут нахилу гілки.
    length -- довжина гілки.
    level -- поточний рівень рекурсії.
    max_level -- максимальний рівень рекурсії.
    """
    if level > max_level:
        return
    
    # Обчислюємо кінцеву точку гілки
    end_x = origin[0] + length * np.cos(angle)
    end_y = origin[1] + length * np.sin(angle)
    end_point = (end_x, end_y)
    
    # Малюємо гілку від початкової до кінцевої точки
    ax.plot([origin[0], end_point[0]], [origin[1], end_point[1]], 'r')
    
    # Зменшуємо довжину наступних гілок
    new_length = length * np.sqrt(2)/2
    
    # Ліва гілка під кутом 45 градусів
    draw_tree(ax, end_point, angle - np.pi/4, new_length, level + 1, max_level)
    
    # Права гілка під кутом 45 градусів
    draw_tree(ax, end_point, angle + np.pi/4, new_length, level + 1, max_level)

# Налаштування фігури та осей для малюнка
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
plt.axis('off')

# Визначаємо рівень рекурсії
recursion_level = 5  # Приклад рівня рекурсії, який можна змінювати користувачем

# Початкова точка для дерева
origin = (0.5, 0.1)  # Починаємо з центру нижньої частини графіка

# Початкова довжина та кут
initial_length = 0.3  # Початкова довжина дерева
initial_angle = np.pi/2  # Початковий кут (90 градусів для росту вгору)

# Малюємо дерево Піфагора
draw_tree(ax, origin, initial_angle, initial_length, 0, recursion_level)

# Показуємо графік
plt.show()
