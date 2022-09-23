#A. Is your horseshoe on the other hoof?
#Link (https://codeforces.com/problemset/problem/228/A)
"""
Valera the Horse is going to the party with friends. He has been following the fashion trends for a while, and he knows that it is very popular to wear all horseshoes of different color. Valera has got four horseshoes left from the last year, but maybe some of them have the same color. In this case he needs to go to the store and buy some few more horseshoes, not to lose face in front of his stylish comrades.

Fortunately, the store sells horseshoes of all colors under the sun and Valera has enough money to buy any four of them. However, in order to save the money, he would like to spend as little money as possible, so you need to help Valera and determine what is the minimum number of horseshoes he needs to buy to wear four horseshoes of different colors to a party.
"""

#code
s = input().split()
t = 0
l = len(s)
for i in range(l):
    x = s.pop()
    if x in s:
        t += 1
print(t)