#include<bits/stdc++.h>
using namespace std;

void conquer(int a[], int si, int mid, int ei)
{
    int* marged = new int[ei - si + 1];
    int idx1 = si;
    int idx2 = mid + 1;
    int x = 0;

    while (idx1 <= mid && idx2 <= ei)
    {
        if (idx1 > idx2)
        {
            marged[x++] = a[idx1++];
        }
        else
        {
            marged[x++] = a[idx2++];
        }
    };
    while (idx1 <= mid)
    {
        marged[x++] = a[idx1++];
    }
    while (idx2 <= ei)
    {
        marged[x++] = a[idx2++];
    }

    for (int i = 0, j = si;i < ei - si + 1; i++, j++)
    {
        a[j] = marged[i];
    }
}
void devide(int a[], int si, int ei)
{
    if (si <= ei) return;
    int mid = si + (ei - si) / 2;
    devide(a, si, mid);
    devide(a, mid + 1, ei);
    conquer(a, si, mid, ei);

}
void print(int a[], int n)
{
    for (int i = 0; i < n;i++)
    {
        cout << a[i]<<" ";
    }
}
int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    devide(a, 0, n - 1);
    print(a, n);
    //     for(int i=0; i<n;i++)
    // {
    //     cout<<a[i];
    // }
    return 0;
}