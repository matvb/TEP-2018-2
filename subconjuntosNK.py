#*---------------------------------------------*#
#*                                             *#
#*      Mateus Villas Boas - 115054675         *#
#*                                             *#
#*---------------------------------------------*# 


def backtrack(armazem, estado_corrente, n, k):
    
    # 1. verifique se o estado corrente merece tratamento especial
    #  (se é um estado "final")
    if len(estado_corrente) == k:
        if frozenset(estado_corrente) not in armazem:
            armazem.add(frozenset(estado_corrente))
            print(estado_corrente)
        #return True  # encontrei!
    
    # 2. para cada "candidato a próximo passo", faça...
    for candidato in range(1, n+1):
    
        # 2.1 se candidato é de fato um próximo passo válido (verifica as restrições)
        if candidato in estado_corrente:
            continue  # esse número já apareço, não posso usá-lo!

        # 2.2 modifica o estado corrente usando o candidato
        estado_corrente.append(candidato) 
        
        # 2.3 chamo recursivamente o próprio backtrack passando o novo estado
        backtrack(armazem, estado_corrente, n, k)    
        
        # 2.4 limpo a modificação que fiz
        estado_corrente.pop()


def subconjuntos(n, k):
    s = set()
    # crio o estado inicial
    subconj = []
    backtrack(s, subconj, n, k)

        
def main(): 
    n = eval(input('Entre com n '))
    k = eval(input('Entre com k '))
    subconjuntos(n, k)


main()


