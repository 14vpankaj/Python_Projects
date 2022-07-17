"""
Anagrams are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc.
Grouping anagrams is one of the popular questions in coding interviews. So if you want to learn how to solve the problem
of grouping anagrams, this article is for you. In this article, I will take you through a tutorial on how to group anagrams
using Python.

"""

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))