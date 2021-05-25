# hydroHome2
## The purpose of this code is to run the hydroponics lab in the Makerspace
## Running The Pumps
#### Running The Pumps Through `pumpthing.py`
* The first option is to type `sudo python3 pumpthing.py` to run the pumps for any chosen amount of time every 24 hours. In order to do this you need to go into the code and change the `pumptime=10` variable to how long you would like it to run in seconds. The program will then run the pump for the amount of time that you said, wait 24 hours, and repeat until you stop it.
* Another option available is to start the program in the command line but this time you can have it run through the 24-hour wait before it runs the pump for the first time. `sudo python3 pumpthing.py -p off` After it doesn't run for the first 24 hours it will start the loop and run the pump for your specified time every 24 hours.
#### Using The `pumpOn.py` Program
* This program can be used to run the pump one time for a specified period of time. The default time is 600 seconds so `sudo python3 pumpOn.py` will run the pump for ten minutes. To specify how long you would like it to pump water just do the command line parameter --pumptime and then the amount of time in seconds. An example of this is: `sudo python3 pumpOn.py --pumptime 30`
#### Turning Off the Pumps Using `pumpOff.py`
* Running the program `pumpOff.py` should instantly turn off all of the LEDs and the pumps. Run it like this: `sudo python3 pumpOff.py`
#### Bugs in the code
* There is an issue with the `except:` function in both `pumpOff.py` and `pumpOn.py` where the LEDs all turn bright white after a keyboard interrupt or a failure in the code. This doesn't affect the pumps as they will still turn off but it does look terrible.

# Raspberry Pi setup

## Install OS
 Create image on the SD card:
 (make image using Raspberry Pi Imager: https://www.raspberrypi.org/software/)

## Setup ssh, wifi, and usb connection
 Working in the /boot directory of the newly created SD Card:

### 1) File: ssh
[copy] or create empty file ***ssh*** on SD Card's boot directory
* Filename: *ssh*

### 2) File: wpa_supplicant.conf
[edit] or create file for wifi connection and copy to boot directory of Pi:
* File name: *wpa_supplicant.conf*
* Change: `networkName` and `yourPassword`

The file should look like:

*wpa_supplicant.conf*
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
 ssid="networkName"
 psk="yourPassword"
}
```

### 3) USB connection
[copy] over or update files on the SD Card for usb connection (https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget)

File: ***config.txt***:
* Add `dtoverlay=dwc2` as the last line.
 ```
dtoverlay=dwc2
```

File: ***cmdline.txt***:
* Insert:
``` modules-load=dwc2,g_ether``` after `rootwait`
* It should look something like: ( `rootwait modules-load=dwc2,g_ether`).

The SD Card should now be ready for the Pi.

# Set up Pi
Plug the SD Card into the Pi.

## Connect to Pi

Plug Pi into Laptop USB then once pi has booted up:

*Option 1: Windows*: Login with (putty: https://www.putty.org/):
* PuTTY Host/IP: raspberrypi.local
* Port: 22
* Username: pi
* Password: raspberry

*Option 2: Mac or Linux*: use Terminal app, which is built in, for the command line:
```console
ssh pi@raspberrypi.local
```

*NOTE: Troubleshooting*: you may have to remove the **~/.ssh/known_hosts** file if you find yourself logging in to the wrong pi or unable to connect.
```console
rm .ssh/known_hosts
```

## [Optional] Other ways to connect:
You can connect using the pi's IP address if you're logged into the pi, or using an IP address scanner (I've used *Fing* on my Android device).

### Find the local IP address (optional)
You may want to find the IP address of the pi to log in with instead of using pi@raspberrypi.local. When you are ssh'd into the pi. This is particularly useful if you have multiple pi's on the network. Run the command:
```console
ifconfig
```
There will be a section of the output labeled `wlan` that has a couple lines that look like this:
```bash
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.4.76  netmask 255.255.0.0  broadcast 192.168.255.255
```
In this case the IP address is 192.168.4.76 and you can log in using:
```console
ssh pi@192.168.4.76
```

## [Optional] Changing the hostname
This is makes it easier to connect, because you don't have to remember the ip address. You have to edit two files `/etc/hostname` and `/etc/hosts`.

Follow instructions: https://thepihut.com/blogs/raspberry-pi-tutorials/19668676-renaming-your-raspberry-pi-the-hostname

If I change the name of my pi to "***makerspace***" I can access it by logging in to ***pi@makerspace.local***

## update Pi
Once you're logged into the Pi update using the following commands:
 ```console
sudo apt-get update
sudo apt-get upgrade
```

### REBOOT pi
 ```console
sudo reboot
```


# How to run a server
What files you need to make:
* index.html
* ws-client.js
* server.py

Each one of these files has a purpose; the `index.html` is in charge of what is being displayed on your website interface. For this specific project you will be using this html file to create buttons and text boxes that will be used to control your hydroponics system. There will be a more in depth explanation on the code later on.

The `ws-client.js` is in charge of receiving messages sent from the html code and sending a request to the server. Your java script file is not responsible for the appearance on your website interface. There will be a more in depth explanation on the code later on.

The `server.py` file is in charge of receiving and completing requests. There will be a more in depth explanation on the code later on.

Each one of these files have to work together and complete tasks. If one step is unable to work properly, then nothing will work.

# How do the server files work together?
## Create buttons and text boxes in `html`
If you go into the `html` file you will see a list of lines that say `<input type=`. This is where you will find the buttons/ text boxes that are being displayed on the website. If you go onto the website (haki.local:8040) you will see that the first button is the "temp" button. If you go into the `html` file, line 28-19 creates this button.
        `<input type="button" name="temp" value="Temp" id="temp" >
        <span id="tempinfo">x</span>`
--- `<input type=` creates a blank button.
--- `value=Temp"` gives the blank button a name.
--- `id="temp"` gives the button a name so that your `ws-client.js` knows what the button is called.
--- `is="temp"` this gives the output value of the button a value ("x") when you haven't pressed the button yet.

 ## javascrpit
Go into the `ws-client.js` file and you will see a portion of the code that reads
        `$("#temp").click(function(){
            var msg = '{"what": "Temperature"}';
            ws.send(msg);`
As you can see, the first line reads `#temp`. This takes the name that you gave it in the `index.html` file and sends a message to the server once you click the button (`.click(function(){`) using the second line `var msg = '{"what": "Temperature"}';`.

## server  
The `server.py` file receives the message `if msg["what"] == "Temperature":`. And then prints "checking temperature "`print("checking temperature ")`
And then underneath the temperature code I print out "t"; which is the temperature value. 
