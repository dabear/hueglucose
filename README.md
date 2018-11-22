# hueglucose
[![red_light.png](https://s9.postimg.org/46up7cxz3/red_light.png)](https://postimg.org/image/pgibi7e9n/) [![green_light.png](https://s9.postimg.org/6znwrvbbj/green_light.png)](https://postimg.org/image/4ic5klrez/)

Sets up a philips hue to display different lighting based on nightscout glucose values

## Dependencies
* Python 2.7
* Phue
* Python-nightscout


## Installation
```bash
git clone https://github.com/dabear/hueglucose.git
cd hueglucose
python2.7 setup.py --local
```


## Usage

The very first time you run the script you must remember to press the big button on your philips hue bridge to authenticate. This is only needed the first time.

Printing all current lights and their colors (in tuple form)
Assuming "192.168.1.213" is your hue bridge
```bash
python2.7 -m hueglucose.getlightcolors "192.168.1.213"
```
Setting the light "dialys1" based on glucose retrieved from your nightscout installation running on "https://mysite.herokuapp.com":
```bash
python -m hueglucose.hueglucose "192.168.1.213" "dialys1" "https://mysite.herokuapp.com"
```


## Running it periodically
I recommend running the script once a minute in a cron job.
On linux, type ```crontab -e```and add the following code
```bash
* * * * *  python -m hueglucose.hueglucose "192.168.1.213" "dialys1" "https://mysite.herokuapp.com" 2>&1 1> /tmp/hueglucose.log
```
Remember to replace the path to the script with your own. Any errors can be found by inspecting /tmp/hueglucose.log
