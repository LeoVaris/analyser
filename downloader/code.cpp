#include <iostream>

using namespace std;

typedef long long ll;

int n;
int x[505050];
ll c;

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> x[i];
    for (int i = 2; i <= n; i++) {
        if (x[i] < x[i-1]) {
            c += x[i-1]-x[i];
            x[i] = x[i-1];
        }
    }
    cout << c << "\n";
}
