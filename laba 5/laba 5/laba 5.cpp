// laba 5.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <iomanip>
#include <string>
#include <bitset>
#include <cmath>
#include <random>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>


using namespace std;

int Pow(int x, int n)
{
	if (n == 0) return 1;
	else if (n == 1) return x;
	else if (n % 2 == 0) return Pow(x * x, n / 2);
	else return Pow(x * x, n / 2) * x;
}


//В программе объявлен массив :
//int P[] = { 0, 2, 4, 5, 6, 7, 9, 12 };
//Какие значения примут выражения :
//а) P[3]; б)* P; в)* (P + 4); г)* (P + P[2]) ?

void Zadan1(int P[]) {
	cout << P[3] << endl;
	cout << *P << endl;
	cout << *(P + 4) << endl;
	cout << *(P + P[2]) << endl;
}



//Написать функцию, которая меняет местами значения двух
//переменных x и y.

void Zadanie2(int &x, int &y) { 
	int temp = x;
	x = y;
	y = temp;
}

void Zadan2() {
	int x1, y1;
	cout << "Запишите через пробел значения для x, y:";
	cin >> x1 >> y1;
	cout << "\nЗначение х изначально: " << x1 << "\nЗначение y изначально: " << y1 << endl;
	Zadanie2(x1, y1);
	cout << "\nЗначение х после: " << x1 << "\nЗначение y после: " << y1 << endl;
}


//Для решения различных задач используются методы Монте - Карло,
//предполагающие применение массивов случайных чисел с большим количеством
//элементов.Размер массива становится известным во время выполнения программы, т.е.массив должен создаваться динамически.Создайте две функции для
//решения одной и той же задачи : динамическое создание и заполнение случайными
//числами массива указанного размера.Первая функция должна использовать
//возвращаемое значение для передачи пользователю сгенерированного массива, а
//вторая должна передавать массив через один из своих аргументов.Стандартная
//библиотека Си содержит функции int rand() и void srand(unsigned) для генерации
//псевдослучайных чисел(прототипы в файле stdlib.h).

int* Zadanie31(int size) {
	int* arr = new int[size];
	for (int i = 0; i < size; i++) {
		arr[i] = rand() % 30;
	}
	return arr;
}

void Zadan31() {
	int size;
	cout << "Введите сколько будет элементов в массиве: ";
	cin >> size; cout << endl;
	int* arr = Zadanie31(size);
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
}



void Zadanie32(int*& arr, int size) {
	arr = new int[size];
	for (int i = 0; i < size; i++) {
		arr[i] = rand() % 30;
	}
}

void Zadan32() {
	int size;
	cout << "Введите сколько будет элементов в массиве: ";
	cin >> size; cout << endl;
	int* arr;
	Zadanie32(arr, size);
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
}


//Дана строка, содержащая текст на естественном языке.Напишите
//функцию, создающую новую строку, в которой все слова из старой строки следуют в
//обратном порядке и разделены одним знаком пробела.Исходная строка может
//содержать различные знаки - разделители(пробелы, запятые, точки и т.п.).Полный
//набор знаков - разделителей передается функции при ее вызове.

string Zadanie4(string& input,string& delimiters) {
	string as[10];
	string word;
	vector<string> words;
	set <char> mn; for (char delim : delimiters) mn.insert(delim);

	for (char i : input) {
		if (mn.find(i) != mn.end()) {
			words.push_back(word);
			word = "";
		}
		else {
			word = word + i;
		}
	}
	reverse(words.begin(), words.end());
	string output = "";
	for (string i : words) if (i != "") output = output + i + " ";
	return output;
}

void Zadan4() {
	string input = "Hello, ! asd das World!";
	string delimiters = ",! ";
	cout << "Изначальное предложение: " << input << "\nРазделители: " << delimiters << endl;

	string output = Zadanie4(input, delimiters);
	cout << output << endl;
}


//Напишите универсальную функцию для нахождения среднего геометрического отрицательных элементов матриц с произвольным числом строк и
//столбцов.Напишите программу - тест с промежуточной конструкцией, позволяющей
//передавать в функцию двумерные массивы.

double averageNegGeo(int numRows, int numCols, double** arr) {
	int countNeg = 0;
	double negProduct = 1;

	for (int i = 0; i < numRows; i++) {
		for (int j = 0; j < numCols; j++) {
			if (arr[i][j] < 0) {
				countNeg++;
				negProduct *= arr[i][j];
			}
		}
	}
	if (countNeg == 0) {
		return 0;
	}
	else if (countNeg % 2 != 0) {
		double negGeo = -1 * pow(fabs(negProduct), 1.0 / countNeg); // находим среднее геометрическое
		return negGeo;
	}
	double negGeo = pow(fabs(negProduct), 1.0 / countNeg); // находим среднее геометрическое
	return negGeo;
}


