#define _CRT_SECURE_NO_WARNINGS

#include "stdio.h"
#include <stdlib.h>
#include <ctype.h>
#include "windows.h"
#include "string.h"
#include <locale.h>
#include <time.h>

//.Напишите подпрограмму, подсчитывающую количество символов в указанном
//файле, открыв его вначале как текстовый, затем как двоичный.В текстовом режиме
//нужно посчитать также число строк файла.

int Count_lines(char* filename) {
    int count = 0;
    FILE* fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("ошибкочкаааа....\n");
        return -1;
    }

    char c;
    while ((c = fgetc(fp)) != EOF) {
        if (c == '\n') {
            count++;
        }
    }

    fclose(fp);
    printf("Кол-во переходов в строке = %d\n", count);
    return count;
}


int Count_chars(char* filename) {
    int count = 0;
    FILE* fp = fopen(filename, "r"); // открытие файла в текстовом режиме
    if (fp == NULL) {
        printf("ошибкочкаааа....\n");
        return -1;
    }

    char c;
    while ((c = fgetc(fp)) != EOF) {
        count++;
    }
    fclose(fp);
    printf("Кол-во символов в файле, не учитывая переходы = %d\n", count);

    count = 0;
    fp = fopen(filename, "rb"); // открытие файла в двоичном режиме
    if (fp == NULL) {
        printf("ошибкочкаааа....\n");
        return -1;
    }

    while ((c = fgetc(fp)) != EOF) {
        count++;
    }

    printf("Кол-во символов в файле, открытом в двоичном файле = %d\n", count);
    fclose(fp);
    return count;
}


void Zadanie1()
{
    char filename[] = "C:\\Users\\79045\\Desktop\\6 txt\\zad 1\\1.txt";
    Count_lines(filename);
    Count_chars(filename);
}

//-----------------------------------------------------------------------------------------
//Файл содержит как русские, английские буквы и другие символы.Написать
//программу, которая русские буквы из данного файла переписывает в отдельный
//новый файл, английские буквы в другой файл.


void Zadanie2()
{
    setlocale(LC_ALL, "Russian");
    FILE* in_file = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 2\\row.txt", "r");
    if (in_file == NULL) {
        printf("ошибкочкаааа....\n");
        exit(1);
    }

    FILE* rus_file = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 2\\russian.txt", "w");
    if (rus_file == NULL) {
        printf("ошибкочкаааа....\n");
        exit(1);
    }

    FILE* eng_file = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 2\\english.txt", "w");
    if (eng_file == NULL) {
        printf("ошибкочкаааа....\n");
        exit(1);
    }

    int c;
    while ((c = fgetc(in_file)) != EOF) {
        if (isalpha(c)) {
            if (isupper(c) || islower(c)) {
                if (isalpha(c) && (c >= L'a' && c <= L'z' || c >= L'A' && c <= L'Z')) {
                    fputc(c, eng_file);
                }
                else {
                    fputc(c, rus_file);
                }
            }
        }
        else {
            fputc(c, rus_file);
        }
    }

    fclose(in_file);
    fclose(rus_file);
    fclose(eng_file);
}
//-----------------------------------------------------------------------------------------------
//Объявить одномерный массив и заполнить его случайными числами.Записать в
//файл все положительные элементы массива и их сумму.

void Zadanie3()
{
    srand(time(NULL)); // чтобы каждый раз генерировались разные случайные числа
    const int size = 10;
    int arr[10];
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 21 - 10; // заполнение массива случайными числами от -10 до 10
        printf("%d %d\n", i, arr[i]);
    }
    FILE* file = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 3\\3.txt", "w");
    int sum = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] > 0) {
            fprintf(file, "%d\n", arr[i]);
            sum += arr[i];
        }
    }
    fprintf(file, "Сумма положительных значений списка = %d\n", sum);
    fclose(file);

}
//-------------------------------------------------------------------------------------------------
/*Файл f1 содержит последовательность целых положительных чисел в 10 - й системе
счисления.Вывести на экран содержимое файла f1.Записать в файл f2 четные
числа из файла f1 в 8 - ой системе счисления.Записать в файл f3 нечетные числа из
файла f1 в 16 - ой системе счисления.Вывести файлы f2 и f3 на экран(при этом
выводится 10 символов, для продолжения вывода пользователь должен нажать
букву ―n‖).*/

