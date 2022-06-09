# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

a = int(input("a:= "))
for row in range(1, a+1):
    if (row == 1) or (row == a):
        print("#"*a)
    else:
        print('#' + ' '*(row-2) + '#' + ' '*(a-row-1) + "#")
