"""Challenge 1: Estimate CO2 emissions for a car journey."""

FUEL_LITRES_PER_100_MILES = 9.66
EMISSIONS_KG_PER_LITRE = {"diesel": 2.68, "petrol": 2.31}


def get_distance():
    while True:
        try:
            distance = float(input("Enter distance travelled in miles: "))
            if distance >= 0:
                return distance
            print("Distance cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def get_fuel_type():
    while True:
        fuel = input("Fuel type (diesel/petrol): ").strip().lower()
        if fuel in EMISSIONS_KG_PER_LITRE:
            return fuel
        print("Please enter diesel or petrol.")


def calculate_emissions(distance, fuel):
    litres_used = distance * FUEL_LITRES_PER_100_MILES / 100
    return litres_used * EMISSIONS_KG_PER_LITRE[fuel]


def main():
    distance = get_distance()
    fuel = get_fuel_type()
    emissions = calculate_emissions(distance, fuel)
    print(f"Estimated CO2 emissions: {emissions:.2f} kg")


if __name__ == "__main__":
    main()
