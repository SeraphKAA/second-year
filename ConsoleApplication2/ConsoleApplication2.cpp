#include <iostream>
#include <string>
#include "consoleDLL.h"
#include <Windows.h>

using namespace std;

int main()

{
    clrscr(RED);
    gotoxy(3, 10);
    string name;
    cin >> name;
    cout << "Hello World and " << name << "!";

    //    int a = 12;
    //    int b = a++;
    //    std::cout << a << "\n" << b;


}