void Zadanie4()
{
    FILE* f1, * f2, * f3;
    int num;

    // открытие файлов
    f1 = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 4\\f1.txt", "r");
    f2 = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 4\\f2.txt", "w");
    f3 = fopen("C:\\Users\\79045\\Desktop\\6 txt\\zad 4\\f3.txt", "w");
    int f_2[100]; int cf2 = 0;
    int f_3[100]; int cf3 = 0;
    // чтение из f1, запись в f2 или f3, вывод на экран
    while (fscanf(f1, "%d", &num) != EOF) {
        if (num % 2 == 0) {
            f_2[cf2] = num; cf2++;
            fprintf(f2, "%d- %o\n", num, num);
        }
        else {
            f_3[cf3] = num; cf3++;
            fprintf(f3, "%d- %X\n", num, num);
        }
    }

    int j = 0; int if2 = 0; int if3 = 0;
    while (j <= cf2 || j <= cf3 || (cf3 - j >= -10 || cf2 - j >= -10))
    {
        int tempj = j;
        j += 10;
        for (; tempj < j; tempj++) 
        {
            if (tempj % 2 == 0 && if2 < cf2)
            {
                printf("8-ричная система: %o\n", f_2[if2]); if2++;
            }
            else if (tempj % 2 != 0 && if3 < cf3)
            {
                printf("16-ричная система: %X\n", f_3[if3]); if3++;
            }
        }
        getchar();
        //printf("8-ричная система: ");
        //for (int temp = 0; temp < 10 && if2 < cf2; if2++) { printf("%o, ", f_2[if2]); temp++; }
        //printf("\n16-ричная система: ");
        //for (int temp = 0; temp < 10 && if3 < cf3; if3++) { printf("%X, ", f_3[if3]); temp++; }
        //printf("\n");
        
    }

    printf("\n");
    fclose(f1);
    fclose(f2);
    fclose(f3);
}
//--------------------------------------------------------------------------------------------
//В процессе проведения некоторого спортивного турнира должна сохраняться
//информация о показателях каждой участвующей в турнире команды.Информация
//включает в себя название команды, количества выигранных, проигранных и
//сведенных вничью партий, а также общее количество набранных баллов.
//Напишите функции для сохранения в файле и считывания из файла таблицы
//текущего состояния турнира.

struct Team
{
    char name[50];
    int wins;
    int losses;
    int draws;
    int points;
};

void saveToFile(struct Team teams[], int numTeams, const char* filename) {
    FILE* fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Failed to open file for writing\n");
        return;
    }
    for (int i = 0; i < numTeams; i++) {
        fprintf(fp, "%s,%d,%d,%d,%d\n", teams[i].name, teams[i].wins, teams[i].losses, teams[i].draws, teams[i].points);
    }
    fclose(fp);
}


void readFromFile(struct Team teams[], int* numTeams, const char* filename) {
    FILE* fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Failed to open file for reading\n");
        return;
    }
    int i = 0;
    while (fscanf(fp, "%[^,],%d,%d,%d,%d\n", teams[i].name, &teams[i].wins, &teams[i].losses, &teams[i].draws, &teams[i].points) != EOF) {
        i++;
    }
    *numTeams = i;
    fclose(fp);
}


void Zadanie5(const char* filename)
{

    struct Team teams[5] = {
      {"Team Alpha", 3, 1, 0, 10},
      {"Team Betta", 1, 1, 0, 5},
      {"Team Gamma", 0, 2, 2, 3},
      {"Team Delta", 0, 4, 1, 1}
    };

    int numTeams = 4;

    saveToFile(teams, numTeams, filename);

    numTeams = 0;
    readFromFile(teams, &numTeams, filename);

    printf("Кол-во команд: %d\n", numTeams);
    for (int i = 0; i < numTeams; i++) {
        printf("%s: Wins- %d, Losses- %d, Draws- %d, Points- %d\n", teams[i].name, teams[i].wins, teams[i].losses, teams[i].draws, teams[i].points);
    }

}

//--------------------------------------------------------------------------------------------
//Создайте текстовое меню для управления информацией о спортивном
//соревновании.Должно поддерживаться следующее поведение : создание таблицы
//результатов, отображение таблицы, изменение таблицы, сохранение таблицы в
//файле, считывание таблицы из файла.Таблица должна содержать информацию,
//указанную в предыдущем задании.

