list = []


def make_list(list):
    for i in range(0, 3):
        num = input("Enter a number: ")
        num = int(num)
        list.append(num)
    if type(num) != int:
        raise ValueError('not a number')
    return list


if __name__ == '__main__':
    list = make_list(list)
    print(list)