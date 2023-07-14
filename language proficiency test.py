from random import choice

en_dict = {
    'машина': 'car',
    'зеленый': 'green',
    'синий': 'blue',
    'ребенок': 'child',
    'девочка': 'girl',
    'человек': 'human',
    'жизнь': 'life',
    'мужчина': 'man',
    'женщина': 'woman',
    'молодежь': 'yourh',
    'имя': 'name',
    'семья': 'family',
    'родители': 'parents',
    'мама': 'mother',
    'папа': 'father',
    'жена': 'wife',
    'муж': 'husband',
    'возраст': 'age',
    'лицо': 'face',
    'кость': 'bone',
    'глаз': 'eye',
    'волосы': 'hair',
    'череп': 'skull',
    'рука': 'hand',
}
ru_dict = dict(zip(en_dict.values(), en_dict.keys()))


def en_to_ru(en_dict, ru_dict):
    qst_dict = en_dict.copy()
    i = 0
    response_counter = 0
    while i != 10:
        question = qst_dict.get(choice(list(qst_dict)))
        answer = input(f'{question}\nответ:')
        if en_dict.get(answer, '') == question:
            response_counter += 1
        qst_dict.pop(ru_dict[question])
        i += 1
    return response_counter


def ru_to_en(ru_dict, en_dict):
    qst_dict = ru_dict.copy()
    i = 0
    response_counter = 0
    while i != 10:
        question = qst_dict.get(choice(list(qst_dict)))
        answer = input(f'{question}\nответ:')
        if ru_dict.get(answer, '') == question:
            response_counter += 1
        qst_dict.pop(en_dict[question])
        i += 1
    return response_counter


c = input("Выберете тест 1-2:\n"
          "1) Русские слова\n"
          "2) Английские слова")


if c == '1':
    ru = ru_to_en(ru_dict, en_dict)
    print(f"Правильных ответов: {ru}")
elif c == '2':
    en = en_to_ru(en_dict, ru_dict)
    print(f"Правильных ответов: {en}")
else:
    print("Неизвестный выбор")
