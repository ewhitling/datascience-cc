# %% codecell
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %% codecell

sns.set(style="white", palette="muted", color_codes=True)

# generate the random numbers
np.random.seed(4567)
rs = np.random.RandomState(10)

# Set up the matplotlib figure
sns.despine(left=True)

# Generate a random univariate dataset
d = rs.normal(50, 20, size=100)

# Plot a simple histogram with binsize determined automatically
ax = sns.distplot(d, kde=False, color="b")
ax.set(xlabel='Octopus Defense Rating', ylabel='Item Count')

plt.savefig("./output/2-4_defense_histogram.svg", format="svg")

# %% codecell
ax = sns.distplot(d, hist=False, color="g", kde_kws={"shade": True})
ax.set(xlabel='Octopus Defense Rating', ylabel='Probability')
plt.savefig("./output/2-5_defense_kde.svg", format="svg")
