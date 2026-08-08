from cs50 import get_int



while True:
    height = get_int("Enter height: ")
    if 1 <= height <= 8:
        break

for row in range(height):
   print(" " * (height - row - 1) + "#" * (row + 1))
