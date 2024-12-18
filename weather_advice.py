# Prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide Clothing Recommendations
if weather.lower() == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif weather.lower() == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather.lower() == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."

# Output the Recommendation
print(recommendation)