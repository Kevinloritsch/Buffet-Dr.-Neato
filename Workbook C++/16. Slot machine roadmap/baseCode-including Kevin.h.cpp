#include "Kevin.h"
//writeMessage,drawBox,drawLine,framedBox
int random(int r)
{
    return rand()% r + 1;
}  
main()
{
	
      srand(time(NULL)); 
  	int credits;
  	int numberone;
	int numbertwo;
	int numberthree;

	

  	
  	
	framedBox(15,45,0,0,'$');
	framedBox(5,18,0,0,'$');
	framedBox(5,7,3,6,'$');
	framedBox(5,7,13,6,'$');
    framedBox(5,7,23,6,'$');
    gotoxy(3,12);
    writeMessage("Time to go in debt! :)");
	gotoxy(47,2);
	cout<<"How much to bet(limit of 100)?  ";
	cin>>credits;
	gotoxy(47,2);
	cout<<"                                             ";
	
	gotoxy(5,2);
	cout<<"$"<<credits;
	
	while(getch()!='q')
	{
	
	while(kbhit()==0)
	{
	numberone=random(25);
	numbertwo=random(25);
	numberthree=random(100);
		gotoxy(5,8);
	cout<<numberone<<" ";
	
		gotoxy(15,8);
	cout<<numbertwo<<" ";
		gotoxy(25,8);
	cout<<numberthree<<" ";
		
	}
	getch();
	char more = getch();
	if(more!='q')
  	{
  	
  		credits = credits-1;
  		gotoxy(5,2);
  		cout<<'$'<<credits<<" ";
  	
  	
  	
  		if(numberone==numbertwo)
	{
		credits = credits+10;
  		gotoxy(5,2);
  		cout<<'$'<<credits<<" ";
	}
		if(numberone==numberthree)
	{
		credits = credits+10;
  		gotoxy(5,2);
  		cout<<'$'<<credits<<" ";
	}
		if(numbertwo==numberthree)
	{
		credits = credits+10;
  		gotoxy(5,2);
  		cout<<'$'<<credits<<" ";
	}
	if(numberone==numbertwo==numberthree)
	{
		credits = credits+100;
  		gotoxy(5,2);
  		cout<<'$'<<credits<<" ";
	}
  	}
  		if(more == 'q')
	{
		break;
	}
	}
	
  	
  
  
  
  
  
  
  
  
getch();
cout<<endl<<endl<<endl<<endl<<endl<<endl<<endl<<endl<<endl<<endl<<endl<<endl<<endl;
}


