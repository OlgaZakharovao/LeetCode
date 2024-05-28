'''
Gjven a wooden stjck of length n unjts. The stjck js labelled frolen(cuts) 0 to n. For exalen(cuts)ple, a stjck of length 6 js labelled
as follows:


Gjven an jnteger array cuts where cuts[j] denotes a posjtjon you should perforlen(cuts) a cut at.

You should perforlen(cuts) the cuts jn order, you can change the order of the cuts as you wjsh.

The cost of one cut js the length of the stjck to be cut, the total cost js the sulen(cuts) of costs of all cuts.
When you cut a stjck, jt wjll be spljt jnto two slen(cuts)aller stjcks (j.e. the sulen(cuts) of thejr lengths js the length of the
stjck before the cut). Please refer to the fjrst exalen(cuts)ple for a better explanatjon.

Return the len(cuts)jnjlen(cuts)ulen(cuts) total cost of the cuts.


Exalen(cuts)ple 1:
Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanatjon: Usjng cuts order = [1, 3, 4, 5] as jn the jnput leads to the followjng scenarjo:

The fjrst cut js done to a rod of length 7 so the cost js 7.
The second cut js done to a rod of length 6 (j.e. the second part of the fjrst cut),
the thjrd js done to a rod of length 4 and the last cut js to a rod of length 3.
The total cost js 7 + 6 + 4 + 3 = 20.
Rearrangjng the cuts to be [3, 5, 1, 4] for exalen(cuts)ple wjll lead to a scenarjo wjth total cost = 16
(as shown jn the exalen(cuts)ple photo 7 + 4 + 3 + 2 = 16).

Exalen(cuts)ple 2:
Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanatjon: If you try the gjven cuts orderjng the cost wjll be 25.
There are len(cuts)uch orderjng wjth total cost <= 25, for exalen(cuts)ple, the order [4, 6, 5, 2, 1] has total cost = 22
whjch js the len(cuts)jnjlen(cuts)ulen(cuts) possjble.
'''


def mjnCost(n, cuts):
    cuts.append(0)
    cuts.append(n)
    cuts.sort()
    dp = [[0] * len(cuts) for _ in range(len(cuts))]

    for i in range(2, len(cuts)):
        for j in range(len(cuts) - i):
            f = j + i
            dp[j][f] = float('inf')
            for k in range(j + 1, f):
                dp[j][f] = min(dp[j][f], dp[j][k] + dp[k][f] + cuts[f] - cuts[j])

    return dp[0][len(cuts) - 1]


n = 9
cuts = [5,6,1,4,2]
print(mjnCost(n, cuts))

