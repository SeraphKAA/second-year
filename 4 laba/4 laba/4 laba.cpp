#include <iostream>
#include <iomanip>
#include <string>
#include <bitset>
#include <cmath>
#include <random>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>

using namespace std;


int Pow(int x, int n)
{
	if (n == 0) return 1;
	else if (n == 1) return x;
	else if (n % 2 == 0) return Pow(x * x, n / 2);
	else return Pow(x * x, n / 2) * x;
}

//Даны координаты точки на плоскости.Определить и вывести на экран номер
//квадранта, в который попадает точка.
void Zadanie1() { //Zadanie 1
	double x, y;
	cout << "Введите координаты точки через пробел, как 'x y': ";
	cin >> x >> y;
	cout << "\n(" << x << ", " << y << ")";
	if (x > 0 and y > 0) cout << "\nКоординаты точки находятся в первой четверти";
	else if (x > 0 and y < 0) cout << "\nКоординаты точки находятся в четвертой четверти"; 
	else if (x < 0 and y > 0) cout << "\nКоординаты точки находятся во второй четверти";
	else if (x < 0 and y < 0) cout << "\nКоординаты точки находятся в третьей четверти";
	else if (x == 0 and y == 0) cout << "\nначало координат";
	else "\nТочка находится на оси";

}

//Написать программу вычисления корней уравнения а*х*х+Ь*х+с=0. Значение корня
//квадратного от х возвращает функция стандартной библиотеки double sqrt(double x) (прототип в файле math.h).
double Zadanie2() { // zadanie 2
	setlocale(LC_ALL, "RU");
	int a, b, c;
	cout << "Введите значения a, b, c для квадратного уравнения вида a(x)^2 + bx + c = 0: ";
	cin >> a >> b >> c;
	if (a == 0) {
		cout << "Ошибка, нельзя делить на 0"; 
		return 0;
}
	double d = Pow(b, 2) - 4 * a * c;
	double x1, x2;
	if (d == 0) {
		cout << (~b + 1) << " " << d << " " << sqrt(d) << " " << (2 * a);
		x1 = (~b + 1) / (2 * a);
		cout << endl << "x1 = " << x1 << endl;
		return 0;
	}
	else {
		cout << (~b + 1) << " " << d << " " << sqrt(d) << " " << (2 * a);
		x1 = ((~b + 1) + sqrt(d)) / (2 * a);
		x2 = ((~b + 1) - sqrt(d)) / (2 * a);
		cout << endl << "x1 = " << x1 << endl << "x2 = " << x2 << endl;
		return 0;
	}
}

// Hаписать программу вычисления N! (использовать циклы for и do while).
int Zadanie3(int x) // zadanie 3
{
	int result = 1;
	while (x > 0) {
		if (x == 1) return result;
		result *= x; x--;
	}
	cout << result << endl;
	result = 1;
	for (int i = 0; i < x; i++) result *= i;
	cout << result << endl;
}

// Написать программу нахождения суммы квадратов всех нечетных чисел.
void Zadanie4() { //zadanie 4
	int result[] = {0, 0, 0, 0, 0, 0, 0};
	int x;
	int temp = 0;
	int temp2 = 0;
	cout << "Введите цифру с помощью которой мы будем выполнять 4 задание: ";
	cin >> x;
	for (int i = 0; i <= x; i++) {
		if (i % 2 != 0) {
			if (temp == i - 2) {
				// + 2 * temp * i	
				temp2 += Pow(temp, 2) + Pow(i, 2);
				cout <<"Значения для суммы квадратов: " << temp << " " << i << ". Ответ: " << temp2 << endl;
			}
			else temp = i;			
		}
	}
}

/*
Найти количество элементов одномерного массива А(10), в значении которых
установлен пятый бит.После этого у всех элементов массива инвертировать 3 бит и новые
значения записать в массив В(10).Вывести в шестнадцатеричном виде массивы А и В.	*/
void Zadanie5() {
	int A[10], B[10];
	for (int i = 0; i < 10; i++) {
		A[i] = rand();
	}

	cout << "Массив А = ";

	for (int i = 0; i < 10; i++) {
		cout << " " << A[i];
	}
	cout << endl;
	
	int count = 0;
	for (int i = 0; i < 10; i++) {
		if ((A[i] >> 4) % 2 == 1) {
			count++;
			cout << (A[i] >> 4) << endl;
		}
	}
	cout << "Всего элементов в массиве, у которых 5-ый бит это 1: " << count << endl;
	for (int i = 0; i < 10; i++) {
		if ((A[i] >> 2) % 2 == 0) {
			B[i] = A[i] + Pow(2, 3);
		}
		else B[i] = A[i];
	}

	cout << "Массив В = ";

	for (int i = 0; i < 10; i++) {
		cout << " " << B[i];
	}
	cout << endl;
}

