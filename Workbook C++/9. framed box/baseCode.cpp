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
main()
{
      srand(time(NULL)); 
  // write code here
	char character;
	int length;
	int height;
	string blank = " ";
	int numy = 8;
	int numx =0 ;
	int i;
	int counter;
	int fred = height/2;
	
	cout<<endl<<"Please enter...a SYMBOL: ";
	cin>>character;
	cout<<endl<<"Please enter...the length (ints only): ";
	cin>>length;
	cout<<endl<<"Please enter...the height (ints only): ";
	cin>>height;
	cout<<endl;

		for(counter=0;counter<height;counter++)
	{
		gotoxy(numx, numy);
		numy++;
		for(int i=0;i<length;i++)
		{
			cout<<character;
		}
	}
	
			for(counter=0;counter<height-2;counter++)
	{
		gotoxy(numx+1, numy-height+1);
		numy++;
		for(i=0;i<length-2;i++)
		{
			cout<<blank;
		}
	}

	getch();
	gotoxy(numx,numy+fred);

}
