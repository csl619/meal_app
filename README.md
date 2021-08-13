
# Weekly Meal Planner

A Django web application created for storing our family favourite meal recipes. The system then automatatically selects a meal for each night of the week and provides us with a shopping list for all the items required.

## Installation

#### Setting up Virtual Environment
On cloning the repository, you will need to navigate to the repository folder and set up a virtual environment:
```
python3 -m venv venv **creates the virtual environment called venv**
```

Once the virtual environment is created, activate it and install the required packages via the requirements.txt file,
deactivate the virtual environment once packages installed.

```
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
```
#### MySQL

The system uses a MySQL database as the database, you will need to have this installed on your server/machine you wish to
run the application from. Once installed you will need to create a new database called `meal_app`. To do this log into your
server and open a terminal window, type `mysql -u **yourusername** -p` and hit enter you will now be prompted for your user
password. Once you are in to the admin console for MySQL, type `create database meal_app;` and hit enter. The database is
now created.

#### Environment Variables

A sample of the .env file can be found in the repository called `sample.dotenv`, you need to duplicate this file and rename
to .env.
For the appplication to run correctly you will need to provide all the required environment variables listed on the sample
file.

#### Running initial migration and create superuser
Once you have created the database and input the required environment variables into the .env file you are ready to create
the database structure and create a admin superuser. Run the following commands from within the main directory for the meal app.
```
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
```
On creating the superuser you will be asked to enter your username, email address and a password twice for accessing the system.
Complete the steps and hit enter, this will provide a prompt confirming the account is created successfully. The app is now ready
to run this can be achieved by running the following command (or via a web server like Apache or Nginx):
```
python manage.py runserver
```

## Automation
The application requires you to set up a Cronjob to run the weekly process of selecting the meals and sending the emails
to the user accounts. To do this you need to run the following commands:

```
cd /etc/cron.d
nano generate_week
```
This will create a new cron entry for the weekly update, you need to enter the following in the nano editor and save:
```
0 7 * * * root /bin/bash **MEAL APP FOLDER LOCATION**/scripts/generate_week.sh >> /var/log/generate_week.log
```


## Screenshots

Below are a few screenshots from various areas of the site and the PDFs generated.

_New Profile:_
![New Profile](https://imgur.com/uBnbgeO.png)

_User Profile Page:_
![User Profile Page](https://imgur.com/3sdO0OM.png)

_Add Meal:_
![Add Meal](https://imgur.com/OdJUSyz.png)

_Example Week PDF:_
![Example Week PDF](https://imgur.com/KZpcV63.png)

_Example Meal PDF:_
![Example Meal PDF](https://imgur.com/xL7IYaq.png)
  
