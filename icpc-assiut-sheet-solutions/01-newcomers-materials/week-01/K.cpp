#include <iostream>
#include<iomanip>

using namespace std;

int min(int a, int b);
int max(int a, int b);

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int min_val = min(a, b);
    min_val = min(min_val, c);

    int max_val = max(a, b);
    max_val = max(max_val, c);

    cout << min_val << " " << max_val <<endl;

    return 0;
}

int min(int a, int b) {return a < b? a:b;}

int max(int a, int b) {return a > b? a: b;}