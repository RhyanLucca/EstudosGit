#include <stdio.h>

int main(){

    //comando print
    printf("Bom Dia!\n");
    printf("Boa Noite!\n");

    //impirimindo variaveis
    //INTEIROS
    int x, y;

    x = 10;
    y=20;

    printf("%d\n", x);
    printf("%i\n", y);


    //NUMEROS DE PONTO FLUTUANTE
    double z;

    z=2.34567;

    //POr padrao a linguagem C imprime os 6 p´rimeiros caracteres

    //printf("%lf", z);

    //para imprimir apoenas os numeros que eu quero:
    printf("%.2lf\n\n", z);

    int idade;
    double salario;
    char nome[50];
    char sexo;

    idade = 18;
    salario = 10000;
    strcpy(nome, "Isabella martins");
    sexo = 'F';

    printf("A funcionaria %s,\n sexo: %c,\n ganha %.2lf e tem %d anos.", nome, sexo, salario, idade);

}
