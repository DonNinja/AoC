#include <string.h>

#include <fstream>
#include <iostream>
#include <regex>
using namespace std;

int main() {
    ifstream myfile("input2.txt", ios::in | ios::binary | ios::ate);
    streampos size;
    char* memblock;
    char* numbers = new char[2];
    int result = 0;

    if (myfile.is_open()) {
        fill_n(numbers, 2, NULL);
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
                if (numbers[0] == NULL) {
                    // printf("Found number %i and am adding it to the array
                    // \n",
                    //        number);
                    numbers[0] = letter;
                    // atoi(&memblock[i]);
                }
                numbers[1] = letter;
            }
            if (letter == '\n') {
                //* Reset num array & calculate new result
                printf("Numbers to add together: %c", numbers[0] + numbers[1]);
                // result += atoi(numbers[0] + numbers[1]);
                fill_n(numbers, 2, NULL);
            }
        }
        delete[] memblock;
    } else {
        cout << "Unable to open file";
    }

    delete[] numbers;

    return 0;
}