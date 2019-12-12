#ifndef _KEVIN_H_
#define	_KEVIN_H_


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




void writeMessage(string);
void writeMessage(string message)
{
	cout <<message;
}

void drawBox(int,int,char);
void drawBox(int height, int length, char output)
{	
int numy = 0;

		for(int counter=0;counter<height;counter++)
	{
		gotoxy(0, numy);
		numy++;
		for(int i=0;i<length;i++)
		{
			cout<<output;
		}
	}

}
   
     
#endif


