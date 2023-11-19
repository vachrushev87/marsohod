# Импорт системной библиотеки,
# при помощи которой будем считывать данные из стандартного потока ввода.
import sys


def main():
    # Прочитали первую строку, в которой указано количество строк,
    # преобразовали в число:
    elements_count = int(sys.stdin.readline().rstrip())
    marsohoda = [None] * elements_count
    # массив куда запишем все данные с массива marsohoda,
    # дублирующие значения уже будут заменены "_"
    duplicates = []
    # сюда запишем в будующем все элементы "_"
    itog = []

    # Читаем следующие строки ввода:
    for index in range(elements_count):
        marsohoda[index] = sys.stdin.readline().rstrip()

    for i in marsohoda:

    # Если значение повторяется но не записано в duplicates, то запишем его
        if marsohoda.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    # Если значение уже присутвует duplicates за место него запишем "_",
    # также запишем его в массив itog
        elif i in duplicates:
            duplicates.append('_')
            itog.append('_')
    # Во всех остальных случаях запишем значение в массив duplicates
        else:
            duplicates.append(i)

    # переведем список в множество, тем самым избавимся от дубликатов
    sett = set(duplicates)
    # переведем обратно в список
    marsohoda = list(sett)

    # Применяем к списку функцию enumerate(), итерируемся
    # по полученному объекту enumerate и распаковываем его кортежи:
    # в переменную index сохраняем индекс элемента, в item - его значение.
    for index, item in enumerate(marsohoda):
    # Если в значении символ "_" то удалим его
        if item == '_':
            del marsohoda[index]

    # Отсортируем наш массив от меньшего к большему
    marsohoda.sort()
    # в конец массива допишем "_" которые были записаны в массив itog
    marsohoda.extend(itog)
    # выведем наш результат
    print(*marsohoda)


if __name__ == '__main__':
    main()
