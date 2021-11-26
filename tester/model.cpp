#include <bits/stdc++.h>
 
typedef long long ll;
 
#define M 1000000007
#define N (1 << 19)
 
using namespace std;
 
ll tree[2*N];
 
void add(int k, ll x) {
  k += N;
  tree[k] += x;
  for (k /= 2; k >= 1; k /= 2) {
    tree[k] = (tree[2*k] + tree[2*k+1]) % M;
  }
}
 
ll cnt(int lim) {
  if (lim < 0) return 0;
  int a = N;
  int b = lim + N;
  ll s = 0;
  while (a <= b) {
    if (a % 2 == 1) s += tree[a++];
    if (b % 2 == 0) s += tree[b--];
    a /= 2; b /= 2;
  }
  return s;
}
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n;
	cin >> n;
  vector<int> v(n);
  set<int> nums;
  map<int, int> mp;
	for (int i = 0; i < n; ++i) {
    cin >> v[i];
    nums.insert(v[i]);
	}
 
  for (int i = 0; i < n + N; ++i) tree[i] = 0;
 
  int c = 0;
  for (int x : nums) mp[x] = c++;
 
  ll ans = 0;
 
  for (int i = 0; i < n; ++i) {
    int val = mp[v[i]];
    ll c = (cnt(val - 1) + 1) % M;
    //cout << c << endl;
    ans = (ans + c) % M;
    add(val, c);
  }
 
  cout << ans;
 
	return 0;
}