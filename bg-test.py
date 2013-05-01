#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7

import bigraph                       # your graph class
import disjointSet
import networkx as nx              # NetworkX graph module
import matplotlib.pyplot as plt    # Matplotlib module (upon which NetworkX is built)

def drawBG(G):
	'''Draw a graph, highlighting its BFS tree.'''
	
	H = nx.Graph()                  # create a new NetworkX graph
	H.add_nodes_from(G.nodes())     # add nodes from G to H
	pos = nx.spring_layout(H)       # positions for the nodes
	
	nx.draw_networkx_nodes(H, pos, node_size = 500)  # draw the vertices
	nx.draw_networkx_labels(H, pos, font_size = 16)  # draw the vertex labels
	
	# draw edges 
	nx.draw_networkx_edges(H, pos, edgelist = G.edges(), width=2)
	

	plt.show()   # keep the display up until we dismiss it

def main():
	
	G = bigraph.BiGraph()
	G.Binomial(4, 0.3)
	
	
	print "The graph G has the following edges:", G.edges()
	G.degreeDistBinomial(200, 0.3, 1000)
	drawBG(G)
	'''
	def connectedBinomial(n, p1, p2, step, trials):
		x=[]
		y=[]
		while p1 <= p2:
			count=0
			for j in range(trials):
				g=bigraph.BiGraph()
				g.Binomial(n, p1)
				ds=disjointSet.DisjointSet()
				vertices=g.nodes()
				for n in vertices:
					ds.make_set(n)
				edge=g.edges()
				for e in edge:
					if ds.find_set(e[0]) != ds.find_set(e[1]):
						ds.union(e[0], e[1])
				disconnected=0
				for check in vertices:
					if ds.find_set(check) != ds.find_set(vertices[0]):
						disconnected=disconnected+1
				if disconnected == 0:
					count=count+1
			x.append(p1)
			y.append(float(count)/trials)
			p1=p1+step
		print "y", y
		plt.plot(x, y)
		plt.show()
	
	connectedBinomial(200, 0.05, 0.9, 0.01, 1000)
	'''
	
	

main()