void Zadan5() {
	int numRows, numCols;

	cout << "Введите количество строк и столбцов матрицы: ";
	cin >> numRows >> numCols;

	double** arr = new double* [numRows];
	for (int i = 0; i < numRows; i++) {
		arr[i] = new double[numCols];
	}

	for (int i = 0; i < numRows; i++) {
		for (int j = 0; j < numCols; j++) {
			arr[i][j] = (rand() / 30.0) * -1;
		}
	}
	
	for (int i = 0; i < numRows; i++) {
		for (int j = 0; j < numCols; j++) {
			cout << setw(10) << arr[i][j];
		}
		cout << endl;
	}


	double negGeo = averageNegGeo(numRows, numCols, arr);

	cout << "Среднее геометрическое отрицательных элементов: " << negGeo << endl;
}

//Напишите функцию, строящую график заданной функции на заданном
//интервале изменения аргумента.Указатель на конкретную функцию и предельные
//значения аргумента передаются через аргументы.Алгоритм работы функции может
//быть таким : разбить интервал изменения аргумента на фиксированное число
//равновеликих подинтервалов и для каждого значения аргумента найти значение
//функции.Получим сетку значений аргумента и функции.Затем нужно провести
//масштабирование - перейти от действительных значений к целым - экранным
//координатам, полагая, что ось абсцисс направлена сверху - вниз, а ось ординат -
//слева - направо(график "лежит на боку").Точки, соответствующие значениям
//функции на сетке можно отображать с помощью какого - нибудь символа, например,
//звездочки.Схема масштабирования :
//double х, у; double yMin, уМах; /* минимальное и максимальное значения функции на
//заданном интервале изменения х */
//const int yScrMin = 1, yScrMax = 50; /* пределы изменения "экранной" координаты
//yScr */
//int yScr; /* координата на экране, соответствующая "физической" координате у */
///* найти yMin и YMax */
//У = f(x);
///* масштабирование */
//yScr = yScrMin + (у - yMin) / (yMax - yMin) * (yScrMax - yScrMin);
//Рисунок для функции у = x * x


// Задаем функцию, которую будем рисовать
double f(double x)
{
	return x * x * x;
}

// Функция для построения графика
void plot(double (*func)(double), double a, double b)
{
	// Задаем количество точек
	const int n = 8;
	// Рассчитываем шаг
	const double h = (b - a) / n;
	// Находим минимальное и максимальное значение функции на заданном интервале
	double yMin = INFINITY;
	double yMax = -INFINITY;
	for (double x = a; x <= b; x += h) {
		double y = func(x);
		if (y < yMin) {
			yMin = y;
		}
		if (y > yMax) {
			yMax = y;
		}
	}
	// Рассчитываем масштабирование
	const int yScrMin = 1;
	const int yScrMax = 50;
	for (double x = a; x <= b; x += h) {
		double y = func(x);
		// Вычисляем экранную координату yScr, соответствующую "физической" координате y
		int yScr = yScrMin + (y - yMin) / (yMax - yMin) * (yScrMax - yScrMin);
		// Рисуем точку на экране
		for (int i = yScrMin; i <= yScrMax; i++) {
			if (i == yScr) {
				cout << "*";
			}
			else {
				cout << " ";
			}
		}
		cout << endl;
	}
}


void Zadan6() {
	plot(f, -5, 5);
}

//Создайте текстовый, основанный на использовании меню, интерфейс пользователя для тестирования функций, содержащих алгоритмы решения
//заданий 1 - 4. Используйте массивы указателей.
int Zadan7() {
	int x;
	int P[] = { 0, 2, 4, 5, 6, 7, 9, 12 };
	while (true) {
		cout << "Для того, чтобы выбрать какую-то функцию, напишите соответствующее число, до 4 включительно.\nЕсли же напишите что-то другое, то вы выйдете из 7 функции.\nВыберите то, что вам надо: ";
		cin >> x;

		switch (x)
		{
		case 1:
			Zadan1(P); cout << endl; system("pause"); system("cls"); // +
			break;
		
		case 2:
			Zadan2(); cout << endl; system("pause"); system("cls"); //+
			break;
		
		case 3:
			Zadan31(); cout << endl; // system("pause"); system("cls"); //+
			Zadan32(); cout << endl; system("pause"); system("cls"); //+
			break;
		
		case 4:
			Zadan4(); cout << endl; system("pause"); system("cls"); //+
			break;

		default:
			return 0;
			break;
		}
	
	
	}

}



int main()
{
	setlocale(LC_ALL, "RU");
	//int P[] = { 0, 2, 4, 5, 6, 7, 9, 12 }; Zadan1(P); cout << endl; system("pause"); system("cls"); // +
	//Zadan2(); cout << endl; system("pause"); system("cls"); //+
	//Zadan31(); cout << endl; system("pause"); system("cls"); //+
	//Zadan32(); cout << endl; system("pause"); system("cls"); //+
	//Zadan4(); cout << endl; system("pause"); system("cls"); //+
	

	//Zadan5(); cout << endl; system("pause"); system("cls"); //+
	//Zadan6(); cout << endl; system("pause"); system("cls"); //+
	//Zadan7(); cout << endl; system("pause"); system("cls"); //+
	

}
