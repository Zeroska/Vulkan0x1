#include<stdio.h>

void Input(int &kWh);
int Count(int kWh);
void Output(int kWh);

int main()
{
	int kWh;
	Input(kWh);
	Output(kWh);
	
}

void Output(int kWh)
{
	if(kWh>=0)
		printf("%.1f",Count(kWh)+(Count(kWh)*10.0/100));
	else	
		Count(kWh);
}

void Input(int &kWh)
{
	scanf("%d",&kWh);
}

int Count(int kWh)
{
	int Cost;
	if ( kWh < 0 )
		printf("-1");
	else if ( kWh >= 401 )
		Cost = 50*1678 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (kWh-400)*2927;
	else if ( kWh >= 301 )
		Cost = 50*1678 + 50*1734 + 100*2014 + 100*2536 + (kWh-300)*2834;
	else if ( kWh >= 201 )
		Cost = 50*1678 + 50*1734 + 100*2014 + (kWh-200)*2536;
	else if ( kWh >= 101 )
		Cost = 50*1678 + 50*1734 + (kWh-100)*2014;
	else if ( kWh >= 51 )
		Cost = 50*1678 + (kWh-50)*1734;
	else
		Cost = kWh*1678;
	return Cost;
}