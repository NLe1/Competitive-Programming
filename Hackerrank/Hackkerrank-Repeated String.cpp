#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    long sLen = s.length();
    long time = n / sLen;
    long lastLen = n % sLen;
    long aOccur = 0;
    long res = 0;

    for(int i = 0; i < sLen; i++){
        if(s[i] == 'a') aOccur++;
    }

    res += aOccur * time;
    if(lastLen == 0) return res;

    aOccur = 0;

    for(int i = 0; i < lastLen;i++){
        if(s[i] == 'a') aOccur++;
    }

    return res + aOccur;
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}