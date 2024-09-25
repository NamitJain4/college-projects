from random import random

class Alice:
    def __init__(self):
        self.past_play_styles = [1, 1] 
        self.results = [1, 0]           
        self.opp_play_styles = [1, 1]  
        self.points = 1

        self.total_rounds = 2

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 0:
            return 1
        elif self.results[-1] == 0.5:
            return 0
        else:
            if (self.total_rounds-self.points)/self.total_rounds>6/11:
                return 0
            return 2
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result

        self.total_rounds += 1

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1, 1] 
        self.results = [0, 1]          
        self.opp_play_styles = [1, 1]   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    payoff_matrix[0][0] = ((alice.total_rounds-alice.points)/alice.total_rounds, 0, alice.points/alice.total_rounds)
    
    a = alice.play_move()
    b = bob.play_move()

    x, y, z = payoff_matrix[a][b]
    
    d = random()
    result = 0.5
    if d<x:
        result = 1
    elif d>=x+y:
        result = 0
    alice.observe_result(a, b, result)
    bob.observe_result(b, a, 1-result)


def monte_carlo(num_rounds):
    num_rounds-=2
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    bob = Bob()
    alice = Alice()
    
    matrix = [
            [(1/2, 0, 1/2), (7/10, 0, 3/10), (5/11, 0, 6/11)],
            [(3/10, 0, 7/10), (1/3, 1/3, 1/3), (3/10, 1/2, 1/5)],
            [(6/11, 0, 5/11), (1/5, 1/2, 3/10), (1/10, 4/5, 1/10)]
        ]

    for i in range(num_rounds):
        simulate_round(alice, bob, matrix)
    print("Points of Alice and Bob respectively:")
    print(alice.points, bob.points)
    print("Win rate:",round(100*alice.points/(alice.points+bob.points), 5), "%")
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)
