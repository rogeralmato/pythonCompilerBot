alias antlr4='java -jar /usr/local/lib/antlr-4.7.2-complete.jar'
cp EnquestesVisitor.py EnquestesVisitor_codi.py
antlr4 -Dlanguage=Python3 -no-listener -visitor Enquestes.g
cp EnquestesVisitor_codi.py EnquestesVisitor.py

