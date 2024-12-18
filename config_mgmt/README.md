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