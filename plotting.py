from util import *
# import numpy as np
import mpld3
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import SGDRegressor
# from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x_train, y_train, month, temp, humidity, year = load_data()
# x_train, y_train = data_load()

# def train_and_plot():
def render_plot(fg):
    html_str = mpld3.fig_to_html(fg)
    Html_file= open("plots.html","w")
    Html_file.write(html_str)
    Html_file.close()
# rf_model = RandomForestRegressor()
# rf_model.fit(x_train.values,y_train)
# print(y_train)
# print(x_train)
# scl = StandardScaler()
# x_n = scl.fit_transform(x_train)
# sgr = LinearRegression()
# sgr = SGDRegressor(max_iter=1000000)
# sgr.fit(x_train,y_train)

# b_n = sgr.intercept_
# w_n = sgr.coef_

# inp_tst = np.array([6,1,20.08,82.31,12.02])
# inp_tst = inp_tst.reshape(1,-1)
# inp_tst = scl.fit_transform(inp_tst)
# print('Rainfall = ',sgr.predict(inp_tst))


def year_plot():
    plt.scatter(year, y_train, color='red', marker='*')
    plt.bar(year, y_train, color='green')
    plt.xlabel('Year')
    plt.ylabel('Rainfall')
    fg = plt.figure()
    # render_plot(fg)
    # plt.show()
    return mpld3.fig_to_html(fg)


def month_plot():
    plt.scatter(month, y_train, color='red', marker='*')
    plt.bar(month, y_train)
    plt.xlabel('Month')
    plt.ylabel('Rainfall')
    fg = plt.figure()
    render_plot(fg)
    plt.show()


def temp_plot():
    plt.scatter(temp, y_train, color='blue', marker='*')
    plt.plot(temp, y_train, color='green')
    plt.xlabel('Temperature')
    plt.ylabel('Rainfall')
    fg = plt.figure()
    render_plot(fg)
    plt.show()


def humidity_plot():
    plt.scatter(humidity, y_train, marker='*')
    plt.hist2d(humidity, y_train)
    # ax = plt.axes()
    # ax.set_facecolor('black')
    plt.xlabel('Humidity')
    plt.ylabel('Rainfall')
    fg = plt.figure()
    render_plot(fg)
    plt.show()

    # print('\n\n\n\nRainfall = ',rf_model.predict(inp_tst)[0])
    # print('\n\n\n\n')
    # print('Rnf = ', np.dot(inp_tst,w_n)+b_n)

# train_and_plot()
# year_plot()