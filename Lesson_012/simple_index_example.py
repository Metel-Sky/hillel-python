# индекс - это нахождение всех уникальных значений в одной колонке и реализация быстрого поиска всех записей
# по этим значениям
import json


if __name__ == '__main__':
    d = json.load(open('children.json', 'r'))
    print(d)
    children_data = d['children']
    # ключами индекса по колонке возраст будут значения возрастов
    age_index = dict()
    for children in children_data:
        if children['age'] not in age_index:
            age_index[children['age']] = list()
        age_index[children['age']].append(children)
    print(age_index)