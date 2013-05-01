
class DisjointSet(object):
	
	def __init__(self):
		self.parent = {}
		self.rank = {}
		
	def make_set(self, x):
		if x not in self.parent:
			self.parent[x] = x
		if x not in self.rank:
			self.rank[x] = 0
			
	def union(self, x, y):
		self.link(self.find_set(x), self.find_set(y))
			
	def link(self, x, y):
		if self.rank[x] > self.rank[y]:
			self.parent[y] = x
		else:
			self.parent[x] = y
			if self.rank[x] == self.rank[y]:
				self.rank[y] += 1
			
	def find_set(self, x):
		if x != self.parent[x]:
			self.parent[x] = self.find_set(self.parent[x])
		return self.parent[x]
		

		
	