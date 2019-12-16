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

int random(int r)
{
    return rand()% r + 1;
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
void sevmos();
void sevmos()
{
	cout<<"H";
	Sleep(50);
	cout<<"";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"T";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"!";
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                       ";
	gotoxy(0,0);
	Sleep(500);
	cout<<"W";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"l";
	Sleep(50);
	cout<<"c";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"g";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"l";
	Sleep(50);
	cout<<"y";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"d";
	Sleep(50);
	cout<<"v";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"n";
	Sleep(50);
	cout<<"c";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"d";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"c";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"p";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"n";
	Sleep(50);
	cout<<"g";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"p";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"g";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"!";
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                                                          ";
	gotoxy(0,0);
	Sleep(500);
	cout<<"I";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"p";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"n";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"y";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"k";
	Sleep(50);
	cout<<"n";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"w";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"w";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"d";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<".";
	Sleep(500);
	cout<<".";
	Sleep(500);
	cout<<".";
	Sleep(50);
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                                                          ";
	gotoxy(0,0);
	Sleep(500);
	cout<<"T";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"d";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"v";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"c";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"x";
	Sleep(50);
	cout<<"+";
	Sleep(50);
	cout<<"b";
	Sleep(50);
	cout<<"!";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"P";
	Sleep(50);
	cout<<"l";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"n";
	Sleep(50);
	cout<<"p";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"y";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"n";
	Sleep(50);
	cout<<"d";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"b";
	Sleep(50);
	cout<<"!";
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                                                               ";
	gotoxy(0,0);
	Sleep(500);
	cout<<"W";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"y";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"?";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	double m;
	cin>>m;
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                                                               ";
	gotoxy(0,0);
	Sleep(500);
	cout<<"W";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"s";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"y";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<"u";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"b";
	Sleep(50);
	cout<<"?";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	int b;
	cin>>b;
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                                                               ";
	gotoxy(0,0);
	cout<<"T";
	Sleep(50);
	cout<<"i";
	Sleep(50);
	cout<<"m";
	Sleep(50);
	cout<<"e";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"t";
	Sleep(50);
	cout<<"o";
	Sleep(50);
	cout<<" ";
	Sleep(50);
	cout<<"g";
	Sleep(50);
	cout<<"r";
	Sleep(50);
	cout<<"a";
	Sleep(50);
	cout<<"p";
	Sleep(50);
	cout<<"h";
	Sleep(50);
	cout<<"!";
	Sleep(500);
	gotoxy(0,0);
	cout<<"                                                                                               ";
	gotoxy(90,1);
	int down;
	cout<<"^";
	int counter = 0;
	down = 2;
	while(counter<44)
	{
		
		gotoxy(90, down);
		down++;
		cout<<"|";
		counter++;
		if(counter>=44)
		{
			break;
		}
	}
	gotoxy(90,45);
	cout<<"v";
	gotoxy(0,22);
	cout<<"<";
	int ocounter;
	ocounter = 0;
	int goright;
	goright = 2;
	while(ocounter<92)
	{
		gotoxy(goright, 22);
		goright++;
		goright++;
		cout<<"-";
		ocounter++;
		if(ocounter>=170)
		{
			break;
		}
	}
	cout<<">";
	gotoxy(91,12);
	cout<<"10";
	gotoxy(91,32);
	cout<<"-10";
	gotoxy(70,23);
	cout<<"-10";
	gotoxy(50,23);
	cout<<"-20";
	gotoxy(30,23);
	cout<<"-30";
	gotoxy(110,23);
	cout<<"10";
	gotoxy(130,23);
	cout<<"20";
	gotoxy(150,23);
	cout<<"30";
	
	gotoxy(90,22-b);
	cout<<"*";
	if(m==1 || m==2 || m==3 || m==4 || m==5 || m==6 || m==7 || m==8 || m==9 || m==10 || m==11 || m==12 || m==13 || m==14 || m==15 || m==16 || m==17 || m==18 || m==19 || m==20) 
	{
	gotoxy(90+2,22-b-m);
	cout<<"*";
	gotoxy(90-2,22-b+m);
	cout<<"*";
	if(m==1 || m==2 || m==3 || m==4 || m==5 || m==6 || m==7 || m==8|| m==9 || m==10)
	{
		gotoxy(90+4,22-b-m-m);
		cout<<"*";
		gotoxy(90-4,22-b+m+m);
		cout<<"*";
	}
	if(m==1 || m==2 || m==3 || m==4 || m==5)
	{
		gotoxy(90+6,22-b-m-m-m);
		cout<<"*";
		gotoxy(90-6,22-b+m+m+m);
		cout<<"*";
	}
	if(m==1 || m==2)
	{
		gotoxy(90+8,22-b-m-m-m-m);
		cout<<"*";
		gotoxy(90-8,22-b+m+m+m+m);
		cout<<"*";
	}
	}
	int parentmxb;
	parentmxb;
	int goxparent;
	goxparent = 45;
	int goyparent;
	goyparent = 44;

	for(parentmxb = 1; parentmxb<45; parentmxb++)
	{
		gotoxy(goxparent, goyparent);
		cout<<"/";
		goxparent++;
		goxparent++;
		goyparent=goyparent-1;
	}
		
	Sleep(20000);
	while(true)
	{
	gotoxy(3,50);
	cout<<"Want to know a specific y value? Please input a x-value.   ";
	double find;
	cin>>find;
	double answer;
	answer=m*find + b;
	cout<<endl<<endl<<"The answer is "<<answer<<"!";
	char again;
	cout<<endl<<endl<<"Want to find another? Hit any char (this will reset how you find a value, then after you hit enter, input a value)except q; q is to continue...into to the unknown :(.   ";
	cin>>again;
	if(again!='q')
	{
		gotoxy(3,50);
		cout<<"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ";
		getch();
	}
	if(again == 'q')
	{
	gotoxy(0,0);
	cout<<"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ";
	gotoxy(0,0);
	break;
	}
	}
//	gotoxy(0,0);
//	cout<<"N";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<"w";
//	Sleep(50);
//	cout<<"-";
//	Sleep(50);
//	cout<<"I";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<" ";
//	cout<<"t";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"m";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<"n";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"p";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"b";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<"!";
//	Sleep(500);
//	gotoxy(0,0);
//	cout<<"                                                       ";
//	gotoxy(0,0);
//	Sleep(500);
//	cout<<"W";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"w";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"y";
//	Sleep(50);
//	cout<<"=";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"(";
//	Sleep(50);
//	cout<<"x";
//	Sleep(50);
//	cout<<"-";
//	Sleep(50);
//	cout<<"h";
//	Sleep(50);
//	cout<<")";
//	Sleep(50);
//	cout<<"^";
//	Sleep(50);
//	cout<<"2";
//	Sleep(50);
//	cout<<"+";
//	Sleep(50);
//	cout<<"k";
//	Sleep(50);
//	cout<<"!";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"Y";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"w";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"f";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"n";
//	Sleep(50);
//	cout<<"p";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"v";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<"x";
//	Sleep(50);
//	cout<<"!";
//	Sleep(50);
//	Sleep(500);
//	gotoxy(0,0);
//	cout<<"                                                                    ";
//	gotoxy(0,0);
//	cout<<"W";
//	Sleep(50);
//	cout<<"h";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"y";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"h";
//	Sleep(50);
//	cout<<"?";
//	Sleep(50);
//	cout<<"  ";
//	Sleep(50);
//	int h;
//	cin>>h;
//	Sleep(50);
//	Sleep(500);
//	gotoxy(0,0);
//	cout<<"                                                       ";
//	gotoxy(0,0);
//	cout<<"W";
//	Sleep(50);
//	cout<<"h";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"y";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"k";
//	Sleep(50);
//	cout<<"?";
//	Sleep(50);
//	cout<<"  ";
//	Sleep(50);
//	int k;
//	cin>>k;
//	Sleep(500);
//	gotoxy(0,0);
//	cout<<"                                                                                               ";
//	gotoxy(0,0);
//	cout<<"N";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<"w";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"p";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"s";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"n";
//	Sleep(50);
//	cout<<"p";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"n";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"v";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"l";
//	Sleep(50);
//	cout<<"u";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<"!  ";
//	int a;
//	cin>>a;
//	Sleep(500);
//	gotoxy(0,0);
//	cout<<"                                                                                               ";
//	gotoxy(0,0);
//	cout<<"T";
//	Sleep(50);
//	cout<<"i";
//	Sleep(50);
//	cout<<"m";
//	Sleep(50);
//	cout<<"e";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"t";
//	Sleep(50);
//	cout<<"o";
//	Sleep(50);
//	cout<<" ";
//	Sleep(50);
//	cout<<"g";
//	Sleep(50);
//	cout<<"r";
//	Sleep(50);
//	cout<<"a";
//	Sleep(50);
//	cout<<"p";
//	Sleep(50);
//	cout<<"h";
//	Sleep(50);
//	cout<<"!";
//	Sleep(500);
//	gotoxy(0,0);
//	cout<<"                                                                                               ";
//	gotoxy(50,1);
//		cout<<"^";
//		int y =2;
//	for(int counter = 0; counter<20; counter++)
//	{
//		
//		gotoxy(50,y);
//		cout<<"-";
//		y++;
//		
//	}
//	gotoxy(50,21);
//	cout<<"v";	
//	gotoxy(0,10);
//	cout<<"<";
//	int x=2;
//	for(int counter = 0; counter<100; counter++)
//	{
//		
//		gotoxy(x,10);
//		cout<<"-";
//		x++;
//		
//	}
//	gotoxy(101,10);
//	cout<<">";
//	gotoxy(50-h,10-k);
//	cout<<"*";
//	gotoxy(50-h+1,10-k-a);
//	cout<<"*";
//	gotoxy(50-h-1,10-k-a);
//	cout<<"*";
//	if(a==2)
//	{
//		gotoxy(50-h+2,10-k-8);
//		cout<<"*";
//		gotoxy(50-h-2,10-k-8);
//		cout<<"*";
//	}
//	if(a==-2)
//	{
//		gotoxy(50-h+2,10-k+8);
//		cout<<"*";
//		gotoxy(50-h-2,10-k+8);
//		cout<<"*";
//	}		
	
}

#endif


