# 9HACKS
## Running the model 
Clone the repos
```
git clone https://github.com/ultralytics/yolov5
git clone https://github.com/ishitazzzz/9Hacks
```
move the custom detection files to the model's folder
```
mv 9Hacks/* yolov5/
```
run inference 
```
python3 detect.py --source <camera> --weights best.pt
```
the model has been trained on a dataset of human images
it has an accuracy of 40-80%, gets better the farther away you are

