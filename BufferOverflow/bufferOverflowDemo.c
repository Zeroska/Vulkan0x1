#include "stdio.h"

int main(void)
{
    char buffer[10];
    gets(buffer); //does not check the size of the data
    puts(buffer);
}
