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
void drawBox(int, int, int, int, char);
main()
{
	
      srand(time(NULL)); 
  // write code here
  	drawBox(5,5,5,5,'*');

      getch();
}

void drawBox(int length, int height,int x, int y, char symb)
{	


		for(int counter=0;counter<height;counter++)
	{
		gotoxy(x, y);
		y++;
		

		for(int i=0;i<length;i++)
		{
			cout<<symb;
			

		}
	}


}

