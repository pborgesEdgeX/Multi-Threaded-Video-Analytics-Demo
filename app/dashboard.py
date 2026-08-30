#!/usr/bin/env python
from flask import Flask, render_template, Response
import datetime
import threading
import time
import cv2
#import imutils
import numpy as np
from datetime import datetime
import sys
from kafka import KafkaConsumer

topic_video_one = "video-1"
topic_video_two = "video-2"
topic_video_three = "video-3"
topic_video_four = "video-4"
topic_video_five = "video-5"
topic_video_six = "video-6"

consumer_one = KafkaConsumer(
    topic_video_one,
    bootstrap_servers=['localhost:9092'])

consumer_two = KafkaConsumer(
    topic_video_two,
    bootstrap_servers=['localhost:9092'])

consumer_three = KafkaConsumer(
    topic_video_three,
    bootstrap_servers=['localhost:9092'])

consumer_four = KafkaConsumer(
    topic_video_four,
    bootstrap_servers=['localhost:9092'])

consumer_five = KafkaConsumer(
    topic_video_five,
    bootstrap_servers=['localhost:9092'])

consumer_six = KafkaConsumer(
    topic_video_six,
    bootstrap_servers=['localhost:9092'])


############### OLD CODE ############
URL   = 'http://174.85.94.245:40/stream.mjpg'
URL_2 = 'http://192.168.55.64:8000/stream.mjpg'
URL_3 = 'http://192.168.55.126:8000/stream.mjpg'

class WebcamVideoStream:
    def __init__(self, url):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(url)
        (self.grabbed, self.frame) = self.stream.read()
        if self.frame is None:
            raise AssertionError("Video is not running")

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        threading.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(consumer):
    #vs = WebcamVideoStream(url=URL).start()
    #vs_two = WebcamVideoStream(url=URL_2).start()
    for msg in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + msg.value + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(consumer_one),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_two')
def video_feed_two():
    return Response(gen(consumer_two),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_three')
def video_feed_three():
    return Response(gen(consumer_three),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_four')
def video_feed_four():
    return Response(gen(consumer_four),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_five')
def video_feed_five():
    return Response(gen(consumer_five),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_six')
def video_feed_six():
    return Response(gen(consumer_six),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='localhost', port=5004, threaded=True)