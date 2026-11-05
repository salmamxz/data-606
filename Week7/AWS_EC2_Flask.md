# AWS EC2 Cloud Infrastructure and Application Deployment Lab

## 1. Video Analysis: Inside a Cloud Data Centre

**Reference video:** [Touring Inside a Hyper-Scale Cloud Data Center](https://youtu.be/XZmGGAbHqa0)

After watching the video, I looked at how large cloud data centres are organised and how they maintain reliable services.

These are some of the main things I noticed:

### Physical infrastructure and modular design

- Servers are organised into standardised racks.
- Hot and cold aisle layouts help manage airflow and keep equipment at the right temperature.
- The modular design makes it easier to expand infrastructure when more computing capacity is needed.

### Redundancy and reliability

- Data centres use backup systems to reduce downtime.
- These include uninterruptible power supplies (UPS), backup generators and redundant cooling systems.
- Multiple network connections help maintain connectivity if one connection fails.
- Redundancy helps keep services available even when individual components experience problems.

### Physical security

- Access to server areas is restricted.
- Biometric checks and security checkpoints help prevent unauthorised access.
- CCTV monitoring is used to maintain security across the facilities.

### Environmental management

- Data centres generate a lot of heat because of the number of servers operating simultaneously.
- Cooling systems help maintain safe operating temperatures.
- Some facilities use liquid cooling and specialised airflow systems to manage higher computing demands.

---

## 2. Cloud Resource Decision Factors

When choosing a cloud provider or infrastructure, there are several things to consider.

| Factor | What it means | Practical considerations |
|---|---|---|
| Ease of use | How easy it is to create, configure and manage cloud resources using a web console, command line or APIs. | Easier management can save time, but resources still need to be monitored and managed properly. |
| Robustness | How well the infrastructure handles failures and keeps applications available. | Backup systems and multiple availability zones improve reliability but can increase costs. |
| Flexibility | How easily resources can be increased, reduced or adapted when requirements change. | Scaling helps prevent performance problems, but unnecessary resources can increase costs. |
| Cost | The overall cost of using cloud services, including computing, storage and networking. | Pay-as-you-go pricing reduces upfront costs, but unused resources can still generate charges. |

---

## 3. Comparison of Major Cloud Providers

I compared the three main cloud providers: AWS, Microsoft Azure and Google Cloud Platform.

| Feature | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Market position | One of the largest cloud providers, with a wide range of services. | Strong enterprise adoption and Microsoft integration. | Particularly strong in data analytics, AI and Kubernetes. |
| Computing | Amazon EC2 | Azure Virtual Machines | Google Compute Engine |
| Object storage | Amazon S3 | Azure Blob Storage | Google Cloud Storage |
| Networking | Amazon VPC, Route 53 and CloudFront | Azure Virtual Network, Azure DNS and Azure Front Door | VPC, Cloud DNS and Cloud CDN |
| Main advantage | Large service ecosystem and extensive documentation. | Good integration with Microsoft products and enterprise environments. | Strong data analytics and machine learning services. |

### My understanding

All three providers offer similar core cloud infrastructure, but they have different strengths.

- AWS offers a wide range of services and is particularly useful for learning cloud infrastructure.
- Azure is a strong option for organisations already using Microsoft technologies.
- Google Cloud is particularly well known for data analytics, machine learning and Kubernetes.

For this lab, I used AWS EC2 to create and manage my cloud infrastructure.

---

## 4. SSH Key Setup and EC2 Authentication

### 4.1 Preparing the SSH key

Before connecting to my EC2 instance, I needed to prepare the private SSH key downloaded from AWS.

I used my Mac Terminal.

First, I created the SSH directory:

```bash
mkdir -p ~/.ssh
```

Then I moved my downloaded key into that directory:

```bash
mv ~/Downloads/DataStudents.pem ~/.ssh/
```

I changed the permissions so that only my user account could read the private key:

```bash
chmod 400 ~/.ssh/DataStudents.pem
```

Finally, I checked the permissions:

```bash
ls -l ~/.ssh/DataStudents.pem
```

The expected permissions are:

```text
-r--------
```

This is important because SSH will reject private keys that have permissions that are too open.

### 4.2 Connecting to the EC2 instance

Once the key was ready, I connected to my Ubuntu EC2 instance using SSH.

```bash
ssh -i ~/.ssh/DataStudents.pem ubuntu@<EC2_PUBLIC_IP>
```

I used the `ubuntu` username because my instance was running Ubuntu.

### 4.3 Troubleshooting SSH connection issues

Initially, I experienced connection timeouts when trying to connect to my EC2 instance.

I checked my current public IP address:

```bash
curl -4 https://checkip.amazonaws.com
```

I also tested whether port 22 was reachable:

```bash
nc -vz -w 5 <EC2_PUBLIC_IP> 22
```

I then checked the AWS Security Group configuration.

The SSH inbound rule needed to allow:

- Type: SSH
- Port: 22
- Protocol: TCP
- Source: My current public IP address, using a `/32` CIDR range.

This helped me understand that SSH connectivity depends on both the key configuration and the network security settings in AWS.

---

## 5. Creating the AWS EC2 Instance

I used the AWS Management Console to create my EC2 instance.

### Steps followed

1. Logged in to the AWS Management Console.
2. Opened the EC2 Dashboard.
3. Selected **Launch instance**.
4. Added a name for the instance.
5. Selected Ubuntu as the operating system.
6. Selected an appropriate instance type.
7. Selected my existing SSH key pair.
8. Configured the network and Security Group rules.
9. Reviewed the storage settings.
10. Launched the instance.

### Instance configuration

| Setting | Configuration |
|---|---|
| Service | Amazon EC2 |
| Operating system | Ubuntu |
| Instance type | t2.micro or t3.micro, depending on availability and eligibility |
| Authentication | SSH key pair |
| SSH port | 22 |
| Flask application port | 5000 during initial testing |
| MongoDB port | 27017, restricted to local access |
| Storage | 8 GiB EBS volume |

*Note: Free Tier eligibility depends on the AWS account, instance type and current AWS pricing conditions.*

### Security Group configuration

During the initial application testing, I configured the following ports:

| Type | Port | Purpose |
|---|---:|---|
| SSH | 22 | Remote terminal access |
| Custom TCP | 5000 | Flask application testing |
| Custom TCP | 27017 | MongoDB access, if required |

For security, SSH should only be accessible from my own IP address.

MongoDB should not be exposed publicly. In my final architecture, it remains accessible through the local EC2 instance.

After completing a lab, I can stop or terminate resources that are no longer required to avoid unnecessary AWS charges.

---

## 6. Installing and Configuring MongoDB

### 6.1 Creating the installation script

Rather than installing MongoDB commands individually every time, I created a Bash script called:

`mongo_setup.sh`

The purpose of this script was to automate the installation and configuration of MongoDB Community Server.

```bash
#!/usr/bin/env bash

# MongoDB Community Server Installation Script
# Target: Supported Ubuntu LTS environments

set -euo pipefail

echo "==> Starting MongoDB deployment..."

# Check that the script is running with root permissions
if [[ "$(id -u)" -ne 0 ]]; then
    echo "[-] Please execute this script using sudo."
    exit 1
fi

# 1. Update package lists and install dependencies
echo "==> Updating package indices..."

apt-get update -y
apt-get install -y gnupg curl

# 2. Import MongoDB official signing key
echo "==> Importing MongoDB signing key..."

install -m 0755 -d /usr/share/keyrings

curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
    gpg --dearmor --yes -o /usr/share/keyrings/mongodb-server-7.0.gpg

# 3. Configure MongoDB repository
echo "==> Configuring MongoDB repository..."

UBUNTU_CODENAME="$(grep VERSION_CODENAME /etc/os-release | cut -d= -f2)"

# Repository fallback used in the original lab script
if [[ "$UBUNTU_CODENAME" != "jammy" && "$UBUNTU_CODENAME" != "focal" ]]; then
    REPO_TARGET="jammy"
else
    REPO_TARGET="$UBUNTU_CODENAME"
fi

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu ${REPO_TARGET}/mongodb-org/7.0 multiverse" | \
    tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# 4. Install MongoDB
echo "==> Installing MongoDB packages..."

apt-get update -y
apt-get install -y mongodb-org

# 5. Enable and start MongoDB
echo "==> Starting MongoDB service..."

systemctl daemon-reload
systemctl enable --now mongod

# 6. Verify service status
if systemctl is-active --quiet mongod; then
    echo "[+] MongoDB is running successfully on port 27017."
else
    echo "[-] MongoDB failed to start."
    echo "Check logs using: journalctl -u mongod -e"
    exit 1
fi
```

**Important:** The repository configuration above reflects the original lab script. Before reusing it on another Ubuntu release, I would check that MongoDB officially supports that release and use its matching repository rather than relying on the Jammy fallback.

### 6.2 Transferring the script to EC2

I transferred the script from my Mac to the EC2 instance using SCP.

```bash
scp -i ~/.ssh/DataStudents.pem mongo_setup.sh ubuntu@<EC2_PUBLIC_IP>:~
```

Then I connected to the instance:

```bash
ssh -i ~/.ssh/DataStudents.pem ubuntu@<EC2_PUBLIC_IP>
```

I made the script executable:

```bash
chmod +x mongo_setup.sh
```

Finally, I ran it:

```bash
sudo ./mongo_setup.sh
```

### 6.3 Troubleshooting the Bash script

I encountered an issue where the script returned errors such as:

```text
[[: not found
source: not found
```

After investigating, I found that there was an empty line before the Bash shebang.

The shebang tells Ubuntu which interpreter should execute the script.

It needs to be the first line:

```bash
#!/usr/bin/env bash
```

I fixed the issue using:

```bash
sed -i '1{/^$/d;}' mongo_setup.sh
```

I then checked the first line:

```bash
head -n 1 mongo_setup.sh
```

After correcting it, the script executed successfully.

---

## 7. MongoDB Database Configuration

### 7.1 Creating a database and inserting a test record

Once MongoDB was installed, I opened the MongoDB shell:

```bash
mongosh
```

I created a database called `data606` and inserted a test student record.

```javascript
use data606

db.students.insertOne({
    name: "Example Student",
    course: "Data 606",
    technology: "MongoDB"
})
```

This created a `students` collection and inserted a document.

### 7.2 Creating an administrative user

I switched to the admin database:

```javascript
use admin
```

Then I created an administrative user:

```javascript
db.createUser({
    user: "siteAdmin",
    pwd: passwordPrompt(),
    roles: [
        {
            role: "root",
            db: "admin"
        }
    ]
})
```

Using `passwordPrompt()` meant that I could enter the password interactively rather than writing it directly into the command.

I then exited the MongoDB shell:

```javascript
exit
```

### 7.3 Enabling MongoDB authentication

I edited the MongoDB configuration file:

```bash
sudo nano /etc/mongod.conf
```

I checked that the following settings were present:

```yaml
net:
  port: 27017
  bindIp: 127.0.0.1

security:
  authorization: enabled
```

The `bindIp` setting restricts MongoDB to local connections.

The `authorization: enabled` setting ensures that users must authenticate before accessing the database.

I restarted MongoDB to apply the changes:

```bash
sudo systemctl restart mongod
```

I checked the service status:

```bash
sudo systemctl status mongod
```

### 7.4 Testing MongoDB authentication

I tested the administrative account:

```bash
mongosh -u siteAdmin --authenticationDatabase admin -p
```

I entered the password when prompted.

This confirmed that authentication was working.

### 7.5 Connecting through MongoDB Compass using SSH tunnelling

I also wanted to inspect my remote MongoDB database visually using MongoDB Compass on my Mac.

Instead of opening port 27017 publicly, I used an SSH tunnel.

I ran:

```bash
ssh -i ~/.ssh/DataStudents.pem -L 27018:127.0.0.1:27017 ubuntu@<EC2_PUBLIC_IP>
```

This forwards my Mac's local port 27018 to MongoDB's port 27017 on the EC2 instance.

I used port 27018 locally because port 27017 was already being used by my local MongoDB installation.

In MongoDB Compass, I configured the connection using:

| Setting | Value |
|---|---|
| Host | 127.0.0.1 |
| Port | 27018 |
| Authentication | Username and Password |
| Username | siteAdmin |
| Authentication Database | admin |

I entered my database password in the Compass interface.

This allowed me to access the remote database without exposing MongoDB directly to the internet.

---

## 8. Flask Application Integration

### 8.1 Preparing the Python environment

After setting up MongoDB, I created a directory for my Flask application.

```bash
mkdir -p ~/flask-app
cd ~/flask-app
```

I installed the required Python packages:

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip
```

I created a virtual environment:

```bash
python3 -m venv venv
```

I activated it:

```bash
source venv/bin/activate
```

Then I installed Flask and PyMongo:

```bash
pip install Flask pymongo
```

### 8.2 Creating the Flask application

I created a Python file called:

`app.py`

The application connects Flask to MongoDB and provides an endpoint for retrieving student records.

One important issue I had to consider was password encoding.

MongoDB connection strings use special characters for separating different parts of the connection details. Characters such as `@`, `:` and `/` can cause problems if they appear in an unencoded password.

I used `quote_plus` from `urllib.parse` to handle this.

```python
from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from urllib.parse import quote_plus
import os

app = Flask(__name__)

# Retrieve and encode the MongoDB password
raw_password = os.environ.get("MONGO_PASSWORD", "")
encoded_password = quote_plus(raw_password)

# Connect to the local MongoDB service
client = MongoClient(
    f"mongodb://siteAdmin:{encoded_password}@127.0.0.1:27017/?authSource=admin"
)

db = client["data606"]
students_collection = db["students"]


@app.route("/")
def home():
    return """
    <h1>Welcome to my Flask application!</h1>
    <p>Hosted on AWS EC2.</p>
    <p>Connected to MongoDB.</p>
    <p><a href="/api/students">View students</a></p>
    """


@app.route("/api/students", methods=["GET"])
def get_students():
    try:
        records = list(
            students_collection.find({}, {"_id": 0})
        )
        return jsonify(records), 200

    except PyMongoError as err:
        return jsonify({
            "error": "Database query failure",
            "details": str(err)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### 8.3 Configuring the environment variable

I wanted to avoid storing my MongoDB password directly in the Python source code.

I therefore used an environment variable.

For my initial testing session, I configured it using:

```bash
export MONGO_PASSWORD='YOUR_MONGODB_PASSWORD'
```

I checked that it was configured without displaying the actual password:

```bash
echo ${MONGO_PASSWORD:+Password configured}
```

Expected output:

```text
Password configured
```

### 8.4 Running Flask

I started the application:

```bash
python app.py
```

I then tested it through my browser.

The application was available at:

```text
http://<EC2_PUBLIC_IP>:5000/
```

The API endpoint was:

```text
http://<EC2_PUBLIC_IP>:5000/api/students
```

I also tested the endpoint directly from the EC2 terminal:

```bash
curl -i http://127.0.0.1:5000/api/students
```

Expected response:

```json
[
    {
        "course": "Data 606",
        "name": "Example Student",
        "technology": "MongoDB"
    }
]
```

Receiving a `200 OK` response confirmed that Flask was communicating with MongoDB successfully.

---

# Flask on EC2: Extension Challenges

## 9. Extension Selection and Progress

After completing the initial Flask and MongoDB integration, I looked at additional challenges to improve the application.

The following table shows the extensions I worked on or explored.

| Extension | Description | Status |
|---|---|---|
| 1. Create a JSON API | Create endpoints for retrieving student records and individual records. | Completed |
| 7. Use environment variables | Keep database credentials outside the Python source code. | Completed |
| 3. Add CRUD operations | Implement Create, Read, Update and Delete functionality. | Extended solution prepared |
| 8. Keep the application running | Use Gunicorn and systemd to keep Flask running after disconnecting from SSH. | Implementation prepared |
| 9. Add Nginx reverse proxy | Use Nginx to receive HTTP requests and forward them to Flask. | Implementation prepared |

The additional solutions below demonstrate how I would extend the initial application.

---

## 10. Evidence of Completed Work

### 10.1 Environment variable configuration

I configured the MongoDB password as an environment variable on the EC2 instance.

For verification, I used:

```bash
echo ${MONGO_PASSWORD:+Password configured}
```

The terminal returned:

```text
Password configured
```

This confirmed that the environment variable was available without exposing the password.

### 10.2 Testing the JSON API

I tested the collection endpoint:

```text
GET /api/students
```

The application returned:

```text
200 OK
```

I also tested an individual student ID that did not exist:

```text
GET /api/students/000000000000000000000000
```

The application returned:

```text
404
```

This confirmed that the API could distinguish between an existing record and a record that could not be found.

---

## 11. Implementing CRUD Operations

CRUD stands for:

- **Create:** Add a new record.
- **Read:** Retrieve existing records.
- **Update:** Modify an existing record.
- **Delete:** Remove a record.

I extended the original Flask application to support these operations using MongoDB and PyMongo.

### 11.1 Full Flask application with CRUD functionality

The following implementation includes:

- `GET /api/students`: Retrieve all student records.
- `GET /api/students/<student_id>`: Retrieve one student.
- `POST /api/students`: Create a new student.
- `PUT /api/students/<student_id>`: Update a student.
- `DELETE /api/students/<student_id>`: Delete a student.

```python
import os
from urllib.parse import quote_plus

from bson.errors import InvalidId
from bson.objectid import ObjectId

from flask import Flask, jsonify, request

from pymongo import MongoClient
from pymongo.errors import PyMongoError


app = Flask(__name__)


# Secure configuration using environment variables
raw_password = os.environ.get("MONGO_PASSWORD")

if not raw_password:
    raise RuntimeError(
        "MONGO_PASSWORD environment variable is not set"
    )

encoded_password = quote_plus(raw_password)

client = MongoClient(
    f"mongodb://siteAdmin:{encoded_password}@127.0.0.1:27017/?authSource=admin"
)

db = client["data606"]
students = db["students"]


def serialize_doc(doc):
    """Convert MongoDB ObjectId into a string for JSON output."""

    if not doc:
        return None

    doc["id"] = str(doc.pop("_id"))

    return doc


# Home page
@app.route("/")
def home():
    return """
    <h1>Flask Data API</h1>
    <p>Running on AWS EC2 Ubuntu.</p>
    <ul>
        <li><a href="/api/students">GET /api/students</a></li>
    </ul>
    """


# 1. READ ALL STUDENTS
@app.route("/api/students", methods=["GET"])
def get_students():

    try:
        records = [
            serialize_doc(doc)
            for doc in students.find()
        ]

        return jsonify(records), 200

    except PyMongoError as e:
        return jsonify({
            "error": "Database read error",
            "details": str(e)
        }), 500


# 2. READ ONE STUDENT
@app.route("/api/students/<student_id>", methods=["GET"])
def get_student(student_id):

    try:
        doc = students.find_one({
            "_id": ObjectId(student_id)
        })

        if not doc:
            return jsonify({
                "error": "Record not found",
                "requested_id": student_id
            }), 404

        return jsonify(serialize_doc(doc)), 200

    except InvalidId:
        return jsonify({
            "error": "Invalid identifier format",
            "message": "ID must be a 24-character hexadecimal string"
        }), 400

    except PyMongoError as e:
        return jsonify({
            "error": "Database error",
            "details": str(e)
        }), 500


# 3. CREATE A STUDENT
@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid or missing JSON payload"
        }), 400

    required_fields = ["name", "course", "technology"]

    missing = [
        field for field in required_fields
        if field not in data
    ]

    if missing:
        return jsonify({
            "error": "Missing required fields",
            "fields": missing
        }), 422

    payload = {
        "name": str(data["name"]),
        "course": str(data["course"]),
        "technology": str(data["technology"])
    }

    try:
        result = students.insert_one(payload)

        created = students.find_one({
            "_id": result.inserted_id
        })

        return jsonify(serialize_doc(created)), 201

    except PyMongoError as e:
        return jsonify({
            "error": "Insertion failure",
            "details": str(e)
        }), 500


# 4. UPDATE A STUDENT
@app.route("/api/students/<student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Missing or invalid JSON body"
        }), 400

    update_fields = {}

    for field in ["name", "course", "technology"]:
        if field in data:
            update_fields[field] = str(data[field])

    if not update_fields:
        return jsonify({
            "error": "No valid updatable fields provided"
        }), 400

    try:
        result = students.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": update_fields}
        )

        if result.matched_count == 0:
            return jsonify({
                "error": "Record not found"
            }), 404

        updated = students.find_one({
            "_id": ObjectId(student_id)
        })

        return jsonify(serialize_doc(updated)), 200

    except InvalidId:
        return jsonify({
            "error": "Invalid identifier format"
        }), 400

    except PyMongoError as e:
        return jsonify({
            "error": "Update failure",
            "details": str(e)
        }), 500


# 5. DELETE A STUDENT
@app.route("/api/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):

    try:
        result = students.delete_one({
            "_id": ObjectId(student_id)
        })

        if result.deleted_count == 0:
            return jsonify({
                "error": "Record not found"
            }), 404

        return jsonify({
            "message": "Record successfully removed",
            "id": student_id
        }), 200

    except InvalidId:
        return jsonify({
            "error": "Invalid identifier format"
        }), 400

    except PyMongoError as e:
        return jsonify({
            "error": "Deletion failure",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
```

### 11.2 Understanding the API responses

| HTTP method | Endpoint | Expected response |
|---|---|---|
| GET | `/api/students` | 200 OK |
| GET | `/api/students/<id>` | 200 OK or 404 Not Found |
| POST | `/api/students` | 201 Created |
| PUT | `/api/students/<id>` | 200 OK or 404 Not Found |
| DELETE | `/api/students/<id>` | 200 OK or 404 Not Found |

The application also handles invalid MongoDB IDs using the `InvalidId` exception.

---

## 12. Keeping the Application Running

### 12.1 Why the development server is not enough

Initially, I started Flask using:

```bash
python app.py
```

This works for testing, but there is a limitation.

The application runs inside the active SSH session. If I disconnect from the terminal, the process can stop.

I therefore looked at how to keep the application running independently.

For this, I used Gunicorn and systemd.

### 12.2 Installing Gunicorn

I entered the Flask application directory:

```bash
cd ~/flask-app
```

I activated the virtual environment:

```bash
source venv/bin/activate
```

Then I installed Gunicorn:

```bash
pip install gunicorn
```

Gunicorn is a WSGI server that can run Flask applications without relying on Flask's development server.

### 12.3 Creating a systemd service

I created a service file:

```bash
sudo nano /etc/systemd/system/flaskapp.service
```

Example configuration:

```ini
[Unit]
Description=Gunicorn instance to serve Flask Application
After=network.target mongod.service
Wants=mongod.service

[Service]
User=ubuntu
Group=ubuntu

WorkingDirectory=/home/ubuntu/flask-app

Environment="PATH=/home/ubuntu/flask-app/venv/bin"
EnvironmentFile=/etc/flaskapp.env

ExecStart=/home/ubuntu/flask-app/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 app:app

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

I used an environment file rather than placing the actual MongoDB password directly in the service configuration.

To create it:

```bash
sudo nano /etc/flaskapp.env
```

Inside the file:

```text
MONGO_PASSWORD=YOUR_MONGODB_PASSWORD
```

I restricted access to this file:

```bash
sudo chown root:root /etc/flaskapp.env
sudo chmod 600 /etc/flaskapp.env
```

### 12.4 Starting the service

I reloaded systemd:

```bash
sudo systemctl daemon-reload
```

I enabled the service so it could start automatically:

```bash
sudo systemctl enable flaskapp
```

I started the application:

```bash
sudo systemctl start flaskapp
```

Finally, I checked its status:

```bash
sudo systemctl status flaskapp
```

This approach allows the Flask application to run independently of my SSH session.

---

## 13. Adding Nginx as a Reverse Proxy

### 13.1 What is Nginx?

Nginx is a web server that can also act as a reverse proxy.

Instead of allowing external users to access the Flask application directly through port 5000, Nginx receives incoming HTTP requests on port 80 and forwards them to Gunicorn.

This provides a cleaner application architecture and keeps Gunicorn listening only on the local machine.

### 13.2 Installing Nginx

I would install Nginx using:

```bash
sudo apt update
sudo apt install -y nginx
```

Then I created a configuration file:

```bash
sudo nano /etc/nginx/sites-available/flaskapp
```

### 13.3 Configuring the reverse proxy

I added the following configuration:

```nginx
server {
    listen 80;

    server_name <EC2_PUBLIC_IP>;

    location / {
        proxy_pass http://127.0.0.1:5000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 13.4 Enabling the configuration

I created a symbolic link:

```bash
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/
```

I removed the default configuration:

```bash
sudo rm -f /etc/nginx/sites-enabled/default
```

I checked the Nginx configuration:

```bash
sudo nginx -t
```

If the configuration was valid, I restarted Nginx:

```bash
sudo systemctl restart nginx
```

I could then access the application using:

```text
http://<EC2_PUBLIC_IP>/
```

Nginx would receive the request and forward it to Gunicorn.

*For a real production deployment, I would also configure HTTPS using a valid SSL/TLS certificate.*

---

## 14. Application Architecture and Data Flow

The following diagram shows how the different components work together.

```text
+--------------------------------------------------+
|                 Client / Browser                 |
+--------------------------------------------------+
                       |
                       |
                 HTTP Port 80
                       |
                       v
+--------------------------------------------------+
|                   AWS EC2                        |
|                                                  |
|  +--------------------------------------------+  |
|  |                  Nginx                     |  |
|  |          Reverse Proxy - Port 80           |  |
|  +--------------------------------------------+  |
|                       |                          |
|                       |                          |
|                127.0.0.1:5000                    |
|                       |                          |
|                       v                          |
|  +--------------------------------------------+  |
|  |                 Gunicorn                   |  |
|  |              WSGI Server                   |  |
|  +--------------------------------------------+  |
|                       |                          |
|                       v                          |
|  +--------------------------------------------+  |
|  |                 Flask App                  |  |
|  |             Python Application             |  |
|  +--------------------------------------------+  |
|                       |                          |
|                       |                          |
|                127.0.0.1:27017                   |
|                       |                          |
|                       v                          |
|  +--------------------------------------------+  |
|  |                  MongoDB                    |  |
|  |       data606 Database / students           |  |
|  +--------------------------------------------+  |
|                                                  |
+--------------------------------------------------+
```

### Understanding the data flow

1. A user opens the application in a browser.
2. The request reaches the AWS EC2 instance.
3. Nginx receives the request on port 80.
4. Nginx forwards it to Gunicorn on port 5000.
5. Gunicorn passes the request to the Flask application.
6. Flask communicates with MongoDB using PyMongo.
7. MongoDB retrieves the requested information.
8. Flask returns the response as JSON.
9. Nginx sends the response back to the browser.

This shows how the different technologies work together to create a cloud-hosted application.

---

## 15. Final Security Group Configuration

For the Nginx architecture, I would use the following Security Group configuration:

| Type | Port | Source | Purpose |
|---|---:|---|---|
| SSH | 22 | My public IP `/32` | Secure administrative access |
| HTTP | 80 | `0.0.0.0/0` | Public web application access |
| Custom TCP | 5000 | Not publicly open | Internal Gunicorn communication |
| Custom TCP | 27017 | Not publicly open | Internal MongoDB communication |

MongoDB and Gunicorn should only accept local connections.

This reduces the number of publicly accessible services and improves the overall security of the application.

---

## 16. Troubleshooting and Lessons Learned

During this lab, I encountered several issues. Working through them helped me understand how the different parts of the infrastructure communicate.

### Issue 1: MongoDB connection string and special characters

**Problem**

The Flask application returned an error similar to:

```text
pymongo.errors.InvalidURI:
Username and password must be escaped according to RFC 3986
```

**Cause**

My MongoDB password contained a special character such as `@`.

This character has a specific meaning in a MongoDB connection string. If it is not encoded, it can cause the connection string to be interpreted incorrectly.

**Solution**

I used `quote_plus`:

```python
from urllib.parse import quote_plus

mongo_password = quote_plus(
    os.environ["MONGO_PASSWORD"]
)
```

This encoded the password before using it in the MongoDB URI.

**What I learned**

Passwords should be handled carefully when they contain special characters, particularly when they are included in connection strings.

### Issue 2: Bash script shebang error

**Problem**

When executing my MongoDB installation script, I received:

```text
[[: not found
source: not found
```

**Cause**

There was an empty line before the Bash shebang.

The script was not being interpreted using Bash as expected.

**Solution**

I removed the empty first line:

```bash
sed -i '1{/^$/d;}' mongo_setup.sh
```

I checked the result:

```bash
head -n 1 mongo_setup.sh
```

The first line was then:

```bash
#!/usr/bin/env bash
```

**What I learned**

The shebang needs to be the first line of a script because it tells the operating system which interpreter to use.

### Issue 3: SSH port forwarding conflict

**Problem**

When I attempted to create an SSH tunnel, I received an error similar to:

```text
bind [::1]:27017: Address already in use
```

**Cause**

My Mac already had a local MongoDB service using port 27017.

This meant that the same port could not be used for the local side of the SSH tunnel.

**Solution**

I selected a different local port:

```bash
ssh -i ~/.ssh/DataStudents.pem \
-L 27018:127.0.0.1:27017 \
ubuntu@<EC2_PUBLIC_IP>
```

I could then use port 27018 in MongoDB Compass while the remote MongoDB service continued using port 27017.

**What I learned**

SSH port forwarding allows me to connect to remote services securely without needing to expose their ports publicly.

### Issue 4: Flask application stopped after disconnecting from SSH

**Problem**

The Flask application stopped when the SSH session ended.

**Cause**

I was running the application using:

```bash
python app.py
```

This was the development server running inside my interactive terminal session.

**Solution**

I explored using Gunicorn and systemd to run the application as a background service.

**What I learned**

There is a difference between running an application for development and running it as a persistent service.

---

## 17. Project Files

The main files used for this project are organised as follows:

```text
flask-app/
│
├── app.py
│
├── mongo_setup.sh
│
├── requirements.txt
│
├── .gitignore
│
└── venv/
```

### 17.1 requirements.txt

I used a requirements file to document the Python dependencies.

```text
Flask==3.1.3
pymongo==4.19.0
gunicorn==23.0.0
dnspython==2.9.2
```

The dependencies can be installed using:

```bash
pip install -r requirements.txt
```

### 17.2 .gitignore

I created a `.gitignore` file to prevent unnecessary or sensitive files from being uploaded to GitHub.

```gitignore
venv/
__pycache__/
*.pyc
.env
*.pem
.DS_Store
```

I would also avoid committing passwords, database credentials or private configuration files.

---

## 18. Final Reflection

This lab helped me understand how to deploy an application using cloud infrastructure and connect different technologies together.

I started by creating an AWS EC2 instance and connecting to it remotely using SSH. I then installed MongoDB, configured authentication and created a database with a collection for student records.

After that, I created a Flask application using Python and PyMongo to retrieve information from MongoDB through a JSON API.

I also explored additional extensions, including CRUD operations, environment variables, Gunicorn, systemd and Nginx.

Some of the main things I learned were:

- How to create and manage an AWS EC2 instance.
- How SSH authentication and Security Groups work.
- How to install and configure MongoDB on Ubuntu.
- How to create databases, collections and users in MongoDB.
- How to connect MongoDB Compass to a remote database using SSH tunnelling.
- How to build a Flask application that communicates with MongoDB.
- How to create JSON API endpoints and handle HTTP status codes.
- How to manage sensitive configuration using environment variables.
- How to troubleshoot connection, authentication and configuration issues.
- How Gunicorn, systemd and Nginx can be used to improve an application deployment.

Overall, the most useful part of this exercise was understanding how the different components connect and work together, rather than treating AWS, MongoDB and Flask as completely separate technologies.