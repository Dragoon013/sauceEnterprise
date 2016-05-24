# Sauce Labs: Selenium101 Training Course

You should be able to access the presentation at this location (temporarily) http://107.170.223.87:8080/selenium101.html

### Start Me!
In order to bring up the presentation - there are couple of things you can do.

#### Easiest:
* simply go into the directory and load the selenium101.html file in your browser. (Double clicking on it should bring it up in a browser right away)

#### Easy (if you have python installed):
* go into the folder/direfctory in a terminal
* run python -m SimpleHTTPServer
* open a browser and go to localhost:8000/selenium101.html

#### Medium (if you have nginx installed):
* go into the /etc/conf/conf.d directory
* create a new file called train.conf
* insert the following lines:
server {
   listen 8000;
   root /path/to/the/presentation_folder;

}

* nginx -s reload
* access the presentation at localhost:8000/selenium101.html
