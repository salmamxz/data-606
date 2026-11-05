# MongoDB Installation and Configuration on AWS EC2

## 1. Introduction

The aim of this task is to install and configure MongoDB Community Edition on an Ubuntu EC2 instance using AWS.

I will use the Ubuntu terminal through an SSH connection from my Mac. MongoDB will be installed directly on the EC2 instance using the official MongoDB repository and the APT package manager.

This document explains the steps I plan to follow, including installation, configuration, authentication and basic database testing.

## 2. Prerequisites

Before starting the installation, I need to make sure that:

- My AWS EC2 instance is running.
- The instance is using Ubuntu Server 26.04 LTS.
- I have a working SSH connection from my Mac to the instance.
- I have permission to run commands using `sudo`.
- The instance has an internet connection.

The environment I will be using is:

| Component | Configuration |
|---|---|
| Cloud provider | Amazon Web Services |
| Service | EC2 |
| Operating system | Ubuntu Server 26.04 LTS |
| Instance type | t3.micro |
| Database | MongoDB Community Edition |
| MongoDB version | 9.0 |
| Package manager | APT |

## 3. Connect to the EC2 Instance

The first step is to connect to the Ubuntu instance from my Mac.

I will open Terminal and use the SSH command:

```bash
ssh -i ~/.ssh/<PRIVATE_KEY_FILE>.pem ubuntu@<PUBLIC_IP_ADDRESS>
```

I will replace the private key filename and public IP address with the correct details for my instance.

If the connection is successful, the terminal should display a prompt similar to:

```bash
ubuntu@ip-172-31-xx-xx:~$
```

This means I am working inside the Ubuntu EC2 instance rather than my local Mac.

**Important:** The private key must match the key authorised on the EC2 instance. Creating a new key pair in AWS does not automatically give it access to an instance that already exists.

## 4. Update Ubuntu

Once connected, I will first update the package information and install any available system updates.

```bash
sudo apt update && sudo apt upgrade -y
```

I will then install the tools required for downloading and verifying the MongoDB packages:

```bash
sudo apt install -y gnupg curl
```

These tools are needed to download the MongoDB signing key and configure the repository.

## 5. Import the MongoDB Public Key

MongoDB uses a public GPG key to help verify that the packages being downloaded are genuine.

I will import the MongoDB 9.0 signing key using:

```bash
curl -fsSL https://pgp.mongodb.com/server-9.asc | \
sudo gpg --dearmor --yes -o /usr/share/keyrings/mongodb-server-9.gpg
```

This saves the signing key in the system keyring directory.

## 6. Add the MongoDB Repository

Next, I will add the official MongoDB repository to Ubuntu.

Ubuntu 26.04 uses the codename `resolute`, so I will use the following command:

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-9.gpg ] https://repo.mongodb.org/apt/ubuntu resolute/mongodb-org/9.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-9.0.list
```

This creates a repository configuration file that allows Ubuntu to find the MongoDB packages.

## 7. Update the Package List

After adding the repository, I will update the package list again:

```bash
sudo apt update
```

I can check whether MongoDB is available by running:

```bash
apt-cache policy mongodb-org
```

This should display the available MongoDB package versions.

## 8. Install MongoDB Community Edition

Once the repository has been added successfully, I will install MongoDB using:

```bash
sudo apt install -y mongodb-org
```

This installs MongoDB and its main components.

Some of the important components include:

| Component | Purpose |
|---|---|
| `mongodb-org` | Main MongoDB package |
| `mongodb-org-server` | Runs the MongoDB database server |
| `mongodb-mongosh` | Allows me to interact with MongoDB using the shell |
| `mongodb-org-mongos` | Provides the query router |
| `mongodb-org-tools` | Includes database tools |

The MongoDB server process is called `mongod`.

## 9. Start and Check the MongoDB Service

After installation, I will start the MongoDB service:

```bash
sudo systemctl start mongod
```

I will also enable it to start automatically whenever the EC2 instance restarts:

```bash
sudo systemctl enable mongod
```

To check whether the service is running, I will use:

```bash
sudo systemctl status mongod
```

I should see:

```text
Active: active (running)
```

This would confirm that the MongoDB service has started successfully.

I can press `q` to leave the status screen.

## 10. Check the MongoDB Installation

I will check the installed server version:

```bash
mongod --version
```

I will also check the MongoDB Shell version:

```bash
mongosh --version
```

If both commands return version information, I can continue to the next step.

### 10.1 Open the MongoDB Shell

To interact with the database, I will run:

```bash
mongosh
```

This should open the MongoDB Shell and allow me to enter database commands.

### 10.2 Test the Connection

Inside the MongoDB Shell, I will run:

```javascript
db.runCommand({ ping: 1 })
```

The expected response is:

```javascript
{
  ok: 1
}
```

This would confirm that MongoDB is responding to commands.

To leave the shell, I will type:

```javascript
exit
```

## 11. Create an Administrator Account

The next step is to configure authentication so that access to MongoDB is protected.

First, I will open the MongoDB Shell:

```bash
mongosh
```

Then I will switch to the administrative database:

```javascript
use admin
```

I will create an administrator account:

```javascript
db.createUser({
  user: "siteAdmin",
  pwd: passwordPrompt(),
  roles: [
    { role: "root", db: "admin" }
  ]
})
```

The shell will ask me to enter a password. I will use a strong password and keep it somewhere secure.

The `root` role gives this account administrative permissions across the MongoDB deployment.

Once the account has been created, I will exit the shell:

```javascript
exit
```

## 12. Enable Authentication

I will now enable authentication in the MongoDB configuration file.

First, I will open the configuration file:

```bash
sudo nano /etc/mongod.conf
```

I will find the `security` section and make sure it contains:

```yaml
security:
  authorization: enabled
