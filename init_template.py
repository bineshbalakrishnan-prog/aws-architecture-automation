import csv

def create_master_template():
    filename = 'master_requirements.csv'
    headers = ['Environment', 'Service', 'Region', 'Spec', 'Quantity', 'Usage_Type']
    
    # A starter set of resources for your Mumbai DR scenario
    sample_data = [
        ['PROD', 'Data Transfer', 'ap-south-1', 'Internet Outbound', '10000', 'GB'],
        ['PROD', 'EC2', 'ap-south-1', 't3.medium', '2', 'Instances'],
        ['PROD', 'RDS', 'ap-south-1', 'db.t4g.medium', '1', 'Instance'],
        ['UAT', 'EC2', 'ap-south-1', 't3.micro', '1', 'Instance'],
        ['UAT', 'S3', 'ap-south-1', 'Standard Storage', '500', 'GB']
    ]

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(sample_data)
    
    print(f"Created {filename}! Open this file to add your resources.")

if __name__ == "__main__":
    create_master_template()