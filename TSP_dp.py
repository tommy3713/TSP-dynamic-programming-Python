import numpy as np
import copy
import time

DP_dict={}
route=[]
real_sol=[]
data_length=0
data_int=[]
#read file
def readfile(file):
	j=0;
	i=0;
	global data_length


	f=open(file,mode='r');
	data_str=f.readlines()  #read each line of txt and store it into list. Each element's data type is string.
	f.close();

	#calculate the number of cities
	data_length=len(data_str); 
	
	#change data type into int(data_int)
	for i in range(data_length): 
		for j in range(len(list(data_str[0].split()))):
			data_int.append(int(data_str[i].split(' ')[j]));

	#change data_int into two dimension
	city=np.zeros((data_length,3));
	for i in range(data_length):
		for j in range(3):
			city[i][j]=data_int[i*3+j];

	#calculate each distance from different cities
	cost=np.zeros((data_length,data_length));
	for i in range(data_length):
		for j in range(i+1,data_length):
			cost[i][j]=pow(pow((city[i][1]-city[j][1]),2)+pow((city[i][2]-city[j][2]),2),0.5);
			cost[j][i]=cost[i][j];

	#create a dictionary for dynamic programming
	for i in range(1, data_length):
		DP_dict[i+1,()] = cost[i][0] 

	return city,cost

#Dynamic Programming
def DP(node, subset):
	if (node, subset) in DP_dict:
		return DP_dict[node, subset] #if it exist, then return.
	
	values = []
	all_min = []

	for i in subset:
		set_tmp = copy.deepcopy(list(subset))
		set_tmp.remove(i) #go through all cities
		all_min.append([i, tuple(set_tmp)]) #store the combination
		result = DP(i, tuple(set_tmp)) # set_tmp's smallest distance
		values.append(cost[node-1][i-1] + result) # result+ this recursive's starting city's distance



	DP_dict[node, subset] = min(values) #pick the smallest one

	route.append(((node, subset), all_min[values.index(DP_dict[node, subset])])) #store the smallest distance

	return DP_dict[node, subset]

#output route
def findroute():
	#go through all cities
	solution = route.pop() 
	real_sol.append(1)#city one is the starting point
	real_sol.append(solution[1][0])#solution[1][0]is the next city of city 1
	for x in range(data_length - 2):
		for new_solution in route: #find next city
			if tuple(solution[1]) == new_solution[0]:
				solution = new_solution
				real_sol.append(solution[1][0])
				break
	real_sol.append(1) #back to city 1

	print("Best Visit Order: ",end='')
	for i in range(data_length+1):
		print(data_int[(real_sol[i]-1)*3],' ',end='') #modify the city number ex:1->0

	print('\n',end='')

	print("Best Distance： ",DP_dict[1, tuple(subset)])


#store the answer
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
	city,cost=readfile(file)

	subset=[]

	#create a subset[2,3,4,5.....end]
	for i in range(2,data_length+1):
		subset.append(i)

	#Dynamic Programming
	DP(1, tuple(subset))

	#output route
	findroute()

	#write file
	writefile(city,real_sol)
	print("Execution Time: ",time.time()-start_time," (s)")




