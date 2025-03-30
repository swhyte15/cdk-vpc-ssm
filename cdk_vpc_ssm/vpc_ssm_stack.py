from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

class VpcSsmStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # VPC with public and private subnets across 2 AZs
        vpc = ec2.Vpc(
            self, "MyVpc",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )

        # IAM Role for EC2 with SSM access
        role = iam.Role(
            self, "EC2SSMRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore")
        )

        # Amazon Linux 2 AMI
        ami = ec2.MachineImage.latest_amazon_linux2()

        # Security Group
        sg = ec2.SecurityGroup(
            self, "InstanceSG",
            vpc=vpc,
            description="Allow outbound",
            allow_all_outbound=True
        )

        # EC2 Instance in a private subnet
        instance = ec2.Instance(
            self, "SSMInstance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ami,
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            security_group=sg,
            role=role
        )

        # Set root EBS volume size to 50GB
        instance.instance.add_property_override(
            "BlockDeviceMappings", [{
                "DeviceName": "/dev/xvda",
                "Ebs": {
                    "VolumeSize": 50,
                    "VolumeType": "gp3",
                    "DeleteOnTermination": True
                }
            }]
        )
