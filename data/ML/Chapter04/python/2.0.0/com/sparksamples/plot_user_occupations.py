import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from util import get_user_data


def main():
    # get user data
    user_data = get_user_data()
    # extract occupation
    user_occ = user_data.groupby("occupation").count().collect()
    # extract list of tuple occupation by length    
    # user_occ_list = map(lambda x: (x.occupation, x.__getattr__('count')), user_occ)
    user_occ_list = [(x.occupation, x.__getattr__('count')) for x in user_occ]
    x_axis1 = np.array([c[0] for c in user_occ_list])
    y_axis1 = np.array([c[1] for c in user_occ_list])
    sorted_ind = np.argsort(y_axis1)
    x_axis = x_axis1[sorted_ind]    
    y_axis = y_axis1[sorted_ind]

    pos = np.arange(len(x_axis))
    width = 1.0

    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(x_axis)

    plt.bar(pos, y_axis, width, color='lightblue')
    plt.xticks(rotation=45, fontsize='9')
    plt.gcf().subplots_adjust(bottom=0.15)
    #fig = matplotlib.pyplot.gcf()


    plt.show()



if __name__ == "__main__":
    main()