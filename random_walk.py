from random import choice

class RandomWalk():
    """生成一個產生隨機座標的類"""
    
    def __init__(self, num_points=5000):
        #設定num_point的默認值5000
        self.num_points = num_points
        
        #所有隨機座標起始在(0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """生成座標"""
        #不斷漫步，直到指定長度
        while len(self.x_values) < self.num_points:
            #決定前進方向及前近距離
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction
            
            #避免原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            #self.x_values[-1]，將x_values最後一個直加上新的座標
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            