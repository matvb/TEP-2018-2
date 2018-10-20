#*---------------------------------------------*#
#*                                             *#
#*      Mateus Villas Boas - 115054675         *#
#*                                             *#
#*---------------------------------------------*# 

import time
import random

#Trabalho 3: Imprima todos os anagramas de uma palavra dada (qualquer) que:
#a) começam por vogal; e
#b) não tem três consoantes juntas; e
#c) a primeira ocorrência da letra "P", se houver, tem que ocorrer antes da primeira ocorrência da letra "G", se houver; e
#d) não tem duas letras iguais consecutivas.  


def backtracking(characters, noRep, current, contcons):
    
    # 1. verifique se o estado corrente merece tratamento especial
    #  (se é um estado "final")
    if len(current) == len(characters):
        print (''.join(current))
        return
        #return True  # encontrei!
    
    # 2. para cada "candidato a próximo passo", faça...
    for letra in noRep :
        
        #não usar letra demais
        if current.count(letra) == characters.count(letra):
            continue
        
        #a) começam por vogal;
        if len(current) == 0:
            if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
                continue  # esse número já apareço, não posso usá-lo!
        
        else:
        #b) não tem três consoantes juntas;
            if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
                contcons = contcons + 1
                if contcons > 3:
                    continue
                
            #d) não tem duas letras iguais consecutivas.    
            if letra == current[len(current)-1]:
                continue
        
        #c) a primeira ocorrência da letra "P", se houver, tem que ocorrer antes da primeira ocorrência da letra "G", se houver; 
        if letra == "g" and "p" in characters and "p" not in current:
            continue
          
        
        # 2.2 modifica o estado corrente usando o candidato
        current.append(letra)
        
        # 2.3 chamo recursivamente o próprio backtrack passando o novo estado
        backtracking(characters, noRep, current, contcons)    
        
        # 2.4 limpo a modificação que fiz
        current.pop()
        
    #if len(current) == 0:
    #    print("Não há mais anagramas!")



def remove_repetition(lista):
    noRep = list()
    for item in lista:
        if item not in noRep:
            noRep.append(item)
    return noRep
        

def main():
    word = input("Entre com a palavra que deseja o anagrama: ")
    characters = list(word)
    noRep = remove_repetition(characters)
    current = list()
    contcons = 0
    backtracking(characters, noRep, current, contcons)
#    print(word)


if __name__ == '__main__':
    main()



