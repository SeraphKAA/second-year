#define _CRT_SECURE_NO_WARNINGS

#include "stdio.h"
#include "windows.h"
#include "string.h"


int main() {

	//zadanie 1 +
	//int a, b, c;
	//scanf_s("%d %d %d", &a, &b, &c);
	//float cc = a + b + c;
	//printf("%f", cc);


	//zadanie 2 +

	
	int x2, y2, z2;
	char st1[4], st2[3], st3[3];
	char cost1[41];
	for (int i = 0; i < 40; i++) cost1[i] = '.';
	cost1[40] = '\0';
	scanf("%d %d %d", &x2, &y2, &z2);
	scanf("%s %s %s", &st1, &st2, &st3);
	//st1[3] = '\0', st2[3] = '\0', st3[3] = '\0';
	printf("%s%s%d\n", st1, cost1, x2);
	printf("%s%s%d\n", st2, cost1, y2);
	printf("%s%s%d\n", st3, cost1, z2);
	return 0;
	

	//zadanie 3 +

	
	//int x3;
	//float f3;

	//scanf_s("%d", &x3);
	//scanf_s("%f", &f3);

	//printf("Integer value x3 in 16 system is %x\n", x3);
	//printf("e-form of number f3 is %e\nRounding this number by 1, 2, 3 characters is %.1e, %.2e, %.3e\n", f3, f3, f3, f3);
	

	//zadanie 4 +

	
	//float x4 = 1.23456;
	//printf("%10.1f\n%10.2f\n%10.3f\n%10.4f\n", x4, x4, x4, x4);
	

	//zadanie 6 +


	//int x61, y61, x62, y62;
	//scanf_s("(%d,%d)\n", &x61, &y61);
	//scanf_s("(%d,%d)", &x62, &y62);
	//printf("Beginer of the segment is (%d, %d)\nEnd of the segment is (%d, %d)\n", x61, y61, x62, y62);


	//zadanie 7 +

	
	//char x7[9], x77[9] = {0};
	//scanf("%8s", x7);

	//for (int i = 1; i < 8; i++) {
	//	if (x7[i] == 'g') {
	//		x7[i + 1] == '\0';
	//		break;
	//	}
	//}
	//x7[7] = 'g';
	//x7[8] = '\0';
	//printf("%s", x7);
	




	/*for (int i = 0; i < 8; i++) {
		if (x7[i] == 'g') {
			if (8 - i > 0) {
				for (int j = i; j < 8; i++) x7[j] = '\0';
				break;
			}
		}

	}*/


	//zadanie 8 +

	
	//char x8, y8, z8[255];

	//scanf("%c%c%s", &x8, &y8, z8);
	//z8[254] = '\0';
	//printf("%c\n%c\n%s", x8, y8, z8);
	

	//zadanie 9 +

	
	//char v1[] = "Who are you?";
	//char v2[] = "What's your name?";
	//char v3[] = "You have a parents?";
	//char v4[] = "Doesn't your ma~ is a woman? ";
	//char v5[] = "Fill you deadly?";

	//char o1[255] = {0}, o2[255] = { 0 }, o3[255] = { 0 }, o4[255] = { 0 }, o5[255] = { 0 };
	////char o1[255] = "asdda", o2[255] = "asdasd", o3[255] = "asdasd132", o4[255] = "asdasd3213142", o5[255] = "asdasd321312314";

	//printf("%s\n", v1);
	//scanf("%s", o1);
	//system("cls");
	//printf("%s\n", v2);
	//scanf("%s", o2);
	//system("cls");
	//printf("%s\n", v3);
	//scanf("%s", o3);
	//system("cls");
	//printf("%s\n", v4);
	//scanf("%s", o4);
	//system("cls");
	//printf("%s\n", v5);
	//scanf("%s", o5);
	//system("cls");

	//char costt[] = "|--------------------------------------------------|";

	//printf("%s\n 1. %s\n%52s\n%s\n%52s\n%s\n%52s\n%s\n%52s\n%s\n%52s\n%s", costt, v1, o1, v2, o2, v3, o3, v4, o4, v5, o5, costt);
	//

	//zadanie 10 +


	/*char c1 = 'Q';
	wchar_t c2 = L'ß';
	printf("%c\n", c1);
	wprintf(L"Character = %c\n", c2);
	putchar(c1);
	putchar(c2);

	printf("%d\n%d", (int)sizeof(c1), (int)sizeof(c2));

	system("pause");
	return 0;*/


}
