# FaceRecognition-Attendance-Marking
FaceRecognition Attendance Marking System 

## Tech Stack
* Opencv2
* Microsoft Cognitive Services
* dlib
* SQLite 
* openpxyl

Uses Micosoft Cognitive Face API to recognizes faces in picture from cctv or clicked from mobile devices (source can varry) and marks the attendace of each student present in picture

FILE | DESC
----- | -----
Face-DataBase | Database 
dataset | (A dataset) contains dir with faces of each student
add_student.py | make dataset and entry in DB
create_person.py | generate personId from microsoft server
add_person_faces.py | generate faceIds for each face in dataset 
train.py | trains the model in microsoft server
get_status.py | show the current status 
spreadsheet.py | makes xls sheet named reports.xlsx
detect.py | detect faces in test picture and crops and put them in Cropped_faces directory
identify.py | identify each face and marks the attendance 

### How to run : 
refer to this ---> [youtube video](https://www.youtube.com/watch?v=FeNasBaXdhg)

Refrence : [This](https://github.com/malharsk27/Autoattendance-Cognitive)
