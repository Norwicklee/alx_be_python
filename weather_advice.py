#Prompt user to input current weather
weather = input("What's the weather like today? (sunny/rainy/cold)")
# Hive clothe recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses")
elif weather == "rainy":
    print("Don't forget your umbrella or raincoat")
elif weather == "cold":
    print("Make sure to wear warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather")