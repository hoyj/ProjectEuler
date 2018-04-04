/*
 * Project Euler Problem #19
 *
 * Information about calendar dates -
 * 1) 1900/01/01 was Monday
 * 2) 4,6,9,11 have 30 days while 1,3,5,7,8,10,12 have 31 days.
 * 3) February usually has 28 days but on leap years it has 29 days
 * 4) leap years occurs every 4 years. However, every 100th year that
 *    is not divisible by 400 is NOT a leap year, but if divisible then it is.
 * 
 * In the 20th century(1901/01/01 - 2000/12/31), how many times is the first
 * day of the month a Sunday?
 */

#include <stdio.h>
#include <stdlib.h>

int getDays(int year, int month)
{
	if (month == 4 || month == 6 || month == 9 || month == 11)
		return 30;
	else if (month == 1 || month == 3 || month == 5 || month == 7 ||
			month == 8 || month == 10 || month == 12)
		return 31;
	else { // leap year
		if (year % 4 == 0) 
		{
			if (year % 100 == 0 && year % 400 != 0)
				return 28;
			else
				return 29;
		}else
			return 28;
	}
}

char* getName(int n)
{
	switch(n)
	{
		case 0: 
			return "Monday"; 
			break;
		case 1:
			return "Tuesday";
			break;
		case 2:
			return "Wednesday";
			break;
		case 3:
			return "Thursday";
			break;
		case 4:
			return "Friday";
			break;
		case 5:
			return "Saturday";
			break;
		case 6:
			return "Sunday";
			break;
		default:
			printf("[Error] calculating mod returned unknown value");
	}
}

int main()
{
	/* 
	 * 0 - Monday
	 * 1 - Tuesday
	 * 2 - Wednesday
	 * 3 - Thursday
	 * 4 - Friday
	 * 5 - Saturday
	 * 6 - Sunday
	 */
	int day = 1;
	int count = 0;
	for(int yr = 1901; yr < 2001; yr++)
	{
		for(int m = 1; m < 13; m++)
		{
			if (day == 6) 
			{
				count += 1;
				printf("%d/%d/1 was %s\n", yr, m, getName(day)); 
			}
			day = (day + getDays(yr, m)) % 7;
		}
	}	
	printf("%d days in 20th century were Sundays.", count);
	return 0;
}

