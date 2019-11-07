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
	char dylan;
	cout<<endl<<"Please enter...an Arhcetypal SYMBOL: ";
	cin>>joe;
	cout<<endl<<"Please enter...the length (ints only): ";
	cin>>sam;
	cout<<endl<<"Please enter h (if you want it to be horizantal) or v if you want your it to be vertical): ";
	cin>>dylan;
	cout<<endl;
	if(dylan == 'h')
	{
		for(daniel=0;daniel<=sam;daniel++)
		{
			cout<<joe;
			
		}
	}
	if(dylan == 'v')
	{
		for(daniel=0;daniel<=sam;daniel++)
		{
			cout<<endl<<joe;
			
		}
	}
//	
	
	  


      getch();
}


