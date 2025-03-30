#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_vpc_ssm.vpc_ssm_stack import VpcSsmStack

app = cdk.App()
VpcSsmStack(app, "VpcSsmStack", env=cdk.Environment(region="us-east-1"))
app.synth()
