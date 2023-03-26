import matplotlib.pyplot as plt
#設定x,y軸的值
x_label = list(range(1, 5001))
y_label = [x**3 for x in x_label]

#設定美的點的大小、顏色、位子
plt.scatter(x_label, y_label,c=y_label, cmap=plt.cm.RdYlGn, s=40)
#設定圖表名稱、x,y軸的名稱
plt.title("立方計算", fontsize= 18)
plt.xlabel("x軸", fontsize=14)
plt.ylabel("y軸", fontsize=14)

#設定x,y軸的起始值
plt.axis([0, 5000, 0, 125e9])
plt.show()