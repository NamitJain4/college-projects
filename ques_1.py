"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""

"""
ENTRY NUMBER: CS1230483
T1T2 = 94
T3T4 = 83
T = 94 + 83 = 177
NO DRAWS (ONLY AGGRESSIVE GAMEPLAY)

"""

entry_no = "0483"

initial_points_Alice = 1
initial_points_Bob = 1

T1T2 = int("".join(["9" if i=="0" else i for i in entry_no[:2]]))
T3T4 = int("".join(["9" if i=="0" else i for i in entry_no[2:]]))
T = T1T2 + T3T4

M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# def mod_add(a, b):return a+b
# def mod_multiply(a, b): return a*b
# def mod_divide(a, b): return a/b


# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """

    dp = [[0]*(bob_wins+1) for i in range(alice_wins+1)]
    
    dp[initial_points_Alice][initial_points_Bob] = 1
    
    for i in range(initial_points_Alice, alice_wins+1):
        for j in range(initial_points_Bob, bob_wins+1):
            if i<alice_wins:
                dp[i+1][j] = mod_add(dp[i+1][j], mod_multiply(dp[i][j], mod_divide(j, mod_add(j, i))))
            if j<bob_wins:
                dp[i][j+1] = mod_add(dp[i][j+1], mod_multiply(dp[i][j], mod_divide(i, mod_add(j, i))))

    # to print 2 dimensional dp array
    # print(*dp, sep = "\n")
    
    return dp[-1][-1]
    
# Problem 1b (Expectation)      
def calc_expectation(t, g = lambda x: x):
    # g represents the function of rv to be used, default value is the rv itself
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    E = 0
    # because first two rounds are already decided
    t = t - initial_points_Alice - initial_points_Bob

    # i represents the summation value
    for i in range(-t, t+1, 2):
        AliceWins = (t+i)/2
        BobWins = (t-i)/2
        if AliceWins%1==0:
            E += g(i)*calc_prob(int(AliceWins)+initial_points_Alice, int(BobWins)+initial_points_Bob)

    return E


# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """

    E_x2 = calc_expectation(t, lambda x: mod_multiply(x,x))

    Ex = calc_expectation(t)
    Ex_2 = mod_multiply(Ex, Ex)

    return mod_add(E_x2, -Ex_2)
    
print("Probability:",calc_prob(T1T2, T3T4))
print("Expectation:",calc_expectation(T3T4))
print("Variance:",calc_variance(T3T4))
