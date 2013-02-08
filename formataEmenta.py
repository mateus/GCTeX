#!/usr/bin/python
#coding: utf-8

import re
import subprocess
import shlex
import os

#Abre arquivo de ementa não formatada
ementaLimpa = open('editaveis/Ementa.txt', 'r').readlines()

#Retira quebra de linha
for linha in ementaLimpa:
    if linha == '\n':
        ementaLimpa.remove(linha)
     
#Retira estaças adicionais   
for linha in ementaLimpa:
    ementaLimpa[ementaLimpa.index(linha)] = linha.strip()           

#Adiciona tag italico LaTeX a ementa
textoItalico = r'\\textit{\1}' 
for linha in ementaLimpa:
    ementaLimpa[ementaLimpa.index(linha)] = re.sub(r'_(.+?)_', textoItalico, linha)

#Adiciona tags LaTeX a ementa
topico = r'{\\normalsize \\textbf{\1\2\3\\\}}'
subtopico = r'	• \1\\\\'
for linha in ementaLimpa:
    try:
        ementaLimpa[ementaLimpa.index(linha)] = re.sub(r'(^[0-9]+.)(.*)()$', topico, linha)
    except Exception, e:
        pass
    try:
        if(len(linha) > 0):
            ementaLimpa[ementaLimpa.index(linha)] = re.sub(r'(.*)', subtopico, linha)
    except Exception, e:
        pass


#Agrupa o texto
ementaLimpa = '\n'.join(ementaLimpa)

#Imprime no arquivo EmentaFormatada.txt o texto final
open('EmentaFormatada.txt', 'w').write(ementaLimpa)

print '\033[1;33m\nArquivo de ementa formatado gerado em EmentaFormatada.txt\033[0m'
print '\033[1;33mGerando PDF...\n\033[0m'

#Gera pdf com base no código .tex(Template LaTeX)
proc=subprocess.Popen(shlex.split('pdflatex GeradorCertificados.tex'))
proc.communicate()


