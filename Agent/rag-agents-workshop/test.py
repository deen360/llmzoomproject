def set_weather(city: str, temp: float) -> None:
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'

    set_weather_tool = {
    "type": "function",
    "function": {

        "name": "set_weather",

        "description": "A function that adds or updates weather data for a city.",

        # Describe the parameters (inputs) the tool expects
        "parameters": {

            "type": "object",

            # Define the input fields
            "properties": {
                "city": {
                    
                    "type": "string",
                    "description": "The name of the city to add or update in the database."
                },
                "temp": {
                    
                    "type": "number",
                    "description": ""The temperature in Celsius to store for the city."
                }
            },

            "required": ["city", "temp"]
        }
    }
}
