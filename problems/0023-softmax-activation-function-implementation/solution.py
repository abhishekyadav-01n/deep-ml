import math

def softmax(scores: list[float]) -> list[float]:
    max_val = 0
    for i in range(len(scores)):
        max_val = max(max_val, scores[i])

    for i in range(len(scores)):
        scores[i] = scores[i] - max_val

    determinor = 0

    for i in range(len(scores)):
        determinor += math.exp(scores[i])
    
    ans = []

    for i in range(len(scores)):
        ans.append(math.exp(scores[i]) / determinor)
    
    return ans
    pass