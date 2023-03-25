import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
#設定線條粗細（linewidth）
plt.plot(squares, linewidth=5)
#設置圖表標題，x,y軸的的標籤
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

#設置刻度標記的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()