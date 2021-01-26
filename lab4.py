#Descrição do laboratorio 4
# Street Fighter é um jogo de luta desenvolvido pela Capcom que teve sua primeira versão lançada em 1987. O jogo é bastante famoso e faz sucesso até os dias atuais, inclusive servindo de inspiração para filmes. No jogo, um jogador controla um lutador que enfrenta seu adversário. O jogo apresenta vários personagens com poderes especiais que podem ser escolhidos para a luta, sendo Ryu e Ken os dois lutadores mais conhecidos de Street Fighter. Neste laboratório, você deve simular uma luta entre Ryu e Ken, informando no fim qual dos dois lutadores saiu vitorioso.
#
# Cada lutador começa a luta com uma quantidade de pontos de vida (hp, do inglês Health Points) e realiza uma sequência de golpes que geram decréscimo no hp do adversário. Inicialmente, seu programa deve ler dois valores inteiros que indicam a quantidade inicial de hp dos lutadores Ryu e Ken, respectivamente. Depois disso, você deve ler a sequência de golpes que foram realizados na luta. Um golpe é um valor inteiro, sendo que um golpe com valor positivo indica que o golpe foi realizado pelo lutador Ryu e um golpe com valor negativo indica que o golpe foi realizado pelo lutador Ken. O valor absoluto de um golpe indica a quantidade que deve ser diminuída do hp do adversário. Para cada golpe, você deve imprimir três linhas de informações. A primeira linha deve informar quem aplicou o golpe e o valor absoluto do mesmo. A segunda e terceira linha devem informar o hp dos lutadores Ryu e Ken, respectivamente. Exemplo das informações que devem ser exibidas para cada golpe aplicado:
#
# <Lutador que atacou> APLICOU UM GOLPE: <Valor absoluto do golpe>
# HP RYU = <HP do lutador RYU>
# HP KEN = <HP do lutador KEN>

# O hp de cada lutador nunca será negativo, sendo que seu valor mínimo é zero. No momento que o hp de um dos lutadores chega em zero o mesmo é considerado como derrotado e a luta é encerrada. Seu programa deve imprimir o nome do lutador que venceu a luta seguido do número de golpes aplicados por cada lutador no seguinte formato:

# LUTADOR VENCEDOR: <Lutador vencedor>
# GOLPES RYU = <Número de golpes aplicados pelo lutador RYU>
# GOLPES KEN = <Número de golpes aplicados pelo lutador KEN>

# Leitura do hp dos lutadores
hp_ryu = int(input())
hp_ken = int(input())
hp_ryu_impressao = hp_ryu
hp_ken_impressao = hp_ken
fim = 0
conta_golpes_ken = 0
conta_golpes_ryu = 0
seq_golpes = []
i=0;

# Leitura da sequência de golpes

while(fim != 1):
    golpe = int(input())
    if golpe<0:
            #golpe realizado pelo hp_ken
             hp_ryu = hp_ryu - abs(golpe)
    else:
        hp_ken = hp_ken - abs(golpe)

    #Guardando a informação em um vetor para consulta posterior
    seq_golpes.append(golpe)
    #Checagem se algum deles já morreu
    if (hp_ryu<=0):
        hp_ryu = 0
        fim = 1
    elif hp_ken<=0 :
        hp_ken = 0
        fim=1

# Impressão do vencedor e do número de golpes aplicados
    #Voltar com os valores iniciais de HP dos lutadores

hp_ryu = hp_ryu_impressao
hp_ken = hp_ken_impressao

#print(seq_golpes)
#print(len(seq_golpes))

while((hp_ken>0 or hp_ryu>0) and i<len(seq_golpes)):
    if seq_golpes[i] < 0:
        #golpe realizado pelo hp_ken
        #print("golpe sendo realizado no momento:", seq_golpes[i],i)
        conta_golpes_ken = conta_golpes_ken + 1;
        golpe_atual = int(seq_golpes[i])
        print("KEN APLICOU UM GOLPE:", abs(golpe_atual))
        hp_ryu = hp_ryu - abs(golpe_atual)
        i=i+1

        if(hp_ryu<=0):
            hp_ryu = 0
            print("HP RYU = ", hp_ryu)
            print("HP KEN = ", hp_ken)
            print("LUTADOR VENCEDOR: KEN")
            print("GOLPES RYU = ", conta_golpes_ryu)
            print("GOLPES KEN = ", conta_golpes_ken)
        else:
            print("HP RYU = ", hp_ryu)
            print("HP KEN = ", hp_ken)
    else:
        conta_golpes_ryu = conta_golpes_ryu + 1;
        golpe_atual = int(seq_golpes[i])
        i=i+1
        print("RYU APLICOU UM GOLPE:", abs(golpe_atual))
        hp_ken = hp_ken - abs(golpe_atual)
        if (hp_ken<=0):
            hp_ken = 0
            print("HP RYU = ", hp_ryu)
            print("HP KEN = ", hp_ken)
            print("LUTADOR VENCEDOR: RYU")
            print("GOLPES RYU = ", conta_golpes_ryu)
            print("GOLPES KEN = ", conta_golpes_ken)
        else:
            print("HP RYU = ", hp_ryu)
            print("HP KEN = ", hp_ken)
