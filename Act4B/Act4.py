import csv
from decimal import Decimal

def load_currency_rates():
    """Load currency rates from CSV file and return a dictionary of rates."""
    rates = {}
    try:
        with open('currency.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                rates[row['code']] = {
                    'name': row['name'],
                    'rate': Decimal(row['rate'])
                }
        return rates
    except FileNotFoundError:
        print("Error: currency.csv file not found!")
        return None
    except Exception as e:
        print(f"Error loading currency rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another using given rates."""
    if not rates:
        return None, None, None
    
    if from_currency not in rates or to_currency not in rates:
        return None, None, None
    
    try:
        converted_amount = amount * (rates[to_currency]['rate'] / rates[from_currency]['rate'])
        return round(converted_amount, 2), rates[from_currency]['name'], rates[to_currency]['name']
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None, None, None

def main():
    """Main program function."""
    currency_rates = load_currency_rates()
    if not currency_rates:
        return
    
    while True:
        try:
            amount = float(input("\nEnter the amount to convert (or 0 to exit): "))
            if amount == 0:
                print("Thank you for using the currency converter!")
                break
                
            if amount < 0:
                print("Please enter a positive amount.")
                continue
                
            from_currency = input("Enter the currency code to convert from: ").upper()
            to_currency = input("Enter the currency code to convert to: ").upper()
            
            converted_amount, from_name, to_name = convert_currency(
                amount, from_currency, to_currency, currency_rates
            )
            
            if converted_amount is not None:
                print(f"\n{amount:,.2f} {from_name} ({from_currency})")
                print(f"= {converted_amount:,.2f} {to_name} ({to_currency})")
            else:
                print("\nError: Invalid currency codes! Available codes:")
                print(", ".join(sorted(currency_rates.keys())))
                
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()