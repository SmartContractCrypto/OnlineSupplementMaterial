import pandas as pd
from collections import Counter

Categories = ["Hash","Signature","ZKP"]

for category in Categories:
    print("-"*60, category, "-"*60)
    posts = pd.read_csv("../data/4_StackExchangePosts_Label_" + category + ".CSV", keep_default_na=False)
    
    # Post Number
    print(f"Number of {category}-related Posts:",len((posts['Question'])))

    # Post Labels: Obstacles faced bu the poster
    numbers=dict(Counter(posts['Obstacle']))
    print(f"Number of Obstacles in {category}-related Posts:", numbers)
    
    ratios={}
    obstacles = list(numbers.keys())
    obstacles.remove("N/A")
    for obstacle_name in obstacles:
        ratios[obstacle_name] = "{:.1%}".format(numbers[obstacle_name]/(len((posts['Question']))-numbers["N/A"]))
    print(f"Proportion of Obstacles in {category}-related Posts:", ratios)
