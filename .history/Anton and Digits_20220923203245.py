#Anton and Digits
#Link (https://codeforces.com/problemset/problem/734/B)

"""
Recently Anton found a box with digits in his room. There are k2 digits 2, k3 digits 3, k5 digits 5 and k6 digits 6.

Anton's favorite integers are 32 and 256. He decided to compose this integers from digits he has. He wants to make the sum of these integers as large as possible. Help him solve this task!

Each digit can be used no more than once, i.e. the composed integers should contain no more than k2 digits 2, k3 digits 3 and so on. Of course, unused digits are not counted in the sum.
"""
#Code
n = list(map(int, input().split()))
n256 = min([n[0], n[2], n[3]])
n32 = min([n[1], n[0]- n256])
print(256 * n256 + 32 * n32)