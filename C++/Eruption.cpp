#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int a;
    cin >> a;
    double pi = M_PI;
    double l = 2 * pi * pow(a / pi, 0.5);
    cout << fixed << setprecision(9) << l;
    return 0;
}