import numpy as np
import copy
import time

DP_dict={}
route=[]
real_sol=[]
data_length=0
data_int=[]
#讀檔
def readfile(file):
	j=0;
	i=0;
	global data_length


	f=open(file,mode='r');
	data_str=f.readlines()  #逐行讀取txt並存成list。每行是list的一個元素，資料型別為str
	f.close();

	#算出有幾個城市
	data_length=len(data_str); 
	
	#把資料轉成int，存到data_int
	for i in range(data_length): 
		for j in range(len(list(data_str[0].split()))):
			data_int.append(int(data_str[i].split(' ')[j]));

	#把data_int轉成二維的
	city=np.zeros((data_length,3));
	for i in range(data_length):
		for j in range(3):
			city[i][j]=data_int[i*3+j];

	#算出個城市之間的距離
	cost=np.zeros((data_length,data_length));
	for i in range(data_length):
		for j in range(i+1,data_length):
			cost[i][j]=pow(pow((city[i][1]-city[j][1]),2)+pow((city[i][2]-city[j][2]),2),0.5);
			cost[j][i]=cost[i][j];

	#做Dynamic Prgramming會用到的陣列，城市1當起點
	for i in range(1, data_length):
		DP_dict[i+1,()] = cost[i][0] 

	return city,cost

#Dynamic Programming
def DP(node, subset):
	if (node, subset) in DP_dict:
		return DP_dict[node, subset] #有存在這個組合就回傳
	
	values = []
	all_min = []

	for i in subset:
		set_tmp = copy.deepcopy(list(subset))#做一個subset的複製品
		set_tmp.remove(i) #遍歷每個城市當頭
		all_min.append([i, tuple(set_tmp)]) #把當下的組合存起來
		result = DP(i, tuple(set_tmp)) # set_tmp這個組合的最小路徑
		values.append(cost[node-1][i-1] + result) # result+這個recursive的起始城市的路徑長度存下來



	DP_dict[node, subset] = min(values) #選出最小路徑，存在DP_dict[]

	route.append(((node, subset), all_min[values.index(DP_dict[node, subset])])) #存最小路徑的組合

	return DP_dict[node, subset]

#輸出路徑
def findroute():
	#把經過的城市一個一個找到
	solution = route.pop() 
	real_sol.append(1)#real_sol是城市的順序，城市1是起點
	real_sol.append(solution[1][0])#solution[1][0]是城市1的下一個要經過的城市
	for x in range(data_length - 2):
		for new_solution in route: #找下一個城市
			if tuple(solution[1]) == new_solution[0]:
				solution = new_solution
				real_sol.append(solution[1][0])
				break
	real_sol.append(1) #回到城市1

	print("Best Visit Order: ",end='')
	for i in range(data_length+1):
		print(data_int[(real_sol[i]-1)*3],' ',end='') #修正城市的編號

	print('\n',end='')

	print("Best Distance： ",DP_dict[1, tuple(subset)])


#把答案存起來
def writefile(city,real_sol):
	f_draw = open('draw.txt', 'w')
	f_output = open('output.txt','w')
	for i in range(data_length+1):
		print(int(city[real_sol[i]-1][1]),'', end='',file=f_draw)
		print(int(city[real_sol[i]-1][2]),file=f_draw)
	print("Best Visit Order: ",end='',file=f_output)
	for i in range(data_length+1):
		print(data_int[(real_sol[i]-1)*3],' ',end='',file=f_output)
	print('\n',end='',file=f_output)
	print("Best Distance： ",DP_dict[1, tuple(subset)],file=f_output)
	print("Execution Time: ",time.time()-start_time," (s)",file=f_output)
	f_draw.close()
	f_output.close()

if __name__=='__main__':

	start_time=time.time()
	file = 'readfile.txt'
	city,cost=readfile(file)#讀檔

	subset=[]

	#做一個子集合[2,3,4,5.....end]
	for i in range(2,data_length+1):
		subset.append(i)

	#Dynamic Programming
	DP(1, tuple(subset))

	#輸出路徑
	findroute()

	#寫入檔案
	writefile(city,real_sol)
	print("Execution Time: ",time.time()-start_time," (s)")




