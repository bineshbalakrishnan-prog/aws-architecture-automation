import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

import sys

try:
    from diagrams import Cluster, Diagram
    from diagrams.aws.network import APIGateway
    from diagrams.aws.compute import Lambda
    from diagrams.aws.database import Dynamodb
except ImportError:
    print("Error: The 'diagrams' library is not installed. Run 'pip install diagrams' first.")
    sys.exit(1)

with Diagram("Serverless Architecture", show=False, filename="serverless", direction="LR"):
    api = APIGateway("API Gateway")

    with Cluster("Backend"):
        fn = Lambda("Lambda Function")
        db = Dynamodb("DynamoDB")

        fn >> db

    api >> fn

print("Success! 'serverless.png' has been generated in your project folder.")