//Найти среднее арифметическое положительных элементов главной и побочной
//диагоналей матрицы действительных чисел А(5Х5).
void Zadanie6() { //zadanie 6
	int A[5][5] = {0};
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			int temp = rand() * Pow(-1, j);
			A[i][j] = temp;
		}
	}

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cout << setw(8) << A[i][j];
		}
	cout << endl;
	}

	int count = 0;
	int result = 0;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			if (i == j and A[i][j] > 0) {
				count += 1;
				result += A[i][j];
			}
		}
	}
	result /= count;
	// сделать отрицательные числа и нахождение их суммы
	cout << "Сумма положительных элементов главной диагонали: " << result << endl;
	

	int n = 4;
	result = 0;
	count = 0;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			if (j == n) {
				if (A[i][j] > -1) {
					count += 1;
					result += A[i][j];		
				}
				n -= 1;
			}
		}
	}
	cout << "Сумма положительных элементов побочной диагонали: " << result / count << endl;

}


//Дана матрица целых чисел размера 5х9.Получить одномерный массив, состоящий из
//средних арифметических элементов каждого из столбцов, имеющих четные номера.Найти
//максимальный элемент одномерного массива.
void Zadanie7() { //Zadanie 7
	int A[5][9] = {0};
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 9; j++) {
			A[i][j] = rand();
		}
	}

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 9; j++) {
			cout << setw(8) << A[i][j];
		}
		cout << endl;
	}

	int result[9] = {0, 0, 0, 0, 0};
	for (int i = 0; i < 5; i++) {
		for (int j = 1; j < 9; j+= 2) {
				result[i] += A[i][j];
		}
	}
	int temp = -1;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 9; j++) {
			if (A[i][j] > temp) temp = A[i][j];
		}
	}
	cout << "Максимальный элемент в массиве: " << temp << endl;
	for (int i = 0; i < 5; i++) cout << i + 1 << " элемент в списке: " << double(result[i]) / 4.0 << endl;
}

//В реализации интерактивной игры необходимо отслеживать перемещение, в
//пределах игрового поля, объекта, управляемого игроком.Представим в программе игровое поле
//массивом целых значений Агеа(20Х20).В начале все элементы имеют значение ноль.Положение
//перемещаемого объекта в конкретный момент времени можем задать, изменяя значение нужного
//элемента Area с нуля на единицу.После нескольких перемещений "след", оставляемый объектом будет
//выглядеть как цепочка единиц в поле нулей.Напишите собственную функцию int move(), которая, с
//помощью функции int getch() (прототип в файле conio.h), возвращающей код нажатой клавиши,
//определяет, в какую сторону сместился объект за один ход и возвращает 0, если сделан неправильный
//ход, -1, если сделан шаг влево, 1 - шаг вправо, -11 - вверх и 11 - вниз(можно использовать любые другие
//значения).Пользователь должен нажимать на клавиши с символами L или I, R или г, U или u, D ИЛИ d,
//соответственно.Используйте оператор switch.Напишите программу тест, создающую игровое поле, вызывающую некоторое число раз функцию move и отображающую на экране результат.
int move(char per) {

	switch (per) {
	case 'w':
	case 'W':
		return -11;
	case 'a':
	case 'A':
		return -1;
	case 's':
	case 'S':
		return 11;
	case 'd':
	case 'D':
		return 1;
	case '*':
		return 1000;
	}

}

void Zadanie8() {
	int Area[20][20] = { {0} }; int it = 10; int jt = 10; Area[it][jt] = 1;
	int a = 0;

	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			cout << " " << Area[i][j];
		}
		cout << endl;
	}
	
	while (1) {
		char z = _getch();
		a = move(z);
		if (a != 1000) {
			system("cls");
			switch (a) {
			case 1:
				jt += 1;
				Area[it][jt] = 1;
				break;
			case -1:
				jt -= 1;
				Area[it][jt] = 1;
				break;
			case 11:
				it += 1;
				Area[it][jt] = 1;
				break;
			case -11:
				it -= 1;
				Area[it][jt] = 1;
				break;
			}

			for (int i = 0; i < 20; i++) {
				for (int j = 0; j < 20; j++) {
					cout << " " << Area[i][j];
				}
				cout << endl;
			}
		}
		else break;
	}
}

int main()
{
	setlocale(LC_ALL, "RU");
	//Zadanie1();
	//Zadanie2();
	

	//int x; cout << "Напишите число для нахожждения оного факториала: "; cin >> x;
	//Zadanie3(x);
	
	//Zadanie4(); 
	//Zadanie5();
	//Zadanie6();	//++
	//Zadanie7();	//++
	//Zadanie8();
}
