# car_parking_detection_webapp
A small computer vision project, using M-RCNN to detect the car parking slot, store the index into MongoDB and show the result through a Flask Web. This project is inspired by https://towardsdatascience.com/parking-spot-detection-using-mask-rcnn-cb2db74a0ff5
There are 3 main tasks in this project: Detecting car, Checking the parking slot status, and Web App.

1. Detecting car
 Detecting car is a popular task, so I used pre-trained model Mask_RCNN (https://github.com/matterport/Mask_RCNN)
2. Cheking the parking slot status
 - In order to check if the parking slot is parked or not. I created dictionaries, which contain parking slot's status, frame, id.
 - Localizing parking slot in the frame by set_regions.py. This file helps us to draw a bounding box in each parking slot and saves the bounding box as region.p file.
 - Calculating IOU between car's bounding boxes and parking slot's bounding boxes to check whether the parking slot is parked or not. If a car's bounding box overlaps a parking slot for 10 frames, the parking slot's status will be changed to be parked

<img width="856" alt="Screen Shot 2022-04-14 at 13 53 43" src="https://user-images.githubusercontent.com/50269219/163385699-b6ffc2ae-cd30-42ad-b296-6960a25aae17.png">


3. Web App
 I used Flask framework to create website.
