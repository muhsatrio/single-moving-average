import csv
import math
import matplotlib.pyplot as plt

data = []
ma = []
se = []
# pe = []

def countSquareError(data, ma, t):
    # print("Menghitung Square Error: ")
    for i in range(0,t):
        se.append(0)
    length = len(data)
    for i in range(t, length):
        se.append((data[i]-ma[i])**2)
    i = 1
    # for row in se:
    #     print("{} - {}".format(i,row))
    #     i = i + 1
    # print("========================")

def countMovingAverage(data, t):
    # print("Menghitung Single Moving Average")
    for i in range(0,t):
        ma.append(0)
    length = len(data)
    for i in range(t, length+1):
        ma.append((data[i-1]+data[i-2]+data[i-3])/t)
    i = 1
    # for row in ma:
    #     print("{} - {}".format(i, row))
    #     i = i + 1
    # print("========================")

def importData(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            data.append(row[0])
    # print("Mengimport Data")
    # i = 1
    # for row in data:
    #     print("{} - {}".format(i, row))
    #     i = i + 1
    # print("========================")

if __name__=="__main__":
    t = 3
    importData("databeras.csv")
    countMovingAverage(data, t)
    countSquareError(data, ma, t)
    # countPercentageError(data, ma, t)
    sse = sum(se)
    mse = sse/(len(se) - 3)
    rmse = math.sqrt(mse)
    print("Prediksi Harga Beras Bulan November 2018",ma[-1])
    print("SSE: ",sse)
    print("MSE: ",mse)
    print("RMSE: ", rmse)
    plt.plot(data, label="Real Data")
    plt.plot(ma, label="Forecasting Prediction")
    plt.legend(loc='lower left')
    plt.title("Prediksi Harga Beras November 2018", fontsize=14, fontweight='bold')
    plt.suptitle("Dataset: Januari 2016 - Oktober 2018", fontsize=10)
    plt.show()
    