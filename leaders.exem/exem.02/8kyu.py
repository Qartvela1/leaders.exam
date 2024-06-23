def human_years_cat_years_dog_years(human_years):
    # Your code here
    return [0,0,0]
    
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years == 15 + 9
        dog_years == 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
    return [human_years , cat_years , dog_years]
        
  
def nearest_sq(n):
    # pass
    
    def nearest_sq(n):
        root = (n)
        lower = int(root)
        upper = lower + 1
        
        lower_sq = lower ** 2
        upper_sq = upper ** 2
        
        if abs(n - lower_sq) <= abs(n - upper_sq):
            return lower_sq
        else:
            return upper_sq
        

















