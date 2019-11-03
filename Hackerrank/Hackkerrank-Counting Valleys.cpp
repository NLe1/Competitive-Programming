#include <bits/stdc++.h>

using namespace std;
int countingValleys(int n, string s) {
    int count = 0;
    bool inValley = false;
    int elev = 0;
    for(char x: s){
        if(x == 'U') elev++;
        else elev--;

        if(!inValley && elev < 0){
            inValley = true;
            count++;
        }

        if(inValley && elev >= 0){
            inValley = false;
        }
    }
    return count;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string s;
    getline(cin, s);
    int result = countingValleys(n, s);
    fout << result << "\n";

    fout.close();

    return 0;
}