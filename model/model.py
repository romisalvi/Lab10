import networkx as nx

from database.DAO import DAO
from model.country import Country


class Model:


    def __init__(self):

        self.G=nx.Graph()
        self.allCountries=DAO.getCountries()
        self.G.add_nodes_from(self.allCountries)
        self.idMap={}

        for c in self.allCountries:
            self.idMap[c.CCode]=c

    def creaGrafo(self, anno):
        #i need to get the edges
        allConfini=self.addConfini(anno)
        for c in allConfini:
            self.G.add_edge(self.idMap[c.state1no],self.idMap[c.state2no])


    def addConfini(self, anno):
        self.G.clear_edges()
        return DAO.getConfini(anno)
    def getNodes(self):
        return self.G.nodes
    def getNConn(self):
        return nx.number_connected_components(self.G)
    def degNode(self, co:Country):
        return self.G.degree(co)
    def getCompConn(self, co:Country):
        return nx.bfs_tree(self.G,co)
    def getNinCompConn(self,co:Country):
        return len( nx.node_connected_component(self.G,co))
    def daiNodi(self, co):
        visited=[]
        self.recursione(co,visited)
        visited.remove(co)
        return visited
    def recursione(self, co:Country, visited):
        visited.append(co)
        vicini=self.G.neighbors(co)
        for nodo in vicini:
            if nodo not in visited:
                self.recursione(nodo,visited)
    def algorIter(self,co:Country):
        visitati=[]
        davisitare=[co]
        while len(davisitare)!=0:
            for el in davisitare:
                vicini=self.G.neighbors(el)
                for vicino in vicini:
                    if vicino not in visitati:
                        davisitare.append(vicino)
                visitati.append(el)
                davisitare.remove(el)
        visitati.remove(co)
        return visitati








