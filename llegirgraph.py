import networkx as nx
import pickle
import matplotlib.pyplot as plt

def llegirCorrecte(G, name):
    nodes = list(G.nodes)
    return nodes[0] == name

def llegirPreguntes(G):
    nodes = list(G.nodes)
    result = []
    for n in nodes:
        if n[0] == 'P':
            result.append(n)
    return result

def llegirPreguntaEspecifica(G, P):
    nodes = list(G.nodes)
    arcs = list(G.edges)
    l = list(filter(lambda x: x[0] == P, arcs ))
    lr = list(map(lambda x: (x[1],G.nodes[x[1]]['info'],[0]*len(G.nodes[x[1]]['info']),G.nodes[x[1]]['possR']),list(filter(lambda x: G[x[0]][x[1]]['tipus'] == 1, l))))
    ls = list(map(lambda x: (x[1],G[x[0]][x[1]]['question']),list(filter(lambda x: G[x[0]][x[1]]['tipus'] == 2, l))))
    return [(P,G.nodes[P]['info']), lr[0], ls]

def readData(nomFitxer):
    G = nx.read_gpickle("graph")
    preguntes = llegirPreguntes(G)
    try:
        with open(nomFitxer, 'rb') as handle:
            data = pickle.load(handle)
    except Exception:
        data = {}
        for p in preguntes:
            data[p] = llegirPreguntaEspecifica(G,p)
        with open(nomFitxer, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return data

def writeData(nomFitxer, data):
    with open(nomFitxer, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def afegirResposta(pregunta, resposta, data):
    if isinstance(data[pregunta][1][3][0], int):
        resposta = int(resposta) 
    l = data[pregunta][1][3]
    index = l.index(resposta)
    data[pregunta][1][2][index] += 1
    return data