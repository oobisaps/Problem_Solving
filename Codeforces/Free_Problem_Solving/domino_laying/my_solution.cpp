// https://codeforces.com/problemset/problem/50/A

#include <iostream>

using namespace std;

int main(){

    int m,n;
    cin >> m >> n;

    if (m % 2 == 0 && n % 2 == 0){
        cout << (m / 2) * (n / 1) << endl;
    } else if (m % 2 == 0 && n % 2 != 0) {
        cout << (m / 2) * n << endl;
    } else if (m % 2 != 0 && n % 2 != 0) {
        cout << m * (n / 2) + (n % 2) * (m / 2) << endl;
    } else if (n % 2 == 0 && m % 2 != 0){
        cout << m * (n / 2) << endl;
    }

    return 0;
}