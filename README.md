# AppleHealth2GoogleFit

Want to move to Android from iOS but don't want to loose your Apple Health data? 
This is a simple script to move data from Apple Health to Google Fit. 

Currently migrating:
- Steps 
- Distance 
- Weight

## Installation

### Install dependencies:
`sudo pip install -r requirements.txt`  

### Get Apple Health Data
You need to to export your Apple Health data in XML format. Here are some clues on how to do that:

<a href=""><img src="https://raw.githubusercontent.com/naspersclassifieds-shared/interviews/master/process.png?token=AHa0sdWPazQShmxQ5lmRS3Zu2s2EjhtXks5ZXke1wA%3D%3D" align="center" width="500" ></a>

![](https://raw.githubusercontent.com/hermanmaritz/AppleHealth2GoogleFit/master/screenshots/export_apple_health_data1.jpg)  |  ![](https://raw.githubusercontent.com/hermanmaritz/AppleHealth2GoogleFit/master/screenshots/export_apple_health_data2.jpg)

### Get Access to Google Fitness API
Now for the difficult part. Getting a Google Access Token. 

Easiest Way:
1. Got to https://developers.google.com/oauthplayground/
2. Scroll down and select Fitness v1
3. Select and Authonrize:
- https://www.googleapis.com/auth/fitness.activity.write (for steps)
- https://www.googleapis.com/auth/fitness.body.write (for weight)
- https://www.googleapis.com/auth/fitness.location.write (for distance)
4. Click on *Exchange auth code for token* 
5. Rename `config.py.example` to `config.py` and add the access token.

For more details: https://developers.google.com/fit/rest/v1/get-started

## Running

`python main.py /path/to/export.xml`

It takes about 10 minutes for data to show on Google Fit.
![](https://raw.githubusercontent.com/hermanmaritz/AppleHealth2GoogleFit/master/screenshots/export_apple_health_data3.jpg)  |


