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
	
	int length = 7;
	int height = 5;
	string blank = " ";
	int numy = 0;
	int numx =0 ;
	int i;
	int counter;
	int fred = height/2;
	char more;
	int thx;
		for(counter=0;counter<height;counter++)
	{
		gotoxy(numx, numy);
		numy++;
		for(int i=0;i<length;i++)
		{
			cout<<"#";
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
	
	gotoxy(10,0);
	cout<<" Click a char to pause, and a key to continue. Otherwise, hit q: ";
	
	while(kbhit()==0)
	{
		gotoxy(2,2);
	cout<<random(100);
		
	
		gotoxy(2,2);
	cout<<"   ";
	gotoxy(2,2);
	cout<<random(100);

	
	thx = kbhit();
	if(thx != 0)
	{
		getch();
		char more = getch();
		if(more == 'y')
		{
			thx = 0;
		}
		if(more == 'q')
		{
			break;
		}		
	}
		
	}
	

	gotoxy(0,8);

}
