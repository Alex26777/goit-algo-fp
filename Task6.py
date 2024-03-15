# Вихідні дані задачі
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, max_cost):
    """Жадібний алгоритм для максимізації калорійності страв за обмеженого бюджету."""
    # Сортування страв за співвідношенням калорій до вартості (спадання)
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= max_cost:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_calories

def dynamic_programming(items, max_cost):
    """Динамічне програмування для знаходження оптимального набору страв."""
    # Підготовка таблиці для динамічного програмування
    dp = [[0] * (max_cost + 1) for _ in range(len(items) + 1)]
    item_list = list(items.items())

    for i in range(1, len(item_list) + 1):
        for w in range(1, max_cost + 1):
            item_name, details = item_list[i - 1]
            if details['cost'] <= w:
                # Якщо можемо взяти страву - вибираємо максимум між взяттям страви та не взяттям
                dp[i][w] = max(details['calories'] + dp[i - 1][w - details['cost']], dp[i - 1][w])
            else:
                # Якщо не можемо взяти страву - беремо попереднє значення
                dp[i][w] = dp[i - 1][w]

    # Знаходимо вибрані страви
    w = max_cost
    n = len(items)
    selected_items = []

    while w > 0 and n > 0:
        item_name, details = item_list[n - 1]
        if dp[n][w] != dp[n - 1][w]:
            selected_items.append(item_name)
            w -= details['cost']
        n -= 1

    return selected_items, dp[-1][-1]

# Виконання жадібного алгоритму
greedy_result, greedy_calories = greedy_algorithm(items, 100)
print("Жадібний алгоритм:", greedy_result, "Калорії:", greedy_calories)

# Виконання алгоритму динамічного програмування
dp_result, dp_calories = dynamic_programming(items, 100)
print("Динамічне програмування:", dp_result, "Калорії:", dp_calories)