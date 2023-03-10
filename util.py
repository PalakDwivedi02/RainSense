import numpy as np
import pandas as pd


def data_load():
    data = np.loadtxt('Rnf.txt', delimiter=',')
    x = data[:, 1:6]
    y = data[:, 6]
    # y = (np.rint(y)).astype(int)
    return x, y


def load_data():
    data = pd.read_csv('Rainfall_data.csv')
    x = data.drop(['Year', 'Precipitation'], axis=1)
    y = data['Precipitation']
    m = data['Month']
    tmp = data['Temperature']
    humidity = data['Relative Humidity']
    yr = data['Year']
    return x, y, m, tmp, humidity, yr


def specific_humidity(rh, temp):
    """
    Calculates the specific humidity from relative humidity and temperature.

    Parameters:
    rh (float): Relative humidity expressed as a decimal fraction (e.g. 0.5 for 50% RH).
    temp (float): Temperature in Celsius.

    Returns:
    sh (float): Specific humidity in kg/kg.
    """
    # Calculate saturation vapor pressure at temperature
    es = 6.112 * np.exp(17.67 * temp / (temp + 243.5))

    # Calculate vapor pressure from relative humidity
    e = rh * es

    # Calculate specific humidity
    sh = 1000 * 0.622 * e / (1013.25 - 0.378 * e)

    return sh
