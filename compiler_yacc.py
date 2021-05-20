import sys
import ply.yacc as yacc
from compiler_lex import tokens

# Prog -> VarBlc MainBlc
#
# VarBlc -> vars '{' Dcls '}'
#
# Dcls    -> DclInt Dcls
#          | 
#
# DclInt -> int id = num 
#         | int id num
#         | int id
#
# MainBlc -> main '{' Insts '}'
# 
# Insts -> AttrInt Insts
#        | Print Insts
#        | Println Insts
#        | Repat Insts
#        |
# 
# AttrInt -> id = num 
#          | id num
# 
# Print -> print '(' id ')'
#
# Repeat -> repeat '(' num ')' '{' Insts '}'

def p_Prog(p):
    "Prog : VarBlc MainBlc"

def p_VarBlc(p):
    "VarBlc : vars '{' Dcls '}'"

def p_Dcls(p):
    "Dcls : DclInt Dcls"

def p_Dcls_End(p):
    "Dcls : "
    out.write("pushn 10\n")
    out.write("start\n")
    p.parser.table["ciclo"]=[0,1,2,3,4,5,6,7,8,9]

def p_MainBlc(p):
    "MainBlc : main '{' Insts '}'"
    out.write("stop\n")

def p_Insts_Attr(p):
    "Insts : AttrInt Insts"

def p_Insts_Print(p):
    "Insts : Print Insts"

def p_Insts_Println(p):
    "Insts : Println Insts"

def p_Insts_Repeat(p):
    "Insts : Repeat Insts"

def p_Insts(p):
    "Insts : "

def p_Repeat(p):
    "Repeat : RepeatS '(' num ')' '{' Insts '}' "
    out.write("pushg "+str(p.parser.table["ciclo"][p.parser.numReg]+p.parser.offset)+"\n")
    out.write("pushi 1\n")
    out.write("add\n")
    out.write("storeg "+str(p.parser.table["ciclo"][p.parser.numReg]+p.parser.offset)+"\n")

    out.write("pushg "+str(p.parser.table["ciclo"][p.parser.numReg]+p.parser.offset)+"\n")
    out.write("pushi "+str(p[3])+"\n")
    out.write("equal\n")
    out.write("jz ciclo"+str(p.parser.cicles)+"\n")

    out.write("pushi 0\n")
    out.write("storeg "+str(p.parser.table["ciclo"][p.parser.numReg]+p.parser.offset)+"\n")
    print(p.parser.numReg)
    p.parser.numReg-=1

def p_RepeatS(p):
    "RepeatS : repeat"
    p.parser.numReg+=1
    p.parser.cicles+=1
    out.write("ciclo"+str(p.parser.cicles)+":\n")
    print("Reg: "+str(p.parser.numReg))

def p_Print(p):
    "Print : print '(' id ')'"
    out.write("pushg "+str(p.parser.table[p[3]])+"\n")
    out.write("writei\n")

def p_Println(p):
    "Println : println '(' id ')'"
    out.write("pushg "+str(p.parser.table[p[3]])+"\n")
    out.write("writei\n")
    out.write("pushs \"\\n\"\n")
    out.write("writes\n")

def p_DclInt(p):
    "DclInt : int id"
    out.write("pushi 0\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_DclInt_Attr(p):
    "DclInt : int id num"
    out.write("pushi "+str(p[2])+"\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_DclInt_AttrEq(p):
    "DclInt : int id '=' num"
    out.write("pushi "+str(p[4])+"\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_AttrInt(p):
    "AttrInt : id num"
    out.write("pushi "+str(p[2])+"\n")
    out.write("storeg "+str(p.parser.table[p[1]])+"\n")

def p_AttrInt_Eq(p):
    "AttrInt : id '=' num"
    out.write("pushi "+str(p[3])+"\n")
    out.write("storeg "+str(p.parser.table[p[1]])+"\n")

def p_error(p):
    print('Syntax error: ', p)

parser = yacc.yacc()
parser.table = {}
parser.offset = 0
parser.numReg = -1
parser.cicles = 0

f = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

result = parser.parse(f.read())