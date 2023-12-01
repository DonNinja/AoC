#include <string.h>

#include <fstream>
#include <iostream>
#include <regex>
using namespace std;

int main() {
    ifstream myfile("input2.txt", ios::in | ios::binary | ios::ate);
    streampos size;
    char* memblock;
    int* numbers = new int[2];
    // int result = 0;

    if (myfile.is_open()) {
        fill_n(numbers, 2, -1);
        size = myfile.tellg();
        memblock = new char[size];
        myfile.seekg(0, ios::beg);
        myfile.read(memblock, size);
        myfile.close();

        // printf("%s", memblock);

        for (int i = 0; i < size; i++) {
            char letter = memblock[i];
            int number = letter - '0';

            // printf("%c", letter);
            regex numRegex("[[:digit:]]");

            if (number > 0 && number <= 9) {
                // printf("Found number\n");
                if (numbers[0] == -1) {
                    printf("Found number %i and am adding it to the array \n",
                           number);
                    numbers[0] = number;
                    // atoi(&memblock[i]);
                }
                numbers[1] = number;
            }
            if (letter == '\n') {
                //* Reset num array & calculate new result
                printf("Resetting num array\n");
                fill_n(numbers, 2, -1);
            }
        }
        delete[] memblock;
    } else {
        cout << "Unable to open file";
    }

    delete[] numbers;

    return 0;
}