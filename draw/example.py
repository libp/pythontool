import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# refer
# https://zhuanlan.zhihu.com/p/139052035

def drawpic1():
    fig=plt.figure(num=1,figsize=(4,4))
    plt.plot([1,2,3,4],[1,2,3,4])
    plt.show()

def drawpic2():
    fig=plt.figure(num=1,figsize=(4,4))
    ax=fig.add_subplot(111)
    ax.plot([1,2,3,4],[1,2,3,4])
    plt.show()

def drawpic3():
    fig=plt.figure(num=1,figsize=(4,4))
    plt.subplot(111)
    plt.plot([1,2,3,4],[1,2,3,4])
    plt.show()



if __name__ == '__main__':
    drawpic3()