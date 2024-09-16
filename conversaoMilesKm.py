
def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(mpg):
    liters = 3.785411784
    km = 1609.344 / 1000
    return (liters / km) * (100 / mpg)

print(liters_100km_to_miles_gallon(3.9))  
print(liters_100km_to_miles_gallon(7.5))  
print(liters_100km_to_miles_gallon(10.0))

print(miles_gallon_to_liters_100km(60.3)) 
print(miles_gallon_to_liters_100km(31.4)) 
print(miles_gallon_to_liters_100km(23.5)) 