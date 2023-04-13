import csv


def read_csv_file(file_path):
    """Функція, що зчитує csv файл і повертає список рядків"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def create_category_brand_index(rows):
    """Функція, що створює словник індексу за категоріями та брендами"""
    index = {'categories': {}, 'brands': {}}
    for row in rows:
        # Додаємо до словника index
        category = row['category']
        brand = row['brand']
        if category not in index['categories']:
            index['categories'][category] = []
        index['categories'][category].append(row)
        if brand not in index['brands']:
            index['brands'][brand] = []
        index['brands'][brand].append(row)
    return index


def print_brand_category_statistics(index):
    """Функція, що виводить статистику за категоріями та брендами"""
    print('Статистика по брендам:')
    for brand, items in index['brands'].items():
        print(f'Від бренду "{brand}" є {len(items)} товарів')
    print('\nСтатистика по категоріям:')
    for category, items in index['categories'].items():
        print(f'Серед категорії "{category}" є {len(items)} товарів')


def print_selected_items_by_category_brand(index, category_name, brand_name):
    """Функція, що виводить інформацію про товари від обраного бренду та категорії"""
    print(f'\nКатегорія "{category_name}" та бренд "{brand_name}":')
    for item in index['categories'][category_name]:
        if item['brand'] == brand_name:
            print(item)


def print_brand_distribution_by_category(index):
    """Функція, що виводить розподіл товарів по брендам для кожної категорії"""
    for category, items in index['categories'].items():
        brand_count = {}
        for item in items:
            brand = item['brand']
            if brand not in brand_count:
                brand_count[brand] = 0
            brand_count[brand] += 1
        print(f'У категорії "{category}" представлені товари таких брендів: {brand_count}')


if __name__ == '__main__':
    file_path = 'tech_inventory.csv'
    rows = read_csv_file(file_path)
    index = create_category_brand_index(rows)
    print_brand_category_statistics(index)
    print_selected_items_by_category_brand(index, 'Smartphones', 'Samsung')
    print()
    print_selected_items_by_category_brand(index, 'Computer Mouse', 'Logitech')
    print()
    print_brand_distribution_by_category(index)