import csv
import json
import os

def build_mcp_payload(csv_file):
    # 1. Load the CSV using built-in csv module (No Pandas needed!)
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return None

    estimate_payload = {
        "metadata": {
            "name": "Mumbai_DR_Strategy_Estimate",
            "customer": "Internal_Reporting"
        },
        "groups": {} # We'll use a dict here to group manually
    }

    try:
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                env_name = row['Environment']
                
                # Create group if it doesn't exist
                if env_name not in estimate_payload['groups']:
                    estimate_payload['groups'][env_name] = {
                        "groupName": env_name,
                        "items": []
                    }

                # Build the item
                item = {
                    "serviceCode": row['Service'],
                    "region": row['Region'],
                    "description": f"{env_name} - {row['Service']}",
                    "usage": {
                        "value": float(row['Quantity']),
                        "unit": "Quantity/Month"
                    },
                    "specifications": row['Spec']
                }
                estimate_payload['groups'][env_name]['items'].append(item)
        
        # Convert groups dict back to a list for the final JSON
        estimate_payload['groups'] = list(estimate_payload['groups'].values())
        return estimate_payload

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    input_csv = 'requirements.csv'
    output_json = 'mcp_input.json'

    print(f"Processing {input_csv} using Pure Python Engine...")
    final_payload = build_mcp_payload(input_csv)

    if final_payload:
        with open(output_json, 'w') as f:
            json.dump(final_payload, f, indent=4)
        
        print(f"SUCCESS: {output_json} generated without using blocked DLLs!")
        print("\nNext step: Give the JSON content to Kiro to get the AWS link.")