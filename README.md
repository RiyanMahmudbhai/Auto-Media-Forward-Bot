# Auto-Media-Forward-Bot

This project allows you to forward media (videos) from one Telegram channel to others using a Telegram bot.

## Requirements

- Python 3.x
- [Pyrogram](https://github.com/pyrogram/pyrogram) library
- [tgcrypto](https://github.com/pyrogram/tgcrypto) (optional for faster encryption)

## Installation

1. **Clone the Repository**

   First, clone the repository to your VPS:

   ```bash
   git clone https://github.com/RiyanMahmudbhai/Auto-Media-Forward-Bot.git
   cd Auto-Media-Forward-Bot
   ```bash
   
2. Create and Activate Virtual Environment

   Create a virtual environment in the project folder and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```bash
3. Install Dependencies

Install the required libraries from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```bash
Setup Systemd Service
1. Create the systemd Service Unit File
Create a new systemd service file at /etc/systemd/system/telegram-mediaforwad2bot.service:
   ```bash
   sudo nano /etc/systemd/system/telegram-mediaforwad2bot.service
   ```bash
2. Edit the Service File
Add the following configuration, customizing the paths to your project and virtual environment as needed:
   ```bash
   [Unit]
Description=Telegram Media Forward Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Auto-Media-Forward-Bot
ExecStart=/root/Auto-Media-Forward-Bot/venv/bin/python3 /root/Auto-Media-Forward-Bot/bot.py
Restart=always
RestartSec=10
Environment="PATH=/root/Auto-Media-Forward-Bot/venv/bin:/usr/bin:/bin"
Environment="VIRTUAL_ENV=/root/Auto-Media-Forward-Bot/venv"

[Install]
WantedBy=multi-user.target
   ```bash

3. Reload systemd and Start the Service
After saving and exiting the file (CTRL+X, then Y to confirm, and ENTER to save), reload the systemd daemon to apply the changes:

```bash
sudo systemctl daemon-reload
```bash
Then start the service with the following command:
```bash
sudo systemctl start telegram-mediaforwad2bot.service
```bash
4. Enable the Service to Start on Boot
To ensure the bot starts automatically on system boot, enable the service:

```bash
sudo systemctl enable telegram-mediaforwad2bot.service
```bash
5. Check the Service Status
You can check the status of the service to verify that it is running:
```bash
sudo systemctl status telegram-mediaforwad2bot.service
```bash
This will show you whether the bot is active and running.

6. Stop or Restart the Service (Optional)
If you need to stop or restart the service, you can use the following commands:

Stop the service:

```bash
sudo systemctl stop telegram-mediaforwad2bot.service
```bash
Restart the service:

```bash
sudo systemctl restart telegram-mediaforwad2bot.service
```bash
Usage
Once the bot is running, it will forward media (videos) from one Telegram channel to others as defined in the script. You can monitor the bot's logs using:

```bash
sudo journalctl -u telegram-mediaforwad2bot.service -f
```bash
This will show real-time logs for the bot.
























   
