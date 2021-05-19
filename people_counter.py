from hammiu import CentroidTracker, TrackableObject
from imutils.video import VideoStream, FPS
import numpy as np
import argparse
import time
import imutils
import cv2
import dlib 

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,	help="path to Caffe pre-trained model")
ap.add_argument("-i", "--input", type=str, help="path to optional input video file")
ap.add_argument("-o", "--output", type=str, help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.4, help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=30, help="# of skip frames between detections")    # sau 30 frame thì chạy là detection
args = vars(ap.parse_args())

# khởi tạo list of classes mà MobileNet SSD đã được trained 
# chú ý mình chỉ quan tâm đến 'person' thôi
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

# load our detection model
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# nếu video ko truyền vào thì mở wwebcam
if not args.get("input", False):
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()     # thực ra có thể vs = VideoCapture(0) là ok
	time.sleep(2.0)
# nếu ko mở video được truyền vào
else:
	print("[INFO] opening video file...")
	vs = cv2.VideoCapture(args["input"])

# khởi tạo bộ ghi lại video
writer = None

