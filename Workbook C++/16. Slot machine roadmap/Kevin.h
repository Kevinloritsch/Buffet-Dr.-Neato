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
void writeMessage(string bob)
{
	cout <<bob;
}

void drawLine(int,char);
void drawLine(int length, char output)
{
	for(int counter=0;counter<length;counter++)
	{
		cout<<output;
	}
}

void drawBox(int, int, char);
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

void framedBox(int height, int length, int xcord, int ycord, char output);
void framedBox(int height, int length, int xcord, int ycord, char output)
{
	
			for(int counter=0;counter<height;counter++)
	{
		gotoxy(xcord, ycord);
		ycord++;
		for(int i=0;i<length;i++)
		{
			cout<<output;
		}
	}
	
			for(int counter=0;counter<height-2;counter++)
	{
		gotoxy(xcord+1, ycord-height+1);
		ycord++;
		for(int i=0;i<length-2;i++)
		{
			cout<<" ";
		}
	}
}


#endif


