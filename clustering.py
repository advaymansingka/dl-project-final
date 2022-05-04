import numpy as np
import csv
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.mixture import GaussianMixture
from joblib import dump, load


def main():

    train = False

    with open('DL_wiki_2.csv', 'r') as f:
        data = list(csv.reader(f, delimiter=","))
 
    data = np.array(data)

    if train:
        gm = GaussianMixture(n_components=5, random_state=0, verbose=2).fit(data)
        dump(gm, 'gaussian_test.joblib')

    else:
        print(data.shape)
        # gm = load('gaussian_test.joblib') 
        # predictions = gm.predict(data)
        # plt.plot(predictions[0:1000])
        # plt.show()


if __name__ == "__main__":
    main()