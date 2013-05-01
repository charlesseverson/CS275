
import random
import disjointSet
import matplotlib.pyplot as plt

class BiGraph:
	'''An undirected binomial random graph'''
	
	def __init__(self):
		'''Graph constructor'''
		self.graph={}
		
	def Binomial(self, n, p):
		'''Generate and return an instance of a binomial random graph'''
		L=[]
		for i in range(n):
			for j in range(n):
				if j != i:
					L.append((i,j))
		for e in L:
			possibility=random.random()
			if possibility < p:
				self.add_edge(e)
				
	def degreeDistBinomial(self, n, p, trials):
		'''Plot an average degree distribution of a binomial ranhom graph over a number of trials'''
		A=[]
		x=[]
		for i in range(n):
			A.append(0)
		for j in range(trials):
			self.Binomial(n, p)
			for k in self.graph:
				count=0
				for e in self.graph[k]:
					count=count+1
				A[count]=A[count]+1
			self.graph={}
		for m in range(n):					#the index of A indicates degree, A[index] indicates the number of nodes with degree index.
			A[m]=(float(A[m])/trials)
		for degree in range(len(A)):		
			x.append(degree)
		plt.plot(x, A)
		plt.show()
				
	def add_edge(self, e):
		'''Add an edge e = (u,v) (and its endvertices if necessary) to the graph'''
		if e[0] in self.graph:
			if e[1] not in self.graph[e[0]]:
				self.graph[e[0]].append(e[1])
				if e[1] in self.graph:
					self.graph[e[1]].append(e[0])
				else:
					self.graph[e[1]]=[e[0]]
		else:
			self.graph[e[0]]=[e[1]]
			if e[1] in self.graph:
				self.graph[e[1]].append(e[0])
			else:
				self.graph[e[1]]=[e[0]]
				
	def add_edges(self, edges):
		'''Add a list of edges to the graph'''
		for i in range(len(edges)):
			self.add_edge(edges[i])
			
	def add_vertex(self, v):
		'''Add a vertex to the graph'''
		if v not in self.graph:
			self.graph[v]=[]
			
	def add_vertices(self, vertices):
		'''Add a list of vertices to the graph'''
		for j in range(len(vertices)):
			self.add_vertex(j)
			
	def edges(self):
		'''Return a list of edges in the graph'''
		Edges=[]
		for K in self.graph:
			for E in self.graph[K]:
				Edges.append([K,E])
		return Edges
	
	def nodes(self): 
		'''Return a list of nodes in the graph'''
		Nodes=[]
		for key in self.graph:
			Nodes.append(key)
		return Nodes
		
