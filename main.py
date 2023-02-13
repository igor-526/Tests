input('Задание 1. Для продолжения Enter')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
Russia = []
for visit in geo_logs:
    if list(visit.values())[0][1] == 'Россия':
        Russia.append(visit)

print(Russia)
print()
input('Задание 2. Для продолжения Enter')

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
ids_list = list((ids.values()))
ids_set = set()
for numbers in ids_list:  # знаю, что можно было сделать без цикла с помощью команды объединения множеств, но мой код подойдёт так же на тот случай, если ключей будет не 3, а сколько угодно и называться они будут как угодно
    for number in numbers:
        ids_set.add(number)

print(ids_set)
print()
input('Задание 3. Для продолжения Enter')

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
max_count = 0  # опять хочу выполнить задание не для частного случая и использовать множества и их индексы
data = []
for query in queries:
    if max_count < (len(query.split())):
        max_count = (len(query.split()))
for i in range(0, max_count):
    data.append(0)

for query in queries:
    data[len(query.split()) - 1] += 1

word_counter = 1
for counter in data:
    print(
        f'Поисковых запросов, состоящих из {word_counter} слов: {counter}. Это {(counter * 100 // sum(data))}% от всех поисковых запросов')
    word_counter += 1

print()
input('Задание 4. Для продолжения Enter')

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
data = []
counter = 0
max_stat = 0
max_stat_index = 0
for service in stats:
    data.append([service])
    data[counter].append(stats[service])
    counter += 1

counter = 0
for index, stat in enumerate(data):
    if stat[1] > max_stat:
        max_stat = stat[1]
        max_stat_index = index

print(
    f'Наибольшее количество продаж обеспечил сервис "{data[max_stat_index][0]}"! Всего {data[max_stat_index][1]} продаж!')