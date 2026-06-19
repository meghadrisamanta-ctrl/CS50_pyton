def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # TODO: Remove '$', convert to float, and return it
    return float(d.replace("$",""))
    
    


def percent_to_float(p):
    # TODO: Remove '%', convert to float, divide by 100, and return it
    percentage_number = float(p.replace("%",""))
    m = percentage_number/100
    return m


main()