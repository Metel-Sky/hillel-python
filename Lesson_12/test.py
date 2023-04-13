import csv

filename = "tech_inventory.csv"

# Створення словника з категоріями та брендами
category_index = {}
brand_index = {}

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Додавання до словника з категоріями
        category = row["category"]
        if category not in category_index:
            category_index[category] = [row]
        else:
            category_index[category].append(row)

        # Додавання до словника з брендами
        brand = row["brand"]
        if brand not in brand_index:
            brand_index[brand] = [row]
        else:
            brand_index[brand].append(row)

# Виведення статистики по брендам та категоріям
print("Статистика по брендам:")
for brand, products in brand_index.items():
    print(f"- Від бренду \"{brand}\" є {len(products)} товарів")

print("\nСтатистика по категоріям:")
for category, products in category_index.items():
    print(f"- Серед категорії \"{category}\" є {len(products)} товарів")

# Виведення повної інформації про товари вибраного бренду та категорії
selected_brand = "Samsung"
selected_category = "Smartphones"

print(f"\nІнформація про товари бренду \"{selected_brand}\":")
for product in brand_index[selected_brand]:
    print(product)

print(f"\nІнформація про товари категорії \"{selected_category}\":")
for product in category_index[selected_category]:
    print(product)

# Розподіл товарів по брендам для кожної категорії
print("\nРозподіл товарів по брендам для кожної категорії:")
for category, products in category_index.items():
    brand_count = {}
    for product in products:
        brand = product["brand"]
        if brand not in brand_count:
            brand_count[brand] = 1
        else:
            brand_count[brand] += 1
    print(f"У категорії \"{category}\" представлені товари таких брендів: {brand_count}")
