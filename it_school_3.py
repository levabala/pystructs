from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('files/prog1_input.csv')
views = np.sort(np.array(data['views']))
downloads = np.sort(np.array(data['downloads']) * 100)

reg = linear_model.LinearRegression()
views_train = views[:, np.newaxis]
downloads_train = downloads[:, np.newaxis]

reg.fit(views_train, downloads_train)

y_pred = reg.predict(views_train)

print(reg.coef_)
print(reg.intercept_)
print(y_pred)

plt.plot(views, downloads, 'g')
plt.plot(views, y_pred, 'b')

plt.show()
