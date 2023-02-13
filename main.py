from datafile import geo_logs
from datafile import ids
from datafile import queries
from datafile import stats


def filter_(data):
    russia = []
    for visit in data:
        if list(visit.values())[0][1] == 'Россия':
            russia.append(visit)
    return russia


def unical_ids(data):
    ids_list = list((data.values()))
    ids_set = set()
    for numbers in ids_list:
        for number in numbers:
            ids_set.add(number)
    return ids_set


def words_percent(data_):
    max_count = 0
    data = []
    for query in data_:
        if max_count < (len(query.split())):
            max_count = (len(query.split()))
    for i in range(0, max_count):
        data.append(0)

    for query in data_:
        data[len(query.split()) - 1] += 1

    word_counter = 1
    for counter in data:
        print(
            f'Поисковых запросов, состоящих из {word_counter} слов: {counter}. Это {(counter * 100 // sum(data))}'
            f'% от всех поисковых запросов')
        word_counter += 1


def max_(data_):
    data = []
    counter = 0
    max_stat = 0
    max_stat_index = 0
    for service in data_:
        data.append([service])
        data[counter].append(data_[service])
        counter += 1
    for index, stat in enumerate(data):
        if stat[1] > max_stat:
            max_stat = stat[1]
            max_stat_index = index
    print(
        f'Наибольшее количество продаж обеспечил сервис "{data[max_stat_index][0]}"! '
        f'Всего {data[max_stat_index][1]} продаж!')
    return data[max_stat_index][0]


if __name__ == '__main__':
    input('Задание 1. Для продолжения Enter')
    print(filter_(geo_logs))
    input('\nЗадание 2. Для продолжения Enter')
    print(unical_ids(ids))
    input('\nЗадание 3. Для продолжения Enter')
    words_percent(queries)
    input('\nЗадание 4. Для продолжения Enter')
    max_(stats)
