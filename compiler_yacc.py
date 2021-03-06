import sys
import ply.yacc as yacc
from compiler_lex import tokens

def p_Prog(p):
    "Prog :  GlobalBlc MainBlc DefBlcs"
    out.write(p[1]+p[2]+p[3])

def p_DefBlcs(p):
    "DefBlcs : DefBlcs DefBlc "
    p[0] = p[1]+p[2]

def p_DefBlcs_End(p):
    "DefBlcs : "
    p[0] = ""

def p_DefBlc(p):
    "DefBlc : id '{' VarBlcs Insts '}' "
    p[0]=p[1]+":\n"
    p[0]+=p[3]+p[4]
    p[0]+="pushi 0\nstorel -1\nreturn\n"

    parser.table = {}
    parser.offset = 0
    parser.level = -1




def p_GlobalBlc(p):
    "GlobalBlc : GlobalBegin VarBlcs '}' "
    p[0]=p[1]+p[2]
    parser.offset = 0
    p.parser.isGlobal=False

def p_GlobalBegin(p):
    "GlobalBegin : global '{' "
    p.parser.isGlobal=True
    p[0]=""

def p_GlobalBlc_Null(p):
    "GlobalBlc : "
    p[0]=""

def p_VarBlcs(p):
    "VarBlcs : VarBlcs BlcInt "
    p[0]=p[1]+p[2]

def p_VarBlcs_End(p):
    "VarBlcs : "
    p[0]=""

def p_BlcInt(p):
    "BlcInt : int '{' Dcls '}' "
    p[0]=p[3]


def p_Dcls(p):
    "Dcls : Dcls Dcl"
    p[0]=p[1]+p[2]

def p_Dcls_End(p):
    "Dcls : "
    p[0]=""


def p_MainBlc(p):
    "MainBlc : main '{' VarBlcs Insts '}'"
    p[0]="start\n"
    p[0]+=p[3]+"pushn 10\n"
    p[0]+=p[4]+"stop\n"
    
    parser.table = {}
    parser.offset = 0
    parser.level = -1

def p_Insts(p):
    "Insts : Insts Inst "
    p[0]=p[1]+p[2]

def p_Insts_End(p):
    "Insts :"
    p[0]=""

def p_Inst_Attr(p):
    "Inst : Attr"
    p[0]=p[1]

def p_Inst_Return(p):
    "Inst : Return"
    p[0]=p[1]

def p_Inst_Exp(p):
    "Inst : Exp"
    p[0]=p[1]

def p_Inst_Print(p):
    "Inst : Print"
    p[0]=p[1]

def p_Inst_Println(p):
    "Inst : Println"
    p[0]=p[1]

def p_Inst_Prints(p):
    "Inst : Prints"
    p[0]=p[1]


def p_Inst_Repeat(p):
    "Inst : Repeat"
    p[0]=p[1]

def p_Inst_For(p):
    "Inst : For"
    p[0]=p[1]

def p_Inst_While(p):
    "Inst : While"
    p[0]=p[1]

def p_Inst_Read(p):
    "Inst : Read"
    p[0]=p[1]


def p_Inst_If(p):
    "Inst : If"
    p[0]=p[1]




def p_Repeat(p):
    "Repeat : repeat '(' Exp ')' '{' Insts '}' "
    p.parser.currTag+=1
    p.parser.level=(p.parser.level+1)%10
    p[0]="repeat"+str(p.parser.currTag)+":\n"

    p[0]+=p[6]
    addr = str(p.parser.level+p.parser.offset)
    p[0]+="pushl "+addr+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storel "+addr+"\n"

    p[0]+="pushl "+addr+"\n"
    p[0]+=p[3]
    p[0]+="equal\n"
    p[0]+="jz repeat"+str(p.parser.currTag)+"\n"

    p[0]+="pushi 0\n"
    p[0]+="storel "+addr+"\n"


def p_For(p):
    "For : for '(' Insts ';' Cond ';' Insts ')' '{' Insts '}'"
    p.parser.currTag+=1
    p[0]=p[3]
    p[0]+="forStart"+str(p.parser.currTag)+":\n"
    p[0]+=p[5]
    p[0]+="jz forEnd"+str(p.parser.currTag)+"\n"
    p[0]+=p[10]+p[7]
    p[0]+="jump forStart"+str(p.parser.currTag)+"\n"
    p[0]+="forEnd"+str(p.parser.currTag)+":\n"

def p_While(p):
    "While : while '(' Cond ')' '{' Insts '}'"
    p.parser.currTag+=1
    p[0]="whileStart"+str(p.parser.currTag)+":\n"
    p[0]+=p[3]
    p[0]+="jz whileEnd"+str(p.parser.currTag)+"\n"
    p[0]+=p[6]
    p[0]+="jump whileStart"+str(p.parser.currTag)+"\n"
    p[0]+="whileEnd"+str(p.parser.currTag)+":\n"
    

def p_Read(p):
    "Read : read '(' id ')'"

    p[0]="read\natoi\n"
    p[0]+="storel "+str(p.parser.table[p[3]])+"\n"

def p_Print(p):
    "Print : print '(' Exp ')'"
    p[0]=p[3]
    p[0]+="writei\n"

def p_Println(p):
    "Println : println '(' Exp ')'"

    p[0]=p[3]
    p[0]+="writei\n"
    p[0]+="pushs \"\\n\"\n"
    p[0]+="writes\n"

def p_Prints(p):
    "Prints : prints '(' string ')'"
    p[0]="pushs "+p[3]+"\n"
    p[0]+="writes\n"

def p_Dcl_Arr(p):
    "Dcl : id '[' num ']'"
    p[0]="pushn "+str(p[3])+"\n"
    if p.parser.isGlobal:
        p.parser.tableG[p[1]]=(p.parser.offset,0)
    else:
        p.parser.table[p[1]]=(p.parser.offset,0)
    p.parser.offset+=p[3]

def p_Dcl_Arr_valEq(p):
    "Dcl : id '[' num ']' '=' num"
    p[0]=""
    for i in range(p[3]):
        p[0]+="pushi "+str(p[6])+"\n"
        
    if p.parser.isGlobal:
        p.parser.tableG[p[1]]=(p.parser.offset,0)
    else:
        p.parser.table[p[1]]=(p.parser.offset,0)
    p.parser.offset+=p[3]

def p_Dcl_Arr_val(p):
    "Dcl : id '[' ']' '=' '{' Nums '}'"
    p[0]=p[6]
    if p.parser.isGlobal:
        p.parser.tableG[p[1]]=(p.parser.offset,0)
    else:
        p.parser.table[p[1]]=(p.parser.offset,0)
    p.parser.offset+=p.parser.arraySize
    p.parser.arraySize=0

def p_Nums(p):
    "Nums : Nums num"
    p.parser.arraySize+=1
    p[0]=p[1]+"pushi "+str(p[2])+"\n"

def p_Nums_End(p):
    "Nums : "
    p[0]= ""

def p_Dcl_Arr_2D_valEq(p):
    "Dcl : id '[' num ']' '[' num ']' '=' num"
    p[0]=""
    for i in range(p[3]*p[6]):
        p[0]+="pushi "+str(p[9])+"\n"

    if p.parser.isGlobal:
        p.parser.tableG[p[1][1:]]=(p.parser.offset,p[6])
    else:
        p.parser.table[p[1]]=(p.parser.offset,p[6])
    p.parser.offset+=p[3]*p[6]

def p_Dcl_Arr_2D(p):
    "Dcl : id '[' num ']' '[' num ']'"
    p[0]="pushn "+str(p[3]*p[6])+"\n"
    if p.parser.isGlobal:
        p.parser.tableG[p[1][1:]]=(p.parser.offset,p[6])
    else:
        p.parser.table[p[1]]=(p.parser.offset,p[6])
    p.parser.offset+=p[3]*p[6]

def p_Dcl_Arr_2D_val(p):
    "Dcl : id '[' ']' '[' ']' '=' '{' BlcsNums '}' "
    p[0]=p[8]
    if p.parser.isGlobal:
        p.parser.tableG[p[1][1:]]=(p.parser.offset,int(p.parser.arraySize/p.parser.linhas))
    else:
        p.parser.table[p[1]]=(p.parser.offset,int(p.parser.arraySize/p.parser.linhas))
    p.parser.offset+=p.parser.arraySize
    p.parser.arraySize=0
    p.parser.linhas=0

def p_BlcsNums(p):
    "BlcsNums : BlcsNums '{' Nums '}'"
    p.parser.linhas+=1
    p[0]=p[1]+p[3]

def p_BlcsNums_End(p):
    "BlcsNums : "
    p[0]=""

def p_Dcl_0(p):
    "Dcl : id"
    p[0]=("pushi 0\n")
    if p.parser.isGlobal:
        p.parser.tableG[p[1]]=p.parser.offset
    else:
        p.parser.table[p[1]]=p.parser.offset
    p.parser.offset+=1

def p_Dcl_num(p):
    "Dcl : id '=' num"
    p[0]="pushi "+str(p[3])+"\n"
    if p.parser.isGlobal:
        p.parser.tableG[p[1]]=p.parser.offset
    else:
        p.parser.table[p[1]]=p.parser.offset
    p.parser.offset+=1
    


def p_Attr(p):
    "Attr : id '=' Exp"

    p[0]=p[3]
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"


def p_Attr_arr(p):
    "Attr : id '[' Exp ']' '=' Exp"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"
    p[0]+=p[3]
    p[0]+=p[6]
    p[0]+="storen\n"
    

def p_Attr_arr2D(p):
    "Attr : id '[' Exp ']' '[' Exp ']' '=' Exp"

    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"
    p[0]+=p[3]
    p[0]+="pushi "+str(p.parser.table[p[1]][1])+"\n" #Tamanho das linhas
    p[0]+="mul\n"
    p[0]+=p[6]
    p[0]+="add\n"
    p[0]+=p[9]
    p[0]+="storen\n"

def p_Attr_g(p):
    "Attr : gid '=' Exp"

    p[0]=p[3]
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"


def p_Attr_arrg(p):
    "Attr : gid '[' Exp ']' '=' Exp"

    p[0]="pushgp\n"
    p[0]+="pushi "+str(p.parser.tableG[p[1][1:]][0])+"\n"
    p[0]+="padd\n"
    p[0]+=p[3]
    p[0]+=p[6]
    p[0]+="storen\n"
    

def p_Attr_arr2Dg(p):
    "Attr : gid '[' Exp ']' '[' Exp ']' '=' Exp"

    p[0]="pushgp\n"
    p[0]+="pushi "+str(p.parser.tableG[p[1][1:]][0])+"\n"
    p[0]+="padd\n"
    p[0]+=p[3]
    p[0]+="pushi "+str(p.parser.tableG[p[1][1:]][1])+"\n" #Tamanho das linhas
    p[0]+="mul\n"
    p[0]+=p[6]
    p[0]+="add\n"
    p[0]+=p[9]
    p[0]+="storen\n"

def p_Return(p):
    "Return : return '(' Exp ')'"
    p[0]=p[3]
    p[0]+="storel -1\n"
    p[0]+="return\n"

def p_If(p):
    "If : if '(' Cond ')' '{' Insts '}' "
    p.parser.currTag+=1
    p[0]=p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n"

    p[0]+=p[6]
    p[0]+="ifEnd"+str(p.parser.currTag)+":\n"



def p_If_Else(p):
    "If : if '(' Cond ')' '{' Insts '}' else '{' Insts '}'"
    p.parser.currTag+=1
    p[0]=p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n"
    p[0]+=p[6]
    p[0]+="jump elseEnd"+str(p.parser.currTag)+"\n"
    p[0]+="ifEnd"+str(p.parser.currTag)+":\n"

    p[0]+=p[10]
    p[0]+="elseEnd"+str(p.parser.currTag)+":\n"




def p_Exp_add(p):
    "Exp : Exp '+' Term"
    p[0] = p[1]+p[3]+"add\n"

def p_Exp_sub(p):
    "Exp : Exp '-' Term"
    p[0] = p[1]+p[3]+"sub\n"

def p_Exp_id_addeq(p):
    "Exp : id addeq Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Exp_id_subeq(p):
    "Exp : id subeq Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Exp_id_addeql(p):
    "Exp : id addeql Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Exp_id_subeql(p):
    "Exp : id subeql Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Exp_gid_addeq(p):
    "Exp : gid addeq Term"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="add\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Exp_gid_subeq(p):
    "Exp : gid subeq Term"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="sub\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Exp_gid_addeql(p):
    "Exp : gid addeql Term"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="add\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Exp_gid_subeql(p):
    "Exp : gid subeql Term"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="sub\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"


def p_Exp_term(p):
    "Exp : Term"
    p[0] = p[1]

def p_Term_mul(p):
    "Term : Term '*' Factor"
    p[0] = p[1]+p[3]+"mul\n"

def p_Term_div(p):
    "Term : Term '/' Factor"
    p[0] = p[1]+p[3]+"div\n"

def p_Term_mod(p):
    "Term : Term '%' Factor"
    p[0] = p[1]+p[3]+"mod\n"

def p_Term_id_muleq(p):
    "Term : id muleq Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mul\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_diveq(p):
    "Term : id diveq Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="div\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_modeq(p):
    "Term : id modeq Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mod\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"


def p_Term_id_muleql(p):
    "Term : id muleql Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mul\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_diveql(p):
    "Term : id diveql Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="div\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_modeql(p):
    "Term : id modeql Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mod\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Term_gid_muleq(p):
    "Term : gid muleq Factor"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="mul\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Term_gid_diveq(p):
    "Term : gid diveq Factor"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]    
    p[0]+="div\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Term_gid_modeq(p):
    "Term : gid modeq Factor"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="mod\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"


def p_Term_gid_muleql(p):
    "Term : gid muleql Factor"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="mul\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Term_gid_diveql(p):
    "Term : gid diveql Factor"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="div\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Term_gid_modeql(p):
    "Term : gid modeql Factor"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+=p[3]
    p[0]+="mod\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Term_factor(p):
    "Term : Factor"
    p[0] = p[1]

def p_Factor_id_plus(p):
    "Factor : id plus"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id_plusl(p):
    "Factor : id plusl"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id_minus(p):
    "Factor : id minus"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id_minusl(p):
    "Factor : id minusl"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Factor_gid_plus(p):
    "Factor : gid plus"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Factor_gid_plusl(p):
    "Factor : gid plusl"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Factor_gid_minus(p):
    "Factor : gid minus"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="sub\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Factor_gid_minusl(p):
    "Factor : gid minusl"
    p[0]="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushg "+str(p.parser.tableG[p[1][1:]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="sub\n"
    p[0]+="storeg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Factor_id(p):
    "Factor : id"
    p[0] = "pushl "+str(p.parser.table[p[1]])+"\n"

def p_Factor_gid(p):
    "Factor : gid"
    p[0] = "pushg "+str(p.parser.tableG[p[1][1:]])+"\n"

def p_Factor_num(p):
    "Factor : num"
    p[0] = "pushi "+str(p[1])+"\n"

def p_Factor_call(p):
    "Factor : id '(' ')' "
    p[0] = "pushi 0\n"
    p[0]+= "pusha "+str(p[1])+"\ncall\n"


def p_Factor_cond(p):
    "Factor : '(' Cond ')'"
    p[0] = p[2]


def p_Factor_arr(p):
    "Factor : id '[' Exp ']'"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"+p[3]
    p[0]+="loadn\n"

def p_Factor_arr_2d(p):
    "Factor : id '[' Exp ']' '[' Exp ']'"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"+str(p[3])
    p[0]+="pushi "+str(p.parser.table[p[1]][1])+"\n"
    p[0]+="mul\n"+str(p[6])
    p[0]+="add\n"+"loadn\n"

def p_Factor_arrg(p):
    "Factor : gid '[' Exp ']'"
    p[0]="pushgp\n"
    p[0]+="pushi "+str(p.parser.tableG[p[1][1:]][0])+"\n"
    p[0]+="padd\n"+p[3]
    p[0]+="loadn\n"

def p_Factor_arrg_2d(p):
    "Factor : gid '[' Exp ']' '[' Exp ']'"
    p[0]="pushgp\n"
    p[0]+="pushi "+str(p.parser.tableG[p[1][1:]][0])+"\n"
    p[0]+="padd\n"+str(p[3])
    p[0]+="pushi "+str(p.parser.tableG[p[1][1:]][1])+"\n"
    p[0]+="mul\n"+str(p[6])
    p[0]+="add\n"+"loadn\n"


def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]


def p_Cond_and_par(p):
    "Cond : '(' Cond and Cond ')'"
    p[0] = p[2]+p[4]+"mul\n"

def p_Cond_or_par(p):
    "Cond : '(' Cond or Cond ')' "
    p[0] = p[2]+p[4]+"add\n"
    p[0]+=p[2]+p[4]+"mul\n"+"sub\n"

def p_Cond_sup(p):
    "Cond : Exp sup Exp"
    p[0] = p[1]+p[3]+"sup\n"

def p_Cond_inf(p):
    "Cond : Exp inf Exp"
    p[0] = p[1]+p[3]+"inf\n"

def p_Cond_supeq(p):
    "Cond : Exp supeq Exp"
    p[0] = p[1]+p[3]+"supeq\n"

def p_Cond_infeq(p):
    "Cond : Exp infeq Exp"
    p[0] = p[1]+p[3]+"infeq\n"

def p_Cond_not(p):
    "Cond : not Exp"
    p[0] = p[2]+"not\n"

def p_Cond_eq(p):
    "Cond : Exp eq Exp"
    p[0] = p[1]+p[3]+"equal\n"

def p_Cond_diff(p):
    "Cond : Exp diff Exp"
    p[0] = p[1]+p[3]+"equal\n"+"not\n"


def p_error(p):
    print('Syntax error: ', p)

parser = yacc.yacc()
parser.tableG = {}
parser.table = {}
parser.offset = 0
parser.level = -1
parser.currTag = 0
parser.isGlobal = False
parser.arraySize = 0
parser.linhas = 0

f = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

result = parser.parse(f.read())