```

I will also check that MongoDB is only listening for local connections:

```yaml
net:
  port: 27017
  bindIp: 127.0.0.1
```

This is important because I do not want to expose the database directly to the public internet.

To save the file in Nano, I will press `Ctrl + O`, then `Enter`, and finally `Ctrl + X` to exit.

## 13. Restart MongoDB

After changing the configuration, I need to restart MongoDB so that the changes take effect.

```bash
sudo systemctl restart mongod
```

I will check the service again:

```bash
sudo systemctl status mongod
```

The expected result is:

```text
Active: active (running)
```

## 14. Test Authentication

Now I will test whether the administrator account works.

I will run:

```bash
mongosh -u siteAdmin --authenticationDatabase admin -p
```

I will enter the password when prompted.

Once connected, I will check the connection status:

```javascript
db.runCommand({ connectionStatus: 1 })
```

I can also list the available databases:

```javascript
show dbs
```

This will help me check that I can access MongoDB using the administrator account.

## 15. Create a Test Database and Collection

To test that MongoDB can store and retrieve information, I will create a small database for the exercise.

First, I will open the shell using the administrator account:

```bash
mongosh -u siteAdmin --authenticationDatabase admin -p
```

I will then create or switch to a database called `data606`:

```javascript
use data606
```

Next, I will insert a sample document into a collection called `students`:

```javascript
db.students.insertOne({
  name: "Salma",
  course: "Data 606",
  technology: "MongoDB"
})
```

MongoDB should return a response confirming that the document was inserted.

To check the stored information, I will run:

```javascript
db.students.find()
```

The document I inserted should appear in the results.

This will allow me to test the basic operations of creating a database, inserting a document and retrieving information.

## 16. Useful MongoDB Commands

The following commands will be useful when managing the MongoDB service:

| Command | Purpose |
|---|---|
| `sudo systemctl start mongod` | Start MongoDB |
| `sudo systemctl stop mongod` | Stop MongoDB |
| `sudo systemctl restart mongod` | Restart MongoDB |
| `sudo systemctl status mongod` | Check the service status |
| `sudo systemctl enable mongod` | Start MongoDB automatically after a restart |
| `mongod --version` | Check the server version |
| `mongosh --version` | Check the shell version |
| `mongosh` | Open the MongoDB Shell |

## 17. Security Considerations

There are a few security points I need to consider when configuring MongoDB on AWS:

- Keep the private SSH key secure and never share it.
- Use a strong password for the MongoDB administrator account.
- Keep MongoDB authentication enabled.
- Keep MongoDB bound to `127.0.0.1` for this exercise.
- Do not expose port `27017` to the public internet.
- Restrict SSH access on port `22` to my trusted IP address.

If I need to connect to MongoDB Compass from my Mac, I can use an SSH tunnel rather than opening the MongoDB port publicly.

## 18. Optional: Connect Using MongoDB Compass

If I want to access MongoDB through MongoDB Compass on my Mac, I can create an SSH tunnel.

I will open another Mac Terminal window and run:

```bash
ssh -i ~/.ssh/<PRIVATE_KEY_FILE>.pem -L 27017:127.0.0.1:27017 ubuntu@<PUBLIC_IP_ADDRESS>
```

I will keep this terminal session open while using Compass.

In MongoDB Compass, I will use this connection string:

```text
mongodb://localhost:27017/?authSource=admin
```

I will then enter the administrator username and password.

This allows me to connect through SSH without making MongoDB publicly accessible.

## 19. Troubleshooting

Some possible problems I may encounter during the installation include:

| Error | Possible reason | What I will check |
|---|---|---|
| `Unable to locate package mongodb-org` | The MongoDB repository may not have been added correctly. | Check the repository file and run `sudo apt update`. |
| `NO_PUBKEY` | The MongoDB signing key may be missing or incorrect. | Repeat the GPG key import step. |
| `Unit mongod.service not found` | MongoDB may not have installed correctly. | Check the installation and run `sudo systemctl daemon-reload`. |
| `Failed to connect to 127.0.0.1:27017` | The MongoDB service may not be running. | Check the service using `sudo systemctl status mongod`. |
| `Authentication failed` | The username, password or authentication database may be incorrect. | Check the credentials and use `--authenticationDatabase admin`. |
| `Connection refused` | MongoDB may not be listening on the expected port. | Check the configuration and service status. |

If MongoDB fails to start, I can inspect the service logs using:

```bash
sudo journalctl -u mongod -n 50 --no-pager
```

## 20. Conclusion

This document outlines the steps I plan to follow to install and configure MongoDB Community Edition on an Ubuntu EC2 instance.

The process includes preparing Ubuntu, adding the official MongoDB repository, installing the database, starting the service and configuring authentication.

I will also test the installation by creating a database and collection, inserting a document and retrieving it.

At the moment, I have prepared the documentation, but I have not completed the practical installation because I am experiencing SSH connection issues with my EC2 instance. Once I resolve the connection problem, I can follow these steps and record the results.

## 21. Official Documentation

- [MongoDB Community Edition Installation](https://www.mongodb.com/docs/manual/administration/install-community/)
- [MongoDB Supported Platforms](https://www.mongodb.com/docs/community-platform-support/)
- [MongoDB Configuration File](https://www.mongodb.com/docs/manual/reference/configuration-options/)
- [Enable Authentication](https://www.mongodb.com/docs/manual/tutorial/enable-authentication/)
- [MongoDB Shell Documentation](https://www.mongodb.com/docs/mongodb-shell/)