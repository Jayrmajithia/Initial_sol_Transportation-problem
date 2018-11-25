def min(x,y):
	if x<y:
		return x;
	else:
		return y;
def sum(x):
	r=0
	for i in x:
		r=r+i;
	return r;
class InitialNorth:
	m=0;
	n=0;
	cost=[];
	init=[];
	supply=[];
	demand=[];
	def __init__(self,a,b):
		self.m=a;
		self.n=b;
		for i in range(0,self.m):
			self.cost.append([]);
			self.init.append([]);
			for j in range(0,self.n):	
				self.cost[i].append(int(input("enter the cost for {} supply location and {} demand location: ".format(i+1,j+1))));
				self.init[i].append(0);
		for i in range(0,self.m):
			self.supply.append(int(input("enter the maximum supply from location {}: ".format(i+1))));
		for i in range(0,self.n):
			self.demand.append(int(input("enter the maximum demand from location {}: ".format(i+1))));
	def sol(self):
		if sum(self.supply)!=sum(self.demand):
			if sum(self.supply)<sum(self.demand):
				self.cost.append([]);
				self.init.append([]);
				self.supply.append(sum(self.demand)-sum(self.supply));
				self.m=self.m+1;
				for i in range(0,self.n):
					self.cost[m].append(0);
					self.init[m].append(0);
			else:
				self.demand.append(sum(self.supply)-sum(self.demand));
				self.n=self.n+1;
				for i in range(0,self.m):
					self.cost[i].append(0);
					self.init[i].append(0);
		s=self.supply;
		d=self.demand;
		for i in range(0,self.m):
			for j in range(0,self.n):
				x=min(s[i],d[j]);
				if s[i]==x:
					s[i]=0;
					d[j]=d[j]-x;
					self.init[i][j]=x;
					i+=1;
					break;
				else:
					d[j]=0;
					s[i]=s[i]-x;
					self.init[i][j]=x;
		z=0;
		print("initial basic variable are as below (Supply Location = Solution):");
		for i in range(0,self.m):
			for j in range(0,self.n):
				if self.init[i][j]==0:
					continue;
				else:
					x=i+1;
					y=j+1;
					print(x,y,"=",self.init[i][j]);
					z+=(self.cost[i][j]*self.init[i][j]);
		print("Initial Optimal Solution is", z);
m=int(input("Enter number of Supply location: "));
n=int(input("Enter number of Demand locations: "));
r=InitialNorth(m,n);
r.sol();