def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str
import re
file = open("test2.txt", "r")
k = 5
last_int_max = int(0)
print('Натуральные числа, у которых более', k, 'цифр:')
char = file.read()
file.close()
all = re.findall(r'\b\d{5,}\b', char)
symbolall = 0
for i in range(len(all)):
    chislo = int(all[i])
    if (chislo > last_int_max):
        last_int_max = chislo
    symbolall += 1
    print(all[i])
print("Всего чисел, содержащих более",k,"цифр -", symbolall,"\n","\nМаксимальное число -", last_int_max)
slovar = {"0": "ноль ", "1": "один ", "2": "два ", "3": "три ", "4": "четыре ", "5": "пять ", "6": "шесть ", "7": "семь ", "8": "восемь ", "9": "девять "}
print(multiple_replace(str(last_int_max), slovar))