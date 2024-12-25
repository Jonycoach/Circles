from ДЗ.Grades import my_list

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
c = 0
while c <= len(my_list):
    if (my_list[c]) > 0:
        print(my_list[c])
        c += 1
        if (my_list[c]) == 0:
            c += 1
        continue
    if (my_list[c]) < c:
        break

