#ifndef __CONDLL_DLL__
#define __CONDLL_DLL__

#include <Windows.h>

#define BLACK	0
#define WHITE	0xffffffu
#define RED		0xff0000u
#define GREEN	0xff00u
#define BLUE	0xff
#define YELLOW	0xffff00u
#define PURPLE	0xff00ffu
#define CYAN	0xffffu

__declspec(dllexport) void clrscr(int color = 0);
__declspec(dllexport) void setColors(int color, int bgColor);
__declspec(dllexport) void gotoxy(int col, int row);
__declspec(dllexport) int getRow();
__declspec(dllexport) int getColumn();

#endif
