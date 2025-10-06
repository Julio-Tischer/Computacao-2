#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{

    //Declarar matrizes de char, buffer e ponteiro de arquivo
    char** cpf =NULL;
    char buffer[100];
    char** nome =NULL;
    FILE* espionagem = NULL;

    //Alocar memoria para os nomes
    nome = (char**) malloc(3 * sizeof(char*));
    cpf = (char**) malloc(3 * sizeof(char*));

    //Perguntar dados
    for (int i=0;i<3;i++)
    {
        //Anotar e alocar nome
        printf("Digite o nome %d: ",i+1);
        fgets(buffer,100,stdin);
        nome[i] = (char*) malloc((strlen(buffer)+1) * sizeof(char));
        strcpy(nome[i],buffer);

        //Verificar Erros na alocação
        if (nome[i]== NULL)
        {
            printf("\n\n----Erro ao alocar memoria para o nome----\n\n");
            exit(0);
        }

        //Perguntar e alocar cpf
        printf("Digite o CPF %d: ",i+1);
        fgets(buffer,100,stdin);
        cpf[i] = (char*) malloc((strlen(buffer)+1) * sizeof(char));
        strcpy(cpf[i],buffer);

        //Verificar Erros na alocação
         if (nome[i]== NULL)
        {
            printf("\n\n----Erro ao alocar memoria para o CPF----\n\n");
            exit(0);
        }
    }

    //Criar um arquivo em binario para escrever os nomes e cpfs
    espionagem = fopen("espionagem.bin","wb");

    //Verificar se o arquivo foi aberto corretamente
    if (espionagem == NULL)
    {
        printf("\n\n----Erro ao abrir o arquivo----\n\n");
        exit(0);
    }
    
    //Escrever os nomes e cpfs
    for (int i=0;i<3;i++)
    {
        fwrite(nome[i], sizeof(char), 100,espionagem);
        fwrite(cpf[i], sizeof(char), 100, espionagem);

    }

    //Fecha arquivo
    fclose(espionagem);

    //Printar os nomes e cpfs -- Isso é debug
    /*for (int i=0;i<3;i++)
    {
        printf("\n\nNome %d: %s",i+1,nome[i]);
        printf("CPF %d: %s",i+1,cpf[i]);
    }*/

    //Zerar o cpf e o nome
    for (int i=0;i<3;i++)
    {
        free (cpf[i]);
        free (nome[i]);
    }

    //Abrir o aqruivo para ler
    espionagem = fopen("espionagem.bin","rb");

    //Verificar se o arquivo foi aberto corretamente
    if (espionagem == NULL)
    {
        printf("\n\n----Erro ao abrir o arquivo----\n\n");
        exit(0);

    }

    //Ler os nomes e cpfs do arquivo
    //Como sabemos que são 3 nomes e cpfs, vamos ler 3 vezes
    for (int i=0;i<3;i++)
    {
        fread(buffer, sizeof(char), 100, espionagem);
        nome[i] = (char*)malloc((strlen(buffer)+1) * sizeof(char));
        strcpy(nome[i],buffer);

        fread(buffer, sizeof(char), 100, espionagem);
        cpf[i] = (char*)malloc((strlen(buffer)+1) * sizeof(char));
        strcpy(cpf[i],buffer);
    }


    //Fecha o arquivo
    fclose(espionagem);

    //Printar os nomes e cpfs e liberar a memoria
    for (int i=0;i<3;i++)
    {
        printf("\n\nNome %d: %s\n",i+1,nome[i]);
        printf("CPF %d: %s\n",i+1,cpf[i]);

        free(nome[i]);
        free(cpf[i]);
    }

    //Liberar a memoria alocada
    free(nome);
    free(cpf);
    return 0;

    //Contemplem o mago do Malloc
    //Com suas alocações dinamicasss
}
