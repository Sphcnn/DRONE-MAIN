from email.mime import image
from unittest import result
from matplotlib import widgets
from ultralytics import YOLO
import numpy as np
import cv2
import cvzone
import math
from sort import*
from roboflow import Roboflow


model = YOLO("yolov8l.pt")
results=model("DRONE YOLO GÖRÜNTÜ.mp4", show = True)
cv2.waitKey(0)