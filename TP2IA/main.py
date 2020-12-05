
from tkinter import *
from std import a_estrela, guloso, node_a_estrela, node_guloso, puzzle
# tamanho da fonte:
large_font = ('Verdana', 30)

# estado final


'''cria a janela'''
janela = Tk()
caminho = []
entradas = []  # vetor de Entrys
init = []  # entrada dos algoritmos
opcoes = []  # vetor de radioButtons
saidas = []  # vetor para Labels
var = IntVar()  # valorar as opções


def fazCaminho(elementoFinal):
    # print("Faz Caminho")
    global caminho
    while (elementoFinal != None):
        # print(elementoFinal.statePuzzle.mat) #<---
        caminho.append(elementoFinal.statePuzzle.mat)
        elementoFinal = elementoFinal.pai
    caminho.reverse()
    print("Imprimir Caminho")
    for i in caminho:
        print(i)

###### ALGORITMOS PARA PESQUISA #######
'''
def runFB_largura():
    global init # Matriz inicial digitada
    estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]] # Estado final estado ótimo
    print("largura\n") # indica qual algoritimo esta executando
    initPuzzle = puzzle.Puzzle(init) # inicializa o puzzle com estado inicial
    root_largura = node_largura.Node(None, initPuzzle, "root", 0, 0) # gera o node largura
    larguraAux = largura.Largura(root_largura, estadoFinal) # inicializa a classe largura passando como parametro o node criado acima
    elemento = larguraAux.teste_lista() # chama a funcao  teste lista
    fazCaminho(elemento[0]) # funcao que passa como paramentro o elemento testado na linha de cima


def runFB_profund():
    global init # Matriz inicial digitada
    estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]] # Estado final estado ótimo
    print("profundidade\n") # indica qual algoritimo esta executando
    initPuzzle = puzzle.Puzzle(init) # inicializa o puzze com estado inicial
    root_profundidade = node_profundidade.Node(None, initPuzzle, "root", 0, 0) # gera o node profundidade
    profundidadeAux = profundidade.Profundidade(root_profundidade, estadoFinal) # Inicializa a classe profundidade passando como paramentro o nodecriado acima
    elemento = profundidadeAux.teste_lista() # chama a funcao teste lista
    fazCaminho(elemento[0]) # funcao que passa como paramentro o elemento testado na linha de cima
'''
def run_guloso():
    global init # Matriz inicial digitada
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]] # Estado final estado ótimo
    print("guloso\n") # indica qual algoritimo esta executando
    initPuzzle = puzzle.Puzzle(init)  # inicializa o puzze com estado inicial
    root_guloso = node_guloso.Node(None,initPuzzle,"root",0,0)
    gulosoAux = guloso.Guloso(root_guloso,estadoFinal)
    elemento = gulosoAux.teste_lista()

    fazCaminho(elemento[0])

def runFB_A_estrela():
    global init # Matriz inicial digitada
    estadoFinal = [[1,2,3],[4,5,6],[7,8,-1]] # Estado final estado ótimo
    initPuzzle = puzzle.Puzzle(init)  # inicializa o puzze com estado inicial
    root_a_estrela = node_a_estrela.Node(None,initPuzzle,"root",0,0,-1)
    a_estrelaAux = a_estrela.A_estrela(root_a_estrela,estadoFinal)
    elemento = a_estrelaAux.teste_lista()

    fazCaminho(elemento[0])


# METODO PARA VERIFICAR DADOS DIGITADOS NAS ENTRADAS:
def verifica():  # Ok
    vetor = []
    global entradas
    global init

    for i in range(9):  # verifica se todos os campos foram preenchidos e substitui o zero por -1
        if (entradas[i].get() == ''):
            vetor.append(-1)
        else:
            vetor.append(int(entradas[i].get()))

    for i in range(-1, 9):  # verifica se tem todos os numeros validos
        if i != 0 and i not in vetor:
            return False
    aux = []
    cont = 0;
    for i in range(3):  # deixa o vetor de entradas da forma que as funções estão esperando
        for j in range(3):
            aux.append(vetor[cont])
            cont += 1
        init.append(aux)
        aux = []
    print(init)
    return True


# AÇÕES DOS BOTÕES
def gerarJogo():  # Ok
    global opcoes
    global init
    # verificação de validade dos dados digitados:
    if (verifica()):
        for i in range(4):
            opcoes[i]['state'] = 'normal'
            opcoes[i].configure(background='white')
        fundo.configure(background='white')
        # print(init)
    else:
        print("DADOS INVALIDOS!", " dados invalidos! digite uma sequência de números válidos")


# REABILITAR COMANDO:
def sel():  # Ok
    global var
    print(var.get())
    rumAlg['state'] = 'normal'
    rumAlg.configure(background='white')


def rodaAlg():
    global var
    if var.get() == 3:
        run_guloso()
    elif var.get() == 4:
        runFB_A_estrela()


def attSaida(i):
    global saidas
    saidas[0].configure(text=str(i[0][0]))
    saidas[1].configure(text=str(i[0][1]))
    saidas[2].configure(text=str(i[0][2]))
    saidas[3].configure(text=str(i[1][0]))
    saidas[4].configure(text=str(i[1][1]))
    saidas[5].configure(text=str(i[1][2]))
    saidas[6].configure(text=str(i[2][0]))
    saidas[7].configure(text=str(i[2][1]))
    saidas[8].configure(text=str(i[2][2]))


################################## funções para criar botões #################################
def criar_entradas():
    global entradas
    largura, altura, cont = 40, 40, 0
    for i in range(3):
        for j in range(3):
            entradas.append(Entry(janela, font=large_font, justify="center"))
            entradas[cont].place(width=40, height=40)
            entradas[cont].place(x=largura, y=altura)
            largura += 40
            cont += 1
        largura = 40
        altura += 40


def criar_opcoes():
    global var
    cont = 0
    aux = 1
    textos = ["LARGURA", "PROFUNDIDADE" ,"BUSCA GULOSA" ," BUSCA A*"]
    for i in range(4):
        opcoes.append(Radiobutton(janela, text=textos[i], variable=var, value=aux, command=sel, state='disabled'))
        opcoes[i].place(x=170, y=90 + cont)
        opcoes[i].configure()
        cont += 20
        aux += 1


def criar_saidas():
    global saidas
    largura, altura, cont = 40, 260, 0
    for i in range(3):
        for j in range(3):
            saidas.append(Label(janela, font=large_font, justify="center"))
            saidas[cont].place(width=39, height=39)
            saidas[cont].place(x=largura, y=altura)
            largura += 40
            cont += 1
        largura = 40
        altura += 40


##########################   informações da tela #################################
lab = Label(janela, text="INSERIR DADOS INICIAIS DO JOGO")
lab.place(x=10, y=10)

criar_entradas()

# BOTÃO PARA GERAR O  JOGO
gera = Button(janela, text='GERAR JOGO', command=gerarJogo)
gera.place(x=200, y=50)

# FUNDO DAS OPÇÕES:
fundo = Label(janela)
fundo.place(x=165, y=90)
fundo.place(width=190, height=85)

criar_opcoes()

# BOTÃO PARA RODAR ALGORITMO:
rumAlg = Button(janela, text='RODAR ALGORITMO', command=rodaAlg)
rumAlg.place(x=180, y=180)
rumAlg.configure(state='disabled')

criar_saidas()

#######################################################################################

# alterar tamanho
# LxA+e+t
janela.geometry("400x400+250+60")
'''bloqueia a possibilidade de redimencionar a tela'''
janela.resizable(width=False, height=False)
janela.mainloop()