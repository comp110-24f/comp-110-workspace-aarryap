def get_weather_report() -> str:

    weather: str = input("WHat is the weather? ")

    if weather == "rainy" or weather == "cold":
        return "Bring a jacket!"
    elif weather == "hot":
        return "Keep cool out there!"
    else:
        return "I dont know you brev!"


print(get_weather_report())
