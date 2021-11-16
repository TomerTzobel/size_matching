# import numpy as np
# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt


# def estimate_coef(x, y):
#     # number of observations/points
#     n = np.size(x)
#
#     # mean of x and y vector
#     m_x = np.mean(x)
#     m_y = np.mean(y)
#
#     # calculating cross-deviation and deviation about x
#     SS_xy = np.sum(y * x) - n * m_y * m_x
#     SS_xx = np.sum(x * x) - n * m_x * m_x
#
#     # calculating regression coefficients
#     b_1 = SS_xy / SS_xx
#     b_0 = m_y - b_1 * m_x
#
#     return (b_0, b_1)
#
#
# def plot_regression_line(x, y, b):
#     # plotting the actual points as scatter plot
#     plt.scatter(x, y, color="m",
#                 marker="o", s=30)
#
#     # predicted response vector
#     y_pred = b[0] + b[1] * x
#
#     # plotting the regression line
#     plt.plot(x, y_pred, color="g")
#
#     # putting labels
#     plt.xlabel('x')
#     plt.ylabel('y')
#
#     # function to show plot
#     plt.show()
#
# # observations / data
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
#
# # estimating coefficients
# b = estimate_coef(x, y)
# print("Estimated coefficients:\nb_0 = {}  \
# \nb_1 = {}".format(b[0], b[1]))
#
# # plotting regression line
# plot_regression_line(x, y, b)
# print("test")


# # Load the diabetes dataset
# diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
#
# # Use only one feature
# diabetes_X = diabetes_X[:, np.newaxis, 2]
#
# # Split the data into training/testing sets
# diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]
#
# # Split the targets into training/testing sets
# diabetes_y_train = diabetes_y[:-20]
# diabetes_y_test = diabetes_y[-20:]
#
# # Create linear regression object
# regr = linear_model.LinearRegression()
#
# # Train the model using the training sets
# regr.fit(diabetes_X_train, diabetes_y_train)
#
# # Make predictions using the testing set
# diabetes_y_pred = regr.predict(diabetes_X_test)
#
# # The coefficients
# print("Coefficients: \n", regr.coef_)
# # The mean squared error
# print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# # The coefficient of determination: 1 is perfect prediction
# print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))
#
# # Plot outputs
# plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
# plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()