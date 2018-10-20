/*---------------------------------------------*/
/*                                             */
/*      Mateus Villas Boas - 115054675         */
/*                                             */
/*---------------------------------------------*/


#include <stdio.h>
#include <stdlib.h>

//struct contendo as estruturas de timestamp de nascimento e de morte
typedef struct life{
    int birth, death;
    struct life *next;
}t_life;


int main()
{  
    int i, j;
    int aux=0, aux2=0, maxTS=0, maxDeath=0, minBirth, cont=0;
    int b, d;
    int question = 1;
   
    //inicialização da lista encadeada   
    t_life *ini_life;
    t_life *next_life;
    ini_life = (t_life*) malloc(sizeof(t_life));
    if(ini_life==NULL)
        exit(1);
    
    next_life = ini_life;
   
    //preenchimento da lista encadeada
    while(question){
        printf("Insert Birth Year: ");
        scanf("%d", &next_life->birth);
        printf("Insert Death Year: ");
        scanf("%d", &next_life->death);
        
        if(cont=0){
            minBirth = next_life->birth;
        }
        else{
            if(next_life->birth<minBirth)
                minBirth = next_life->birth;
        }
        
        if(next_life->death>maxDeath)
            maxDeath=next_life->death;
            
        printf("Do you want to preceed? <1> YES, <other> NO ");
        scanf("%d", &question);
        
        if(question==1){
            next_life->next = (t_life*)malloc(sizeof(t_life));
            next_life = next_life->next;
        }
    }
    
    next_life->next = NULL;
    next_life = ini_life;
    
    //printar a tabela completa de nascimentos e mortes
    while(next_life!=NULL){
        printf("Birth: %d  Death: %d \n", next_life->birth, next_life->death);
        next_life = next_life->next;
    }
    
    //metodo para contar o máximo de pessoas vivas em um mesmo timestamp
    for(i=0; i<maxDeath; i++){
        next_life = ini_life;
        while(next_life!=NULL){
           if(next_life->birth==i){
                aux++;
                if(aux>aux2){
                    aux2=aux;
                    maxTS=i;
                }
            }
            if(next_life->death==i){
                aux--;
            }
            next_life = next_life->next;
        }
    }
   
   
    printf("\n The Year with most people alive was: %d",maxTS);
    //printf("\n %d",maxDeath);
    
    return 0;
}


