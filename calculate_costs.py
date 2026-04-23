import csv
import os

print(f"DEBUG: Running from {os.getcwd()}")
print(f"DEBUG: Looking for requirements.csv... {'Found!' if os.path.exists('requirements.csv') else 'NOT FOUND'}")

import csv

# Hardcoded approximate monthly rates for ap-south-1 (Mumbai)
PRICES = {
    "t3.medium": 30.36,   # ~$0.0416/hr * 730hrs
    "t3.micro": 7.59,     # ~$0.0104/hr * 730hrs
    "db.t4g.medium": 52.56, 
    "500GB": 11.50        # S3 standard ~ $0.023 per GB
}

def calculate():
    print("="*40)
    print("   AWS ESTIMATED COSTS (MUMBAI)   ")
    print("="*40)
    
    grand_total = 0
    
    try:
        with open('requirements.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                env = row['Environment']
                svc = row['Service']
                spec = row['Spec']
                qty = int(row['Quantity'])
                
                # Logic to find price in our dictionary
                unit_price = PRICES.get(spec, 0.0)
                item_total = unit_price * qty
                grand_total += item_total
                
                print(f"[{env}] {svc: <5} | {spec: <15} | Qty: {qty} | ${item_total:>8.2f}/mo")
        
        print("-" * 40)
        print(f"ESTIMATED MONTHLY TOTAL:    ${grand_total:>10.2f}")
        print("="*40)
        print("\nReady for Export! When Node.js is ready, I can push this to calculator.aws.")

    except FileNotFoundError:
        print("Error: requirements.csv not found!")

if __name__ == "__main__":
    calculate()