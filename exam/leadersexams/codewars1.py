def human_years_cat_years_dog_years(human_years):
    
    cat = 0
    
    dog = 0
    
    human = 1
    
    for i in range (human_years ):
        if human == 1 :
           
           cat += 15  
           
           dog += 15

           human += 1

           continue

        if human == 2:

            cat += 9
             
            dog += 9   

            human+= 1 

            continue

            cat += 4
    
            dog += 5

    return[human_years,cat,dog]




