import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(style="ticks")

# 有一套的参数可以控制绘图元素的比例。
# 首先，让我们通过set()重置默认的参数：
# set( )通过设置参数可以用来设置背景，调色板等，更加常用。
# 有五种seaborn的风格，它们分别是：darkgrid, whitegrid, dark, white, ticks。它们各自适合不同的应用和个人喜好。默认的主题是darkgrid。

df = sns.load_dataset("anscombe")
df.head()