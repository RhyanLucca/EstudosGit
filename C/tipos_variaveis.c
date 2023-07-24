#include <stdio.h> //Permite usar fun��es de entrada e saida de valores
#include <string.h> //Permite trabalhar com fun��es de string

int main(){

    //Declarar primeiro a variavel, depois o nome da variavel
    //Valor inteiro
    int idade;
    //valor flutuante, salario e altura
    double salario, altura;
    //valor de string mas com apenas um caracter
    char genero;
    //valor de string mas com um n�mero maior, por�m definido de caracteres
    char nome[50];

    idade = 18;
    salario = 5800.5;
    altura = 1.53;
    //Quando trata-se de um caracter, usase aspas simples
    genero = 'F';
    //Quando se trata de textos (vetor de char), usa-se uma fun��o e aspas duplas
    strcpy(nome, "Isabella Martins");

    printf("IDADE = %d\n", idade);
    printf("SALARIO = %.2lf\n", salario);
    printf("ALTURA = %.2lf\n", altura);
    printf("GENERO = %c\n", genero);
    printf("NOME = %s\n", nome);


    return 0;
}
