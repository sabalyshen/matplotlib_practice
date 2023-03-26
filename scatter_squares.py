import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.magma, s=40)
#s=100調整點的大小,edgecolor='none'刪掉邊匡（默認值就是沒邊匡）,c='red'設定顏色
#RGB顏色定義0~1,接近0顏色深,c=(0, 0, 0.8)
#cmap=plt.cm.magma,.magma 可以上網查colormap
#設置圖表標題並給座標軸加上標籤
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

#設置刻度標記的大小
#.axis x,y的範圍
plt.axis([0, 1100, 0, 1100000])
plt.show()
'''
若要自動保存圖表
plt.savefig('squares_plt.png', bbox_inches='tight')
第一個實參代表儲存的檔名
第二個指定將多餘空白處刪掉
'''