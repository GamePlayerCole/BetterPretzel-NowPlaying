string = "The quick brown fox jumped over the lazy dog"

array = string.split()

count = len(array)

int = 0

while int < count:
    print("The word for array [" + str(int) + "] is " + str(array[int]))
    int = int + 1
