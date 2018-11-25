import sys,os,time,csv,getopt,cv2,argparse,numpy,io
# import numpy as numpy
import os
import subprocess
from datetime import datetime
from libpydetector import YoloDetector
from numpy.testing.decorators import setastest #new
from numpy.testing.nosetester import import_nose #new
from mvnc import mvncapi as mvnc
from skimage.transform import resize

from motor import *
#from Main import main
os.system('raspistill -w 640 -h 480 -v -o image.jpg')

roti_fata_all()
roti_stop()
roti_curba_dreapta()
roti_stop()
roti_curba_stanga()
roti_stop()

#os.system('python3 ./home/pi/YoloV2NCS/detectionExample/Main.py --image image.jpeg')

#subprocess.Popen(["python3","/home/pi/YoloV2NCS/detectionExample/Main.py","--image","image.jpg"])

#os.system('sudo Main.py --image image.jpg')
os.system("python3 ./Main.py --image image.jpg")
#main("--image", "image.jpg")

