#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate and subtract quarters
    int quarters = calculate_quarters(cents);
    cents = cents - (quarters * 25);

    // Calculate and subtract dimes
    int dimes = calculate_dimes(cents);
    cents = cents - (dimes * 10);

    // Calculate and subtract nickels
    int nickels = calculate_nickels(cents);
    cents = cents - (nickels * 5);

    // Calculate and subtract pennies
    int pennies = calculate_pennies(cents);
    cents = cents - (pennies * 1);

    // Sum and print total coins
    int total_coins = quarters + dimes + nickels + pennies;
    printf("%i\n", total_coins);
}

// Calculate how many quarters fit into cents
int calculate_quarters(int cents)
{
    int quarters = 0;
    // Keep subtracting 25 while possible
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}

// Calculate how many dimes fit into remaining cents
int calculate_dimes(int cents)
{
    int dimes = 0;
    // Keep subtracting 10 while possible
    while (cents >= 10)
    {
        dimes++;
        cents = cents - 10;
    }
    return dimes;
}

// Calculate how many nickels fit into remaining cents
int calculate_nickels(int cents)
{
    int nickels = 0;
    // Keep subtracting 5 while possible
    while (cents >= 5)
    {
        nickels++;
        cents = cents - 5;
    }
    return nickels;
}

// Calculate how many pennies fit into remaining cents
int calculate_pennies(int cents)
{
    int pennies = 0;
    // Keep subtracting 1 while possible
    while (cents >= 1)
    {
        pennies++;
        cents = cents - 1;
    }
    return pennies;
}
