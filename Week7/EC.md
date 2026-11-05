# AWS EC2 Setup and Mac Terminal SSH Connection Guide

This document outlines the complete process for creating, configuring and connecting to an Ubuntu EC2 instance on AWS using a custom SSH key pair from a macOS terminal.

## 1. Prerequisites and Key Generation

AWS instances authenticated via SSH require a matching public and private key pair. Since an existing private key (`.pem`) cannot be downloaded from AWS again after creation, a personal key pair can be generated.

1. Navigate to the **EC2 Console** under your target region (`eu-central-1`).
2. In the left navigation pane, under **Network & Security**, select **Key Pairs**.
3. Click **Create key pair** and configure the following settings:
   - **Name:** `salma-key`
   - **Key pair type:** `RSA`
   - **Private key file format:** `.pem`
4. Select **Create key pair**.
5. Save the downloaded `salma-key.pem` file in your local `~/Downloads` directory.

## 2. Launching the EC2 Instance

1. In the EC2 console sidebar, select **Instances** and click **Launch an instance**.
2. Configure the instance using the following settings:

   - **Name:** `data606-salma-mac`
   - **Application and OS Images (AMI):** Ubuntu Server 26.04 LTS (HVM), SSD Volume Type (64-bit x86).
   - **Instance type:** `t3.micro` (Free tier eligible).
   - **Key pair (login):** Select `salma-key`.

   **Network settings:**
   - **Auto-assign public IP:** Enabled.
   - **Firewall (security groups):** Select **Select existing security group** and choose `salma-sg`.
   - Ensure that inbound SSH traffic on port 22 is permitted.

   **Storage:**
   - 1 x 8 GiB gp3 root volume.

3. Click **Launch instance**.
4. Click [**View all instances**](https://eu-central-1.console.aws.amazon.com/ec2/home?region=eu-central-1#Instances:) and wait until the instance state changes from `Pending` to `Running`.

## 3. Retrieving Instance Details

1. Select the running instance (`data606-salma-mac`) from the instances list.
2. In the **Details** pane, copy the **Public IPv4 address**.

For example:

```text
18.198.187.44
```

The address may be different for your instance.

## 4. Connecting via macOS Terminal

Open the macOS Terminal application and execute the following commands in sequence.

### Step A: Navigate to the Directory Containing the Private Key

```bash
cd ~/Downloads
```

This changes the current directory to Downloads, where the private key was saved.

### Step B: Restrict Private Key Permissions

SSH requires private keys to be accessible only by their owner. If the permissions are too open, SSH may reject the key and display an `UNPROTECTED PRIVATE KEY FILE` error.

Run:

```bash
chmod 400 salma-key.pem
```

This restricts the file permissions so that only the owner can read the private key.

### Step C: Establish the SSH Connection

Use the default Ubuntu username and the public IPv4 address copied from the AWS console.

```bash
ssh -i salma-key.pem ubuntu@<PUBLIC_IP_ADDRESS>
```

Replace `<PUBLIC_IP_ADDRESS>` with the actual public IPv4 address of your EC2 instance, without the angle brackets.

For example:

```bash
ssh -i salma-key.pem ubuntu@18.198.187.44
```

### Step D: Accept the Host Fingerprint

When connecting for the first time, SSH may display a host authenticity message similar to the following:

```text
The authenticity of host '18.198.187.44 (...)' can't be established.
ED25519 key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Check that the address belongs to your instance. If it is correct, type:

```text
yes
```

Press **Enter** to continue.

## 5. Post-Connection Initialisation

Once the connection is successful, the terminal prompt will change to something similar to:

```bash
ubuntu@ip-172-31-xx-xx:~$
```

This confirms that you are connected to the Ubuntu instance.

Before installing additional software, update the package indexes and upgrade the available system packages:

```bash
sudo apt update && sudo apt upgrade -y
```

To close the SSH session and return to your local Mac terminal, run:

```bash
exit
```

## 6. Troubleshooting Common Issues

| Error | Root Cause | Solution |
|---|---|---|
| `No such file or directory` during `chmod` or `ssh` | The `.pem` file is not in `~/Downloads`, or macOS has added a `.txt` extension to the filename. | Run `ls -la ~/Downloads/*.pem` to check the file location and filename. |
| `Permissions 0644 are too open` or `UNPROTECTED PRIVATE KEY FILE` | The file permissions allow other users to access the private key. | Run `chmod 400 salma-key.pem`. |
| `Permission denied (publickey)` | The private key does not match the key pair selected when launching the instance. | Check that the instance was launched using `salma-key` and not `DataStudents`. Also check that the SSH username is `ubuntu`. |
| `Connection timed out` | Port 22 is blocked, the instance is not reachable, or the local public IP address has changed. | Check that the instance is running, has a public IP address and that the security group permits inbound SSH traffic on port 22 from your current public IP address. |

## 7. Security Considerations

- Keep private SSH keys confidential.
- Never share `.pem` files through Slack, email or other messaging platforms.
- Do not upload private keys to GitHub or other public repositories.
- Restrict SSH access to trusted IP addresses.
- Do not assume that creating a new key pair in AWS automatically grants access to an existing EC2 instance.
- If a private key is exposed, treat it as compromised and request a replacement. The replacement public key must also be installed on the instance through an authorised method.

## 8. Next Steps

Once connected to the Ubuntu instance, the next stage of the Data 606 exercise is to install and configure MongoDB Community Edition on the EC2 instance.

The installation should follow the official MongoDB documentation for Ubuntu 26.04 LTS.





