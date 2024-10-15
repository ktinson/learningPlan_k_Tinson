from statistics import mean 
scores = []
m = 0
while m <= 3:
    score = int(input("Enter a score: "))
    scores.append(score)
    m += 1
    print(scores)   
print(f'Average using sum() and len(): {sum(scores)/len(scores)}')
print(f'Average using statics import and mean {mean(scores)}')






