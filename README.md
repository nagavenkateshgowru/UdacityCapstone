# UdacityCapstone
Project to demonstrate complete CI/CD pipeline

## To Deploy Infra
ansible-playbook create-k8s-master.yaml # creates security group with tcp ports open and creates t2.medium ec2 instance
ansible-playbook install-k8s.yaml # configures this ec2 as a single node K8S cluster

## CI/CD is done by the Jenkins pipelines
