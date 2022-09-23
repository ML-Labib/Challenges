#1399B - Gifts Fixing
#Link (https://codeforces.com/problemset/problem/1399/B)
"""
You have n gifts and you want to give all of them to children. Of course, you don't want to offend anyone, so all gifts should be equal between each other. The i-th gift consists of ai candies and bi oranges.

During one move, you can choose some gift 1≤i≤n and do one of the following operations:

eat exactly one candy from this gift (decrease ai by one);
eat exactly one orange from this gift (decrease bi by one);
eat exactly one candy and exactly one orange from this gift (decrease both ai and bi by one).
Of course, you can not eat a candy or orange if it's not present in the gift (so neither ai nor bi can become less than zero).

As said above, all gifts should be equal. This means that after some sequence of moves the following two conditions should be satisfied: a1=a2=⋯=an and b1=b2=⋯=bn (and ai equals bi is not necessary).

Your task is to find the minimum number of moves required to equalize all the given gifts.

You have to answer t independent test cases.
"""
#