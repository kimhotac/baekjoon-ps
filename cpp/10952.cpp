#include <iostream>
using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int a, b;
	while (cin >> a >> b, a || b) {
		cout << a + b << '\n';
	}
	return 0;
}