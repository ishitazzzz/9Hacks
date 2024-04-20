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
it has an accuracy of 40-80%, gets better the farther away 

we use custom process injection malware for reverse_tcp shell

```
https://github.com/spirizeon/rootblast
```
after connecting, we use reverse_tcp shell to 
+ stop the webcam stream of our model
+ download an empty image and display it through browser to spoof existing stream. 
