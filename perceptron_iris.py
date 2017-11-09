import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from mylib.perceptron import Perceptron, np

style.use('seaborn-talk')

# krfont = {'family':'NanumGothic', 'weight':'bold', 'size':10}
# matplotlib.rc('font', **krfont)
# matplotlib.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':

    style.use('seaborn-talk')

    df = pd.read_csv('iris.data', header=None)

    y = df.iloc[0:100, 4].values
    y = np.where(y=='Iris-setosa', -1, 1)
    X = df.iloc[0:100, [0, 2]].values

    plt.scatter(X[:50, 0], X[:50, 1], color='r', marker='o', label='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='b', marker='x', label='versicolor')
    plt.xlabel('꽃잎 길이(cm)')
    plt.ylabel('꽃받침 길이(cm)')
    plt.legend(loc=4)
    plt.show()

    ppn1 = Perceptron(eta=0.1)
    ppn1.fit(X, y)
    print(ppn1.errors_)