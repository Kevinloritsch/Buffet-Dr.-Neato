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
	int dylan;
	cout<<endl<<"Please enter...a SYMBOL: ";
	cin>>joe;
	cout<<endl<<"Please enter...the length (ints only): ";
	cin>>sam;
	cout<<endl<<"Please enter...the height (ints only): ";
	cin>>dylan;
	cout<<endl<<endl<<endl;
	
	for(daniel=0;daniel<dylan;daniel++)
	{
		gotoxy(numx, numy);
		numy++;
		for(int i=0;i<sam;i++)
		{
			cout<<joe;
		}

		
	}
	

	
}
