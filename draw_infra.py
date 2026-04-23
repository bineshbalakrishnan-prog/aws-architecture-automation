import os
# Replace this path with the actual path where Graphviz was installed
# Common path: C:\Program Files\Graphviz\bin
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

from diagrams import Cluster, Diagram
# ... rest of your code ...

import sys

try:
    from diagrams import Cluster, Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.network import VPC, PublicSubnet
    from diagrams.aws.storage import S3
except ImportError:
    print("Error: The 'diagrams' library is not installed. Run 'pip install diagrams' first.")
    sys.exit(1)

# Diagram configuration
with Diagram("My AWS Architecture", show=False, filename="infra", direction="LR"):
    with Cluster("Custom VPC"):
        with Cluster("Public Subnet"):
            web_server = EC2("Web Server")
        
        bucket = S3("Assets Bucket")
        
        web_server >> bucket
        
print("Success! 'infra.png' has been generated in your project folder.")