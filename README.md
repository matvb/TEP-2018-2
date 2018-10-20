# TEP-2018-2

Trabalhos da matéria Tópicos Especiais Em computação:
Professor: Vincius Gusmão

### Trabalho 1: Lifespan
Problema: dados o timestamp (exemplo: ano, ou dia, ou minuto, etc.) 
          de nascimento e de morte de cada uma de n pessoas, 
          determinar o timestamp em que havia a maior quantidade de pessoas vivas

Entrada: uma lista com n pares (timestamp_nascimento, timestamp_morte)
Saida: o timestamp no qual havia a maior quantidade de pessoas vivas

Exemplo: 
102, 11800000       L := tamanho do range de anos (ano_max - ano_min)
100, 130000000      l := range máximo vivido por alguma pessoa
80, 120000000
101, 103000000
90, 1020000000
                    102_________________118
              100_____________________________________130
      80_____________________________________120
                 101___103                              Algoritmo 1
           90_______102                                 Complexidade = O(l*n + L)

Resposta: 102                                   


___80+_______90+________100+_101+________102+_____________119-___121-______131-_____
                                             103- 104-


                                                        Algoritmo 2
                                                        Complexidade = O(n log n) 


   Algoritmo Composto (misturando os dois, escolhendo de acordo com o caso)
   Complexidade = O(Min{l*n + L, n log n})


### Trabalho 2: Subconjuntos NK
Encontre todos os subconjuntos de tamanho k do conjunto {1, 2, 3, ..., n}, para n e k dados.

### Trabalho 3: Anagrams
Imprima todos os anagramas de uma palavra dada (qualquer) que:
a) começam por vogal; e
b) não tem três consoantes juntas; e
c) a primeira ocorrência da letra "P", se houver, tem que ocorrer antes da primeira ocorrência da letra "G", se houver; e
d) não tem duas letras iguais consecutivas.  
