from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from functools import reduce

data = pd.read_csv('files/president_heights.csv')
# print(data)

heights = sorted(np.array(data['height(cm)']))

minValue = min(heights)
maxValue = max(heights)
channelsCount = 5
channelWidth = (maxValue - minValue) / channelsCount + 1


def reducer(acc, val):
  i = len(acc)
  currentMaxValue = minValue + (i) * channelWidth

  print(acc, currentMaxValue, val)

  return acc + [1] if val >= currentMaxValue else acc[:-1] + [acc[i - 1] + 1]


print(heights)

channels = reduce(reducer, heights, [1])
bins = [minValue + (i) * channelWidth for i in range(channelsCount + 1)]
print(channels)
print(bins)

# sns.distplot(bins, bins, channels, kde=False)
plt.hist(bins[:-1], bins, weights=channels)
plt.xticks(bins)
plt.show()
