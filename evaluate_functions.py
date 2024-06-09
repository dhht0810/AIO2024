def calculate_evaluate_functions(tp, fp, fn):

    if isinstance(tp, int) == False: 
        return "tp must be int"
    if isinstance(fp, int) == False: 
        return "tp must be int"
    if isinstance(fn, int) == False: 
        return "tp must be int"
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    print(f'precision is:  {precision} \nrecall is: {recall} \nf1_score is: {f1_score}')


ans = calculate_evaluate_functions(2, 3, 4)

print(ans)