def cel_to_fah(x):
    return (x*9/5)+32

temperature_in_celsius=int(input("Enter temperature in celsius: "))
temperature_in_fahrenheit=cel_to_fah(temperature_in_celsius)
print("Temperature in celsius:",temperature_in_celsius,"°C")
print("Temperature in fahrenheit:",temperature_in_fahrenheit,"°F")

    