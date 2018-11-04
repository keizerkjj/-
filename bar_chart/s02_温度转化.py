
import numpy as np

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/temp.csv'



time_in_min_com = []
data_arr = np.loadtxt(data_path, delimiter=',', dtype='str', skiprows=1)

tem_col = data_arr[:,1]
tem_in_c = np.core.defchararray.replace(tem_col,' C','')
tem_in_f = tem_in_c.astype('float')*1.8+32

print('这是摄氏度：{}'.format(tem_in_c))
print('这是华氏度：{}'.format(tem_in_f))

