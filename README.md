# Social-App

## Getting Started: 🚀

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋
1. first of all, You need to install python for running pip command
2. create a project folder  

### Local Development
1. Clone the repository inside this folder
```bash
https://github.com/divyanshkumarworks/heavy-reminder.git
```

2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

5. Run database migrations using:
```bash
python manage.py makemigrations

python manage.py migrate
```
it will create the database schemas, tables and relationships. 

6. And then run:
```bash
python manage.py runserver
```
this command will run the local server. 

In addition, An ngrok server is required so that Twilio can locate your server and invoke the webhooks on every call status update.
