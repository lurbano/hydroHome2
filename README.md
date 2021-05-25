# hydroHome2
## The purpose of this code is to run the hydroponics lab in the Makerspace
## Running The Pumps
#### Running The Pumps Through `pumpthing.py`
* The first option is to type `sudo python3 pumpthing.py` to run the pumps for any chosen amount of time every 24 hours. In order to do this you need to go into the code and change the `pumptime=10` variable to how long you would like it to run in seconds. The program will then run the pump for the amount of time that you said, wait 24 hours, and repeat until you stop it.
* Another option available is to start the program in the command line but this time you can have it run through the 24-hour wait before it runs the pump for the first time. `sudo python3 pumpthing.py -p off` After it doesn't run for the first 24 hours it will start the loop and run the pump for your specified time every 24 hours.
#### Using The `pumpOn.py` Program
* This program can be used to run the pump one time for a specified period of time. The default time is 600 seconds so `sudo python3 pumpOn.py` will run the pump for ten minutes. To specify how long you would like it to pump water just do the command line parameter --pumptime and then the amount of time in seconds. An example of this is:

`sudo python3 pumpOn.py --pumptime 30`
