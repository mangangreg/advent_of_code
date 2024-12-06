#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <regex>
using namespace std;

int main(){
    cout << "hello, world!" << endl;

    ifstream file("./input.txt");
    // Check if the file was opened successfully
    if (!file.is_open()) {
        std::cerr << "Failed to open file!" << std::endl;
        return 1;
    }

    vector<string> lines;
    string line;
    while (getline(file, line)){
        lines.push_back(line);
    }
    file.close();
    regex pattern(R"((\d+)\s+(\d+))");
    smatch match;
    vector<int> nums_a;
    vector<int> nums_b;
    for (const string& line : lines){
        // Parse out first and second number using pattern
        if (regex_search(line, match, pattern)){
            nums_a.push_back(stoi(match[1].str()));
            nums_b.push_back(stoi(match[2].str()));
        }
    }
    sort(nums_a.begin(), nums_a.end());
    sort(nums_b.begin(), nums_b.end());

    int total = 0;
    for (int i = 0; i < nums_a.size(); i++){
        int diff = abs(nums_a[i] - nums_b[i]);
        cout << nums_a[i] << " " << nums_b[i] << " with a diff of " << diff <<endl;
        total += diff;
    }
    cout << "Total: " << total << endl;

    return 0;
};