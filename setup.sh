#copy to /etc/init.d/NAME
#!/bin/bash
cd /home/pi/IoTCam
source ~/.profile
workon cv
cd IoTCam
python IoTCamera.py -c conf.json
