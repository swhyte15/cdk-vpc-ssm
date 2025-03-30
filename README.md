# CDK VPC + EC2 + SSM Setup

This AWS CDK project deploys a secure and modular VPC with:

- 🛡️ Two **public and private subnets** across 2 AZs
- 🖥️ One **Amazon Linux 2 t3.micro** instance in a private subnet
- 💾 **50GB EBS** root volume
- 🔒 **SSM Agent** support with IAM Role
- 🌐 **Outbound internet** access via NAT Gateway
- 💻 Fully accessible via **AWS Systems Manager Session Manager** (no SSH needed)

---

## 📁 Project Structure

```bash
cdk-vpc-ssm/
├── app.py                   # CDK app entrypoint
├── cdk.json                 # CDK project config
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignored files
└── cdk_vpc_ssm/
    ├── __init__.py
    └── vpc_ssm_stack.py     # Main stack definition
🚀 Getting Started
Prerequisites
AWS CLI configured (aws configure)

Node.js & AWS CDK v2 (npm install -g aws-cdk)

Python 3.7+

Virtualenv (python -m venv .venv)

# Activate virtual environment
.venv\Scripts\activate         # Windows
# OR
source .venv/bin/activate      # Mac/Linux

# Install Python packages
pip install -r requirements.txt

cdk synth
cdk deploy

🧠 Usage
Once deployed:

Go to AWS Systems Manager > Session Manager

Start a session with the running EC2 instance

No SSH, no key pairs needed!

Cleanup
To delete all resources:

cdk destroy

![VPC Architecture] https://github.com/swhyte15/cdk-vpc-ssm/commit/fc51bf6279c503a3e302d83c51cfc74fee893c58 



