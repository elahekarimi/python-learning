max_scores=input('the student scorses is:').split()
for n in range(0, len(max_scores)):
    max_scores[n]=int(max_scores[n])

highest_score=0
for score in max_scores:
    if score>highest_score:
        highest_score=score

print("the highest score is:",highest_score)

