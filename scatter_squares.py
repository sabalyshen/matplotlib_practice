import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)
#s=100調整點的大小
#設置圖表標題並給座標軸加上標籤
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

#設置刻度標記的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()