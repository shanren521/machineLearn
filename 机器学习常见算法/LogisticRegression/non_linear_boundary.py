import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from logistic_regression import LogisticRegression

data = pd.read_csv("../data/microchips-tests.csv")

# 类别标签
validities = [0, 1]

# 选择两个特征
x_axis = 'param_1'
y_axis = 'param_2'

# 散点图
for validity in validities:
    plt.scatter(
        data[x_axis][data['validity'] == validity],
        data[y_axis][data['validity'] == validity],
        label=validity
    )

plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title("Microchip Test")
plt.legend()
plt.show()

num_examples = data.shape[0]
x_train = data[[x_axis, y_axis]].values.reshape((num_examples, 2))
y_train = data['validity'].values.reshape((num_examples, 1))

# 训练参数
max_iterations = 100000
regularization_param = 0
polynomial_degree = 5
sinusoid_degree = 0

# 逻辑回归
logistic_regression = LogisticRegression(x_train, y_train, polynomial_degree, sinusoid_degree)

# 训练
(theta, costs) = logistic_regression.train(max_iterations)

columns = []
for theta_index in range(0, theta.shape[1]):
    columns.append('Theta ' + str(theta_index))

# 训练结果
labels = logistic_regression.unique_labels

plt.plot(range(len(costs[0])), costs[0], label=labels[0])
plt.plot(range(len(costs[1])), costs[1], label=labels[1])
plt.xlabel('Gradient Steps')
plt.ylabel('Cost')
plt.legend()
plt.show()

# 预测
y_train_prediction = logistic_regression.predict(x_train)

# 准确率
precision = np.sum(y_train_prediction == y_train) / y_train.shape[0] * 100

print("Training Precision: ", precision)

samples = 150
x_min = np.min(x_train[:, 0])
x_max = np.max(x_train[:, 0])
y_min = np.min(x_train[:, 1])
y_max = np.max(x_train[:, 1])

X = np.linspace(x_min, x_max, samples)
Y = np.linspace(y_min, y_max, samples)
Z = np.zeros((samples, samples))

# 结果展示
for x_index, x in enumerate(X):
    for y_index, y in enumerate(Y):
        data = np.array([[x, y]])
        Z[x_index][y_index] = logistic_regression.predict(data)[0][0]

positive = (y_train == 1).flatten()
negative = (y_train == 0).flatten()

plt.scatter(x_train[negative, 0], x_train[negative, 1], label='0')
plt.scatter(x_train[positive, 0], x_train[positive, 1], label='1')

plt.contour(X, Y, Z)
plt.show()


