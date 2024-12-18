# Configration Management and The Cloud

```bash
git clone https://github.com/blue-kale/hello

cd hello

sudo ./hello_cloud.py 80

sudo cp hello_cloud.py /usr/local/bin/
sudo cp hello_cloud.service /etc/systemd/system/
sudo systemctl enable hello_cloud

sudo reboot

ps ax | grep hello

sudo apt install puppet

./hello/setup_puppet.sh

```

---

```bash
gcloud init

gcolud comput instace create --source-instance-template webserver-template ws1 ws2 ws3 ws4 ws5

```

---

### Managing VMs in GCP

- https://cloud.google.com/compute/docs/quickstart-linux
- https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template
- https://cloud.google.com/sdk/docs

---

- [Getting started on GCP with Terraform](https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform)
- [Creating groups of unmanaged instances](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances)
- [External Application Load Balancer overview](https://cloud.google.com/load-balancing/docs/https/)
- [8 High Performance Cloud Load Balancer for Application HA](https://geekflare.com/cloud-load-balancer/)
- [Terraform Enterprise GCP Reference Architecture](https://developer.hashicorp.com/terraform/enterprise/deploy/replicated/architecture/reference-architecture/gcp)
- [Terraform for On-Premises and Hybrid Cloud at Wayfair](https://www.coursera.org/learn/configuration-management-cloud/supplement/39SOd/more-about-cloud-gcp)

---

```bash

gcloud compute instances create --zone us-central1-a --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8

gcloud compute instances list

```

#### Limitation

- https://cloud.google.com/compute/resource-usage
- https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits
