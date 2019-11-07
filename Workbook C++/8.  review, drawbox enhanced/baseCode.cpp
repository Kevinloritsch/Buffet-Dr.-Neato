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
	char joe;
	int sam;
	int daniel;
	int numy = 10;
	int numx;
	int xc;
	int yc;
	int dylan;
	cout<<endl<<"Please enter...a SYMBOL: ";
	cin>>joe;
	cout<<endl<<"Please enter...the length (ints only): ";
	cin>>sam;
	cout<<endl<<"Please enter...the height (ints only): ";
	cin>>dylan;
	cout<<endl<<"Please enter...the x-coordinate (ints only): ";
	cin>>xc;
	cout<<endl<<"Please enter...the y-coordinate (ints only--choose a number after 10): ";
	cin>>yc;
	cout<<endl<<endl<<endl;
	gotoxy(xc,yc);
	for(daniel=0;daniel<dylan;daniel++)
	{
		gotoxy(numx+xc, numy+yc);
		numy++;
		for(int i=0;i<sam;i++)
		{
			cout<<joe;
		}

		
	}
	

	
}
