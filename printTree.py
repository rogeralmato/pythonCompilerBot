import sys
from antlr4 import *
import networkx as nx
import matplotlib.pyplot as plt
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor, G, labels, labelsI, labelsA


if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1],encoding='utf-8')
else:
    input_stream = InputStream(input('? '))

lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)
tree = parser.root()
visitor = EnquestesVisitor()
visitor.visit(tree)

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
pos=nx.circular_layout(G)
nx.draw(G, pos,with_labels=True)
nx.draw(G,pos,edges=edges, edge_color=colors, edge_labels=labels)
nx.draw_networkx_edge_labels(G,pos,edges=edges, edge_labels=labels,font_color='blue')
nx.draw_networkx_edge_labels(G,pos,edges=edges, edge_labels=labelsA,font_color='green')

plt.show()

nx.write_gpickle(G,"graph")