void addTeam(struct Team* team, int* size, const char* name, int wins, int losses, int draws, int points, int tempsize)
{
    int index = 0;
    int temp = 0;
    for (int i = 0; i < tempsize; i++)
    {
        /*printf("%s %s\n", team[i].name, name);*/
        if (strcmp(team[i].name, name) == 0)
        {
            index = i;
            temp = 1;
            /*printf("index - %d, temp- %d\n", index, temp);*/
            break;
        }
    }

    if (temp == 0)
    {
        struct Team newTeam;
        strcpy(newTeam.name, name);
        newTeam.wins = wins;
        newTeam.losses = losses;
        newTeam.draws = draws;
        newTeam.points = points;

        team[*size] = newTeam;
        (*size)++;
    }
    else 
    {
        struct Team asTeam;
        strcpy(asTeam.name, name);
        asTeam.wins = wins;
        asTeam.losses = losses;
        asTeam.draws = draws;
        asTeam.points = points;
    
        team[index] = asTeam;
    }

}


void zad6_3(Team team[50], int len)
{

}


void Zadanie6(const char* filename)
{
    struct Team teams[50] = {
      {"Alpha", 3, 1, 0, 10},
      {"Betta", 1, 1, 0, 5},
      {"Gamma", 0, 2, 2, 3},
      {"Delta", 0, 4, 1, 1}
    };
    int len_teams = 4;


    for (int i = 0; i < len_teams; i++) {
        printf("%s: Wins- %d, Losses- %d, Draws- %d, Points- %d\n", teams[i].name, teams[i].wins, teams[i].losses, teams[i].draws, teams[i].points);
    }
    printf("\n");

    int vibor = 0;
    int variable = 1;
    char tempname[50]; int tempwins = 0; int templosses = 0; int tempdraws = 0; int temppoints = 0;

    while (variable) {

        printf("\nрешите что вы хотите сделать:\n1) сохранить таблицу в файл;\n2) Прочитать таблицу из файла\n3) Изменить таблицу\n0) выйти\n");
        scanf("%d", &vibor);

        switch (vibor)
        {
        case 1:
            saveToFile(teams, len_teams, filename);
            system("cls");
            break;


        case 2:
            readFromFile(teams, &len_teams, filename);
            for (int i = 0; i < len_teams; i++) {
                printf("%s: Wins- %d, Losses- %d, Draws- %d, Points- %d\n", teams[i].name, teams[i].wins, teams[i].losses, teams[i].draws, teams[i].points);
            }
            getchar();
            break;


        case 3:
            printf("Напишите параметры новой команды как: название команды кол-во побед кол-во поражений кол-во ничьих кол-во очков\n");
            getchar();
            scanf("%s %d %d %d %d", &tempname, &tempwins, &templosses, &tempdraws, &temppoints);
            // scanf("\d \d \d \d", &tempwins, &templosses, &tempdraws, &temppoints); scanf("\s \d \d \d \d", &tempname, &tempwins, &templosses, &tempdraws, &temppoints);
            //system("pause");
            getchar();
            addTeam(teams, &len_teams, tempname, tempwins, templosses, tempdraws, temppoints, len_teams);
            
            for (int i = 0; i < len_teams; i++) {
                printf("%s: Wins- %d, Losses- %d, Draws- %d, Points- %d\n", teams[i].name, teams[i].wins, teams[i].losses, teams[i].draws, teams[i].points);
            }
            printf("\n");
            getchar();
            system("cls");
            break;


        case 0:
        default:
            variable = 0;
            break;
        }

    } 
    printf("пара-пара-пам\n");
}

int main()
{
    setlocale(LC_ALL, "Russian");
    //Zadanie1(); system("pause"); system("cls"); // +
    //Zadanie2(); system("pause"); system("cls"); // +
    //Zadanie3(); system("pause"); system("cls"); // +
    //Zadanie4(); system("pause"); system("cls"); // +
    //Zadanie5("C:\\Users\\79045\\Desktop\\6 txt\\zad 5\\teams.txt"); system("pause"); system("cls"); // +
    //Zadanie6("C:\\Users\\79045\\Desktop\\6 txt\\zad 6\\teams.txt"); system("pause"); system("cls"); //+
    return 0;
}