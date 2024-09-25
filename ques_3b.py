dp = []

def use_dp_to_find_correct_moves(T, nA, nB):
    global dp
    dp = [[(0, 0) for i in range(2*(T+1))] for i in range(T+1)]
    for i in range(1,T+1-int(nA+nB)//2):
        for j in range(nA,nA+(T-i-int(nA+nB)//2)*2+1):
            val = ((T-i)*2-j)/(2*(T-i))
            m = 1/3*(val + 7/10 + 5/11)
            E = [
                    m + m*dp[i-1][j+2][0] + (1-m)*dp[i-1][j][0],
                    9/20 + 14/45*dp[i-1][j+2][0] + 5/18*dp[i-1][j+1][0] + 37/90*dp[i-1][j][0],
                    329/660 + 93/330*dp[i-1][j+2][0] + 13/30*dp[i-1][j+1][0] + 94/330*dp[i-1][j][0]
                ]
            dp[i][j] = (max(E), E.index(max(E)))

    #print(*dp, sep = "\n")

def optimal_strategy(na, nb, tot_rounds, nA = 1, nB = 1):
    global dp
    nA = int(nA*2)
    nB = int(nB*2)
    na = int(na*2)
    nb = int(nb*2)
    use_dp_to_find_correct_moves(tot_rounds+int(nA+nB)//2, nA, nB)
    return [1 if i==dp[tot_rounds][na][1] else 0 for i in range(3)]


def expected_points(tot_rounds, na = 1, nb = 1):
    global dp
    na*=2
    nb*=2
    use_dp_to_find_correct_moves(tot_rounds+int(na+nb)//2, na, nb)
    return dp[tot_rounds][na][0]
    
