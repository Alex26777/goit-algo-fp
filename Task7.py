import random
import matplotlib.pyplot as plt

# Функція для симуляції кидання двох кубиків
def roll_dice(num_rolls):
    counts = {total: 0 for total in range(2, 13)}  # Словник для зберігання кількості кожної суми
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)  # Сума двох кубиків
        counts[roll] += 1
    return counts

# Кількість симуляцій
num_rolls = 1000000

# Виконання симуляції
roll_results = roll_dice(num_rolls)

# Обчислення імовірностей для кожної суми
probabilities = {total: count / num_rolls for total, count in roll_results.items()}

# Виведення результатів у вигляді таблиці
print("Сума", "Імовірність", sep='\t')
for total in range(2, 13):
    print(total, f"{probabilities[total]:.2%}", sep='\t')

# Створення графіка
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='skyblue')
plt.xlabel('Сума кидка')
plt.ylabel('Імовірність')
plt.title('Імовірності суми при киданні двох кубиків (Метод Монте-Карло)')
plt.xticks(range(2, 13))
plt.show()
