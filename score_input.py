def score_input(test_name, test_score=-5, invalid_message='Invalid test score!'):
    tn = test_name + str(input('Enter Test Name:'))
    add = 0
    scores = test_score + add + int(input('Enter Score:'))
    invalid_message = invalid_message
    if test_score < 0:
        return invalid_message
    else:
        print(tn, scores)
