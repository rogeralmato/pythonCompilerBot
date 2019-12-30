import networkx as nx
import matplotlib.pyplot as plt

# Generated from Enquestes.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.
G = nx.DiGraph()
G.add_node('E')
G.add_node('END')
elemP = ['E']
elemR = []
elemI = []
labels = {}
labelsA = {}
labelsI = {}
elemA = []

class EnquestesVisitor(ParseTreeVisitor):
    
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        l = [x for x in ctx.getChildren()]
        for i in range(len(l)):
            self.visit(l[i])

    def visitExpr(self, ctx:EnquestesParser.ExprContext):
            g = ctx.getChildren()
            l = [x for x in ctx.getChildren()]
            for i in range(len(l)):
                self.visit(l[i])

    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
            g = ctx.getChildren()
            l = [x for x in ctx.getChildren()]
            G.add_node(l[0].getText(), info=l[4].getText())

    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        G.add_node(l[0].getText(), info=[], possR = [])
        elemR.append(l[0].getText())
        for i in range(3, len(l)):
            self.visit(l[i])
    
    def visitLlistaRespostes(self, ctx:EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        G.nodes[elemR[-1]]['possR'].append(int(l[0].getText()))
        self.visit(l[2])

    def visitContingutResposta(self, ctx:EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        G.nodes[elemR[-1]]['info'].append(' ' + str(l[1].getText()))
    
    def visitItem(self, ctx:EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        elemI.append(l[0].getText())
        
        self.visit(l[4])
        
    
    def visitRelacioItem(self, ctx: EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        labelsI[elemI[-1]] = l[0].getText()
        labels[(l[0].getText(),l[4].getText())] = elemI[-1]
        G.add_edge(l[0].getText(), l[4].getText(),color='blue')
        G[l[0].getText()][l[4].getText()]['tipus'] = 1

    def visitAlternativa(self, ctx: EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        self.visit(l[4])

    def visitContingutAlternativa(self, ctx: EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        elemA.append(l[0].getText())
        for i in range(len(l)):
            self.visit(l[i])

    def visitContingutClaus(self, ctx: EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        for i in range(len(l)):
            if l[i].getText() == 'I' :
                labelsA[(labelsI[elemA[-1]],labelsI[str(l[i].getText()+l[i+1].getText())])] = l[i-2].getText()
                G.add_edge(labelsI[elemA[-1]], labelsI[str(l[i].getText()+l[i+1].getText())],color='green')
                G[labelsI[elemA[-1]]][labelsI[str(l[i].getText()+l[i+1].getText())]]['question'] = l[i-2].getText()
                G[labelsI[elemA[-1]]][labelsI[str(l[i].getText()+l[i+1].getText())]]['tipus'] = 2

    def visitInfoEnquesta(self, ctx: EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        for i in range(len(l)):
            self.visit(l[i])

    def visitContingutEnquesta(self, ctx:EnquestesParser.RespostaContext):
        l = [x for x in ctx.getChildren()]
        for i in range(len(l)):
            if l[i].getText() != ' ':
                G.add_edge(elemP[-1], labelsI[l[i].getText()],color='black')
                G[elemP[-1]][labelsI[l[i].getText()]]['question'] = -1
                G[elemP[-1]][labelsI[l[i].getText()]]['tipus'] = 2
                elemP.append(labelsI[l[i].getText()])
        G.add_edge(elemP[-1], 'END', color='black')
        G[elemP[-1]]['END']['tipus'] = 2
        G[elemP[-1]]['END']['question'] = -1

#del EnquestesParser