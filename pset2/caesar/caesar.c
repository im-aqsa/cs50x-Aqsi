#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

char rotate(char c, int key);

int main(int argc, string argv[])
{
    // Must have exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check that argument is all digits
    string key_str = argv[1];
    for (int i = 0, len = strlen(key_str); i < len; i++)
    {
        if (!isdigit(key_str[i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(key_str);

    // Get plaintext from user
    string plaintext = get_string("plaintext:  ");

    // Print ciphertext
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        printf("%c", rotate(plaintext[i], key));
    }
    printf("\n");

    return 0;
}

char rotate(char c, int key)
{
    if (isupper(c))
    {
        return 'A' + (c - 'A' + key) % 26;
    }
    else if (islower(c))
    {
        return 'a' + (c - 'a' + key) % 26;
    }
    else
    {
        return c;
    }
}
