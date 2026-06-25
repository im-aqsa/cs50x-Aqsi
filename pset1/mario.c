#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Keep asking until user gives a valid height (1-8)
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Outer loop: one iteration per row
    for (int i = 1; i <= height; i++)
    {
        // Inner loop 1: print spaces
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        // Inner loop 2: print hashes
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // Move to next line
        printf("\n");
    }
}
