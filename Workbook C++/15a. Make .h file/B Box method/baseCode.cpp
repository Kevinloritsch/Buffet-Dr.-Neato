// base code file

#include <iostream>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <sstream>
#include <fstream>
using namespace std;
void gotoxy(short x, short y) {
	COORD pos = {x, y};
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
	}
// generates a random number between 0 and r inclusive
int random(int r)
{
    return rand()% r + 1;
}  
///////////////////////////////////////////////////////////////////////
void drawBox();
main()
{
	
      srand(time(NULL)); 
  // write code here
  	drawBox();
      getch();
}









void drawBox()
{
	int numy = 0;
	for(int counter=0;counter<6;counter++)
	{
		gotoxy(0, numy);
		numy++;
		for(int i=0;i<4;i++)
		{
			cout<<'$';
		}
	}
}

