import os
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, VPC, PublicSubnet, PrivateSubnet
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3

# Ensure Graphviz is found
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

with Diagram("Standard Web Stack", show=False, filename="web_stack_arch", direction="TB"):
    ingress = ELB("ALB")
    content_bucket = S3("Static Assets")

    with Cluster("VPC"):
        with Cluster("Public Tier"):
            web_nodes = [EC2("Web 1"), EC2("Web 2")]

        with Cluster("Database Tier"):
            db_primary = RDS("User DB")
            db_primary - Edge(color="brown", style="dashed") - RDS("Replica")

    ingress >> web_nodes >> db_primary
    web_nodes >> content_bucket