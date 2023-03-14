#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, k, d, s;
    cin >> n >> k >> d >> s;
    double x = static_cast<double>(n * d - s * k) / (n - k);
    if (x < 0 || x > 100) {
        cout << "impossible" << endl;
    } else {
        cout << fixed << setprecision(7) << x << endl;
    }
    return 0;
}