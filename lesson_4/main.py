import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    #1

    # x = [40, 45, 48, 30, 20, 10, 12, 10, 8, 6, 15, 20]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12]
    # plt.plot(y ,x)
    # plt.show()

    #2

    # categories = ['Shoes', 'Funnies', 'BlaBla']
    # values = [23, 45, 56]
    # plt.bar(categories, values)
    # plt.title('Amount of products')
    # plt.xlabel('Products')
    # plt.ylabel('Amount')
    # plt.show()


    #3
    # x = np.random.rand(50) * 100  # 50 ערכי x אקראיים
    # y = np.random.rand(50) * 10  # 50 ערכי y אקראיים
    # colors = np.random.rand(50) * 10  # 50 צבעים אקראיים
    # sizes = 1000 * np.random.rand(50)
    #
    # plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    # plt.colorbar()  # הצגת סרגל הצבעים
    # plt.title('Grades Of Students')
    # plt.xlabel('Grades')
    # plt.ylabel('Time')
    # plt.show()

    #4
    # ages = [22, 45, 30, 35, 50, 41, 28, 33, 55, 65, 29, 42, 48, 31]
    #
    # plt.hist(ages, bins=[20, 30, 40, 50, 60, 70], edgecolor='black')
    #
    # plt.title('Age Distribution')
    # plt.xlabel('Ages')
    # plt.ylabel('Number of People')
    # plt.show()

    #5
    years = range(2010, 2021)
    consumption_oil = [100, 105, 110, 120, 125, 130, 135, 140, 145, 150, 155]
    consumption_gas = [80, 82, 85, 88, 90, 95, 100, 105, 110, 115, 120]
    consumption_renewable = [20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]

    fig, axs = plt.subplots(2, 2)  # יוצר מטריצה של גרפים בגודל 2x2
    axs[0, 0].plot(consumption_renewable, 'tab:blue')
    axs[0, 0].set_title('One')
    axs[0, 1].plot(consumption_gas, 'tab:red')
    axs[0, 1].set_title('Tow')
    # axs[1, 0].scatter(consumption_oil, 'tab:yellow')
    # axs[1, 0].set_title('Three')

    # התאמת הגרפים למראה נקי יותר
    for ax in axs.flat:
        ax.label_outer()
    plt.show()