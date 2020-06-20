list = []
def get_input():
    pass

def make_list(list):
    for i in range(0, 3):

        num = int(input("Enter a number: "))
        list.append(num)

    if not type(num) is int:
        raise ValueError('not a number')

    return list


if __name__ == '__main__':
    list = make_list(list)
    print(list)







