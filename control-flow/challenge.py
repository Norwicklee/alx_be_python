# Prompt user to input different words
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter the last adjective: ")

# Construct the story template with placeholders
story_template = (
    "On a beautiful {adj1} day, I went to the zoo. "
    "I saw a funny {adj2} monkey from the trees. "
    "Then, I spotted a majestic {adj3} lion lounging in the sun. "
    "What a wild and {adj4} experience."
)

# Use conditional to add some variation to the story
if adjective1.lower() == "sunny":
    story_template += " It was the perfect day for a zoo visit!"
else:
    story_template += " Despite the weather, it was an unforgettable day!"

# Print the complete Mad Libs story with the user's inserted words
print(story_template.format(adj1=adjective1, adj2=adjective2, adj3=adjective3, adj4=adjective4))