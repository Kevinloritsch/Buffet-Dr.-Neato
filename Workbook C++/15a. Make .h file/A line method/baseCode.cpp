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
void writeMessage();
main()
{
	
      srand(time(NULL)); 
	writeMessage();
	cout << endl;
	writeMessage();
	cout << endl;
	writeMessage();
	cout << endl;
	cout << "hit a key" << endl;
	getch();

	for(int i=0;i< 500;i++)
	{
		writeMessage();
	}
}
//}
void writeMessage()
{
	cout << "Sevy ";
}

