#include <iostream>
using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int t, a, b;
	cin >> t;
	for (int i=1; i<=t; i++) {
		cin >> a >> b;
		cout << "Case #" << i << ": " << a + b << '\n';
	}
	return 0;
}