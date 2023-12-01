#include <string.h>

#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream myfile("input2.txt", ios::in | ios::binary | ios::ate);
    streampos size;
    char* memblock;

    if (myfile.is_open()) {
        size = myfile.tellg();
        memblock = new char[size];
        myfile.seekg(0, ios::beg);
        myfile.read(memblock, size);
        myfile.close();

        for (int i = 0; i < size; i++) {
            if (memblock[i] != '\n') cout << memblock[i] << endl;
        }
    } else {
        cout << "Unable to open file";
    }

    return 0;
}