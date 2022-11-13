def get_unique_list_numbers() -> list[int]:
    list_ = []
    a = 0
    while (a < 15):
        import random
        beg = -10
        end = 10
        item = random.randint(-10, 10)
        if item not in list_:
            list_.append(item)
            a += 1
            return(list_)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
