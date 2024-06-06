import timeit
import matplotlib.pyplot as plt
from random import randint
from lab_1.binary_tree_class import *


def setup_data(n=50, max_height=7, min_height=0, max_root=10**6, min_root=0) -> list:
    data = [(0, 0)] * n
    with open('data.txt', 'w') as fp:
        for i in range(n):
            data[i] = (randint(min_height, max_height), randint(min_root, max_root))
            fp.write(str(data[i]) + '\n')
    return fp.name


def calculate_time(func, max_height=10, n=50, rand_data=True) -> float:
    if rand_data:
        file = setup_data(n, max_height)
    else:
        file = setup_data(n=n, max_height=max_height, min_height=max_height, max_root=47882, min_root = 47882)
    data = []
    with open(file) as fp:
        for i in fp:
            pair = i.strip().replace("(", "").replace(")", "").split(',')
            data.append((int(pair[0]), int(pair[1])))
    delta = 0
    for n in data:
        start_time = timeit.default_timer()
        func(n[0], n[1])
        delta += timeit.default_timer() - start_time
    return delta


def main():
    # pass
    plt.figure(3)
    res_rec_time = []
    res_time = []
    for n in range(0, 1000, 10):
        res_rec_time.append(calculate_time(gen_rec_bin_tree, n=2, max_height=14, rand_data=False))
        res_time.append(calculate_time(generate_binary_tree, n=2, max_height=14, rand_data=False))

    plt.plot(res_time, label='10 измерений, количество итераций растет линейно', color = 'red')
    plt.plot(res_rec_time, label='10 измерений, количество итераций растет линейно', color='blue')
    plt.xlabel('Ось Номер эксперимента')
    plt.ylabel('Ось Время, c')


    # plt.figure(1)
    # res_time = []
    # for n in range(0, 1000, 10):
    #     res_time.append(calculate_time(generate_binary_tree, n=n))
    # plt.plot(res_time, label='10 измерений, количество итераций растет линейно')
    # plt.xlabel('Ось Номер эксперимента')
    # plt.ylabel('Ось Время, c')
    plt.show()
    res_time2 = []
    x_res = []
    plt.figure(2)
    # for i in range(0, 18):
    #     res_time2.append(calculate_time(generate_binary_tree, max_height=i, rand_data=False, n=10))
    #     x_res.append(i)
    # plt.xlabel('Ось Номер эксперимента')
    # plt.ylabel('Ось Время, c')
    # plt.plot(res_time2, label='Зависимость времени от высоты.')
    # plt.show()


if __name__ == "__main__":
    main()
