#include <iostream>
#include <string>
#include <bitset>
#include <cmath>

using namespace std;

int Pow(int x, int n)
{
	if (n == 0) return 1;
	else if (n == 1) return x;
	else if (n % 2 == 0) return Pow(x * x, n / 2);
	else return Pow(x * x, n / 2) * x;
}

int main()
{
   setlocale(LC_ALL, "RU");
// [+] Zadanie 2
// 
   //int k = 7, j = 12, i = 5;
   //k = (--i + 2 * j - k++, j-- + i - k);
   ////  {1} {5} {4} {6}{2}{9}{3}{7}{8}  
   //
   ////1)i = 4 
   ////5)26
   ////4)22 
   ////6)19
   ////2)k = 8, но из-за постинкремента в выражении 7 
   ////9)19, 8 = 8		ОТВЕТ
   ////3)j = 11 но из-за, постдекримента в выражении 12
   ////7)16
   ////8)8
   //
   //cout << k << endl;


// [+] Zadanie 3

   //int m, i, j, k, l;
   //cout << "Введите значения для i, j, k, l через пробел." << endl;
   //cin >> i >> j >> k >> l;

   //if (i > j + 2 * k) m = (i / 16) + (j * 128) - 17 + (k * 2) - (l / 32);
   //else m = (i / 16) + (j * 128) - 17 + (k * 2) + (l / 32);

   //if (i > j + 2 * k) m = (i >> 4) + (j << 7) - 17 + (k << 1) - (l >> 5);
   //else m = (i >> 4) + (j << 7) - 17 + (k << 1) + (l >> 5);
   //cout << m;


// [+] Zadanie 4

   /*
   int s1, s2;
   //s1 = 12, s2 = 21;
   cout << "Введите 2 целых числа через пробел." << endl;
   cin >> s1 >> s2;

   cout << hex << s1 << endl << s2 << endl;

   int d1 = s1 & s2, d2 = s1 | s2;
   s1 = s1 << 3, s2 = s2 >> 3;

   cout << hex << s1 << "     " << s2 << endl << d1 << "     " << d2 << endl;
   */

// [+] Zadanie 5

	/*
	char mas = 'g';
	int key = 0x424344;

	mas ^= key;
	cout << mas << endl;

	mas ^= key;
	cout << mas << endl;
	*/


// [+] Zadanie 6

   
   //int i;
   //cin >> i;
   //cout << bitset<16>(i) << endl;
   //i = (i & ~0xFFFF) | ((i & 0xFF) << 8) | ((i >> 8) & 0xFF);
   //cout << i << endl;
   //cout << bitset<16>(i);


// [+] Zadanie 7

   
   /*char z1 = 'g';
 
   cout << bitset<16>(z1) << endl;
   int number = (int)z1;
   int count = 0;
   cout << number << endl;
   do
   {
	   if (number % 2) count++;
	   number /= 2;
   } while (number);

   cout << count << endl;*/

   


// [+] Zadanie 8


   //char mask[] = { '_', '_', '_', '_', '_', '_', '_', '_' };
   //string as;
   //cout << "Напишите блоки которые хотите занять (1)" << endl;
   //cin >> as;
   //for (int i = 0; i < as.size(); i++) {
	  // mask[(int)as[i]] = '1';
	  // //cout << mask[(int)as[i]] << endl;
   //}
   //for (int i = 0; i < 8; i++) {

	  // cout << mask[i] << endl;
   //}


//int f = 0;
//bool castil;
//cout << "Битовая карта: " << bitset<8>(f) << endl << "занять блок 1; 0 нет" << endl;
//for (int i = 0; i < 8; i++) {
//	cout << "блок " << i + 1 << endl;
//	cin >> castil;
//	if (castil) f += pow(2, i);
//}
//
//cout << "Битовая карта: " << bitset<8>(f) << endl;
//cout << "освободить блок 1; 0 нет" << endl;
//
//for (int i = 0; i < 8; i++) {
//	cout << "блок " << i + 1 << endl;
//	cin >> castil;
//	if ((castil) && (f & Pow(2, i))) f &= ~Pow(2, i);
//}
//
//cout << "Битовая карта: " << bitset<8>(f) << endl;
//
//}

