# hydroHome2
## The purpose of this code is to run the hydroponics lab in the Makerspace
## Running The Pumps
If you want to run the pumps without going through the webpage you have a few options:
* The first option is to type `sudo python3 pumpthing.py` to run the pumps for any chosen amount of time every 24 hours. In order to do this you need to go into the code and change the `pumptime=10` variable to how long you would like it to run in seconds. The program will then run the pump for the amount of time that you said, wait 24 hours, and repeat until you stop it.
* Another option available is to start the program in the command line but this time you can have it run through the 24-hour wait before it runs the pump for the first time. `sudo python3 pumpthing.py -p off`
