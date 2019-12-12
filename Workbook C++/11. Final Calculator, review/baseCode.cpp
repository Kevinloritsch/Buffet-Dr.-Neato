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
	int length = 38;
	int height = 5;
	string blank = " ";
	int numy = 9;
	int numx =0 ;
	int i;
	int counter;
	int fred = height/2;
	char operation;
	double num1;
	double num2;
	int answerplus;
	int answerminus;
	int answertimes;
	int answerdivide;

	
	cout<<endl<<"Please enter...a SYMBOL: ";
	cin>>character;
	cout<<endl<<"Please enter a NUMBER: ";
	cin>>num1;
	cout<<endl<<"Please enter a OPERATOR (meaning +,-,*,/):  ";
	cin>>operation;
	cout<<endl<<"Please enter a SECOND NUMBER:  ";
	cin>>num2;


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
	if(operation == '+')
	{
		gotoxy (2,11);
		answerplus = num1 +num2;
		cout<<num1<<" "<<operation<<" "<<num2<<" = "<<answerplus;
	}
	if(operation == '-')
	{
		gotoxy (2,11);
		answerminus = num1 -num2;
		cout<<num1<<" "<<operation<<" "<<num2<<" = "<<answerminus;
	}
		if(operation == '*')
	{
		gotoxy (2,11);
		answertimes = num1 *num2;
		cout<<num1<<" "<<operation<<" "<<num2<<" = "<<answertimes;
	}
		if(operation == '/')
	{
		gotoxy (2,11);
		answerdivide = num1 /num2;
		cout<<num1<<" "<<operation<<" "<<num2<<" = "<<answerdivide;
	}


	getch();
	gotoxy(numx,numy+fred);

}
