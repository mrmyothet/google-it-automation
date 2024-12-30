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

---

### Terms and definitions (Automation on the cloud)

- Private cloud: When your company owns the services and the rest of your infrastructure
- Public cloud: The cloud services provided to you by a third party
- Hybrid cloud: A mixture of both public and private clouds
- Multi-cloud: A mixture of public and/or private clouds across vendors
- Software as a Service (or SaaS): When a Cloud provider delivers an entire application or program to the customer
- Platform as a Service (or PaaS): When a Cloud provider offers a preconfigured platform to the customer
- Infrastructure as a Service (or IaaS): When a Cloud provider supplies only the bare-bones computing experience
- A/B testing: A way to compare two versions of something to find out which version performs better
- Automatic scaling: This service uses metrics to automatically increase or decrease the capacity of the system
- Manual scaling: Changes are controlled by humans instead of software
- Autoscaling: Allows the service to increase or reduce capacity as needed, while the service owner only pays for the cost of the machines that are in use at any given time
- Capacity: How much the service can deliver
- Containers: Applications that are packaged together with their configuration and dependencies
- Content Delivery Networks (CDN): A network of physical hosts that are geographically located as close to the end users as possible
- Disk image: A snapshot of a virtual machine’s disk at a given point in time
- Persistent storage: Storage used for instances that are long lived and need to keep data across reboots and upgrades
- Ephemeral storage: Storage used for instances that are temporary and only need to keep local data while they’re running
- Hot data: Accessed frequently and stored in hot storage
- Cold data: Accessed infrequently and stored in cold storage
- Input/Output Operations Per Second (IOPS): Measures how many reads or writes you can do in one second, no matter how much data you're accessing
- Load balancer: Ensures that each node receives a balanced number of requests
- Object storage: Storage where objects are placed and retrieved into a storage bucket
- Orchestration: The automated configuration and coordination of complex IT systems and services
- Reference images: Store the contents of a machine in a reusable format
- Sticky sessions: All requests from the same client always go to the same backend server
- Templating: The process of capturing all of the system configuration to let us create VMs in a repeatable way
- Throughput: The amount of data that you can read and write in a given amount of time
- Rate limits: Prevent one service from overloading the whole system
- Utilization limits: Cap the total amount of a certain resource that you can provision

---

### Build artifact testing

- **Unit tests:** These are small, granular tests written by the developer to test individual functions in the code. In Docker, unit tests are run directly on your codebase before the Docker image is built, ensuring the code is working as expected before being packaged.

- **Integration tests:** These refer to testing an application or microservice in conjunction with the other services on which it relies. In a Dockerized environment, integration tests are run after the docker image is built and the container is running, testing how different components operate together inside the Docker container.

- **End-to-end (E2E) tests:** This type of testing simulates the behavior of a real user (e.g., by opening the browser and navigating through several pages). E2E tests are run against the fully deployed docker container, checking that the entire application stack with its various components and services functions correctly as a whole.

- **Performance tests:** This type of testing identifies bottlenecks. Performance tests are run against the fully deployed Docker container and test various stresses and loads to ensure the application performs at expectations.

---

### Enable Kubernetes

- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [k3s](https://docs.k3s.io/quick-start)
- [microk8s](https://microk8s.io/docs/getting-started)
- [minikube](https://minikube.sigs.k8s.io/docs/start/)

---

- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Official Python client library for Kubernetes](https://github.com/kubernetes-client/python)
- [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [Create an External Load Balancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/)
- [External Name – Kubernetes Networking](https://ibm.github.io/kubernetes-networking/services/externalname/)
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Managing Resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/)
- [Kubernetes ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
- [Declarative Application Management in Kubernetes](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)
- [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Rolling Back a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment)

---

- [Deploy to Cloud Run](https://cloud.google.com/run/docs/quickstarts/deploy-container)
- [Deploy an app to a GKE cluster](https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster)
- [Google Kubernetes Engine vs Cloud Run: Which should you use?](https://cloud.google.com/blog/products/containers-kubernetes/when-to-use-google-kubernetes-engine-vs-cloud-run-for-containers)
- [Containers on Compute Engine](https://cloud.google.com/compute/docs/containers/)
- [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
- [Get started with Kubernetes (using Python)](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)

---

- [Horizontal Vs. Vertical Scaling: Which Should You Choose?](https://www.cloudzero.com/blog/horizontal-vs-vertical-scaling/)
- [Scaling an application](https://cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps)
- [Horizontal Pod autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)
- [Configuring horizontal Pod autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)
- [Configure multidimensional Pod autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling)
- [About instance autoscaling in Cloud Run services](https://cloud.google.com/run/docs/about-instance-autoscaling)
- [About autoscaling workloads based on metrics](https://cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics)
- [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing)

---

- [Patterns for scalable and resilient apps](https://cloud.google.com/architecture/scalable-and-resilient-apps)

---

- [Google Cloud Networking overview](https://cloud.google.com/blog/topics/developers-practitioners/google-cloud-networking-overview)
- [Virtual Private Cloud (VPC)](https://cloud.google.com/vpc/?hl=en)
- [Subnets](https://cloud.google.com/vpc/docs/subnets)
- [Scalable, cloud-first firewall service](https://cloud.google.com/security/products/firewall?hl=en)
- [Cloud Load Balancing](https://cloud.google.com/load-balancing?hl=en)
- [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine?hl=en)

---

- [Exploring container security](https://cloud.google.com/blog/products/containers-kubernetes/exploring-container-security-let-google-do-the-patching-with-new-managed-base-images)
- [Security Command Center overview](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview)
- [Shared responsibilities and shared fate on Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
- [GKE shared responsibility](https://cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility)

---

### Terms and definitions (Docker and Kubernetes)

- **Artifact:** A byproduct of the software development process that can be accessed and used, an item produced during programming
- **Docker:** An open-source tool used to build, deploy, run, update, and manage containers
- **Kubernetes:** An open-source platform that gives programmers the power to orchestrate containers
- **Registry:** A place where containers or artifacts are stored and organized
- **Container registry:** A storage location for container images, organized for efficient access
- **Container repository:** A container registry that manages container images
- **Pod:** A group of one or more containers that are scheduled and run together

---

```bash

sudo apt install puppet-master

sudo puppet apply -v tools.pp

```

```bash

sudo apt install puppet-module-puppetlabs-apache

cd /usr/share/puppet/modules.available/puppetlabs-apache/

sudo puppet apply -v webserver.pp

```

```bash
sudo puppet config --section master set augosign true

ssh webserver
sudo apt install puppet
sudo puppet config set server ubuntu.example.com
sudo puppet agent -v --test
sudo systemctl enable puppet
sudo systemctl start puppet
sudo systemctl status puppet

```

- [The Puppet language style guide](https://puppet.com/docs/puppet/latest/style_guide.html)
- [Open source Puppet](https://puppet.com/docs/puppetserver/latest/install_from_packages.html)
- [Puppet SSL explained](http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/)

---

- [rspec-puppet](https://rspec-puppet.com/tutorial/)
- [puppet-lint](http://puppet-lint.com/)

---

- https://www.datadoghq.com/blog/monitoring-101-collecting-data/
- https://www.digitalocean.com/community/tutorials/an-introduction-to-metrics-monitoring-and-alerting
- https://en.wikipedia.org/wiki/High_availability
- https://landing.google.com/sre/books/

---

- https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances
- https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html

---

### Debugging a problem with a cloud deployment

```bash

sudo systemctl status apache2
sudo systemctl restart apache2
sudo systemctl status apache2

sudo netstat -nlp
ps -ax | grep python3

sudo kill [process-id]
sudo systemctl --type=service | grep jimmy
sudo systemctl stop jimmytest && sudo systemctl disable jimmytest
sudo netstat -nlp

sudo systemctl start apache2

```

---

### Terms and definitions (Puppet)

- **Configuration management:** Automation technique that manages the configuration of computers at scale
- **Domain-Specific Language (DSL):** A programming language that's more limited in scope
- **Facts:** Variables that represent the characteristics of the system
- **Puppet:** The current industry standard for configuration management, also known as the client
- **Puppet master:** Known as the Puppet server

---

### Integration with Github

- https://www.simplilearn.com/tutorials/git-tutorial/what-is-github
- https://github.blog/2022-06-03-a-beginners-guide-to-ci-cd-and-automation-on-github/
- https://docs.github.com/en/webhooks-and-events/webhooks/creating-webhooks
- https://santoshk.dev/posts/2022/how-to-setup-a-github-to-jenkins-pipeline-with-webhook/
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks
- https://circleci.com/docs/enable-checks/

---

- [How to Use Value Stream Mapping in DevOps](https://www.lucidchart.com/blog/value-stream-mapping-for-devops)

---

### Github and delivery

- https://docs.github.com/en/actions
- https://github.blog/2022-06-03-a-beginners-guide-to-ci-cd-and-automation-on-github/
- https://github.blog/2020-04-16-github-protips-tips-tricks-hacks-and-secrets-from-jason-etcovitch/

---

### CD best practices

- [Continuous delivery principles](https://www.atlassian.com/continuous-delivery/principles)
- [What is Continuous Deployment?](https://github.com/resources/articles/devops/continuous-deployment)
- [Continuous Deployment](https://scaledagileframework.com/continuous-deployment/)
- [Feature Flags](https://launchdarkly.com/blog/what-are-feature-flags/)
- [Incremental rollouts with GitLab CI/CD](https://docs.gitlab.com/ee/ci/environments/incremental_rollouts.html)
- [A Comprehensive Guide to Canary Releases](https://blog.getambassador.io/cloud-native-patterns-canary-release-1cb8f82d371a)
- [Canary Deployment & Release Process](https://www.bmc.com/blogs/canary-deployment-release/)
- [Using blue-green deployment to reduce downtime](https://docs.cloudfoundry.org/devguide/deploy-apps/blue-green.html)
