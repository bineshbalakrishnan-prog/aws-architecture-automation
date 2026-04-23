import pandas as pd

def generate_estimate_plan(csv_file):
    df = pd.read_csv(csv_file)
    
    print("--- AWS PRICING ESTIMATE PLAN ---")
    for env in df['Environment'].unique():
        print(f"\nGroup: {env}")
        env_data = df[df['Environment'] == env]
        for _, row in env_data.iterrows():
            print(f"- Add {row['Service']} ({row['Region']}): {row['Spec_1']}, {row['Spec_2']} x{row['Quantity']}")

# Run the processor
if __name__ == "__main__":
    try:
        generate_estimate_plan('aws_requirements.csv')
    except FileNotFoundError:
        print("Please create 'aws_requirements.csv' first!")