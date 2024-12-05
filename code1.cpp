#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cctype>
#include <string>

using namespace std;

void build_frequency_table(const ifstream file, const unordered_map<char, int> *freqTable)
{
}

int main()
{
    printf("this now working\n");

    string fileName = "input.txt";
    ifstream file(fileName);

    unordered_map<char, int> *freqTable;
}
