def run():
    # for counter in range(1000):
    #     if counter % 2 != 0:
    #         continue
    #     print(counter)

    # for i in range(1000):
    #     print(i)
    #     if i == 562:
    #         break

    text = input('Escribe un texto: ')
    for i in text:
        if i == 'o':
            break
        print(i)


if __name__ == '__main__':
    run()