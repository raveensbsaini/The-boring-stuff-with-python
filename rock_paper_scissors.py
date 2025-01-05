def rpsWinner(a,b):
    names = ["rock","scissors","paper"]
    # if a not in names or b not in names:
    #     raise ValueError("")
    #    
    if a == b:
        return "tie"

    elif a == "rock" and b == "scissors":
        return "player one"
    elif b == "rock" and a == "scissors":
            return "player two"

    elif a == "rock" and b == "paper":
        return "player two"
    elif b == "rock" and a == "paper":
            return "player one"

    elif a == "paper" and b == "scissors":
        return "player two"
    elif b == "paper" and a == "scissors":
            return "player one"
    
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
