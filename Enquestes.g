grammar Enquestes;
root : expr?  'END' EOF;
expr : (pregunta | resposta | item | alternativa)*  infoEnquesta ;

pregunta: idPregunta TWODOTS SPACE 'PREGUNTA'  frasePregunta ;
frasePregunta: FRASE '?'; 
idPregunta: 'P' INT ;

resposta: idResposta TWODOTS SPACE 'RESPOSTA' llistaRespostes+ ;
idResposta: 'R' INT ;
llistaRespostes: INT TWODOTS contingutResposta ;
contingutResposta: SPACE FRASE SPACE SEMICOLON;

item: idItem TWODOTS SPACE 'ITEM' relacioItem ;
relacioItem: idPregunta SPACE '->' SPACE idResposta ;
idItem: 'I' INT ;

alternativa: idalternativa TWODOTS SPACE 'ALTERNATIVA' contingutAlternativa ;
idalternativa: 'A' INT ;
contingutAlternativa: idItem SPACE INICLAU contingutClaus* FICLAU ;
contingutClaus: COMA? INIPAR INT COMA 'I' INT FIPAR ;

infoEnquesta: 'E' TWODOTS SPACE 'ENQUESTA' contingutEnquesta ;
contingutEnquesta: idItem (SPACE idItem)* ;


COMA: ','  ;
INICLAU: '[' ;
FICLAU: ']' ;
INIPAR: '(' ;
FIPAR: ')' ;
SEMICOLON: ';' ;
TWODOTS : ':' ;
FRASE: WORD (SPACE WORD)* ;
WORD: [A-Za-zéèàáíìòóùúüï'́ı]+ ;
INT: [0-9]+ ;
SPACE: ' ' ;
WS : [\t\r\n]+ -> skip ;
