# hueglucose
[![red_light.png](https://s9.postimg.org/46up7cxz3/red_light.png)](https://postimg.org/image/pgibi7e9n/) [![green_light.png](https://s9.postimg.org/6znwrvbbj/green_light.png)](https://postimg.org/image/4ic5klrez/)

Sets up a philips hue to display different lighting based on nightscout glucose values

## Dependencies
* Python 2.7
* Phue
* Python-nightscout

On ubuntu, this can be installed with the following commands
```bash
sudo pip install phue
sudo pip install git+https://github.com/ps2/python-nightscout.git
```

## Installation
```bash
git clone https://github.com/dabear/hueglucose.git
```

edit hueglucose.py, change the following variables:
* bridge_ip 
* lightname 
* nightscout_url 

Run it by executing hueglucose.py once manually. 
The very first time you run the script you must remember to press the big button on your philips hue bridge to authenticate. This is only needed the first time.

[![1_root_bjorninge-kodi_ssh_and_New_File.png](https://s26.postimg.org/bkkyabv21/1_root_bjorninge-kodi_ssh_and_New_File.png)](https://postimg.org/image/bkkyabv1x/)

## Running it periodically
I recommend running the script once a minute in a cron job.
On linux, type ```crontab -e```and add the following code
```bash
* * * * *  /home/bjorninge/code/hueglucose/hueglucose.py 2>&1 1> /tmp/hueglucose.log
```
Remember to replace the path to the script with your own. Any errors can be found by inspecting /tmp/hueglucose.log
