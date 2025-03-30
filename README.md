# CDK VPC + EC2 + SSM Deployment

This AWS CDK project deploys the following infrastructure in **us-east-1**:

- A VPC with 2 public and 2 private subnets across 2 Availability Zones
- A NAT Gateway for secure outbound internet access from private subnets
- One EC2 instance (Amazon Linux 2, `t3.micro`) in a private subnet
- 50GB EBS volume
- SSM Agent support for Session Manager access (no SSH needed)

---

## 📊 Architecture Diagram

![VPC Architecture](https://raw.githubusercontent.com/swhyte15/cdk-vpc-ssm/main/A_diagram_illustrates_a_cloud_network_architecture.png)

---

## 🚀 Getting Started

### 📦 Prerequisites

- AWS CLI configured: `aws configure`
- Python 3.7+
- Node.js & AWS CDK v2: `npm install -g aws-cdk`
- VS Code or another code editor

---

### 🛠️ Project Setup

```bash
# Clone the repo
git clone https://github.com/swhyte15/cdk-vpc-ssm.git
cd cdk-vpc-ssm

# Set up Python environment
python -m venv .venv
.venv\Scripts\activate   # On Windows
# OR
source .venv/bin/activate  # On Mac/Linux

# Install Python dependencies
pip install -r requirements.txt

