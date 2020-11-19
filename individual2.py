if __name__ == '__main__':
    p = input("Введите предложение: ")
    a = p.find('чу')
    b = p.find('щу')
    if a < b:
        print(a)
    else:
        print(b)
