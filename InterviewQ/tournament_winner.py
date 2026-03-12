def tournamentWinner(competitions, results):
    # Write your code here.
    top_team = ""
    scores = {top_team: 0} 
    for round in range(len(competitions)):
        competition = competitions[round]
        winner = competition[0] if results[round] == 1 else competition[1]
        
        if winner in scores:
            scores[winner] = scores[winner] + 1
        else:
            scores[winner] = 1
            
        if scores[top_team] < scores[winner]:
            top_team = winner
            
    return top_team
