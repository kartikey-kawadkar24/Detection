# Detection

Almost all the detections use OpenCV because OpenCV uses multiple classifiers, each classifier has multiple stages and each stage has multiple features.
As there can be many features to detect a single object in an image, instead of applying one feature at a time, features are grouped together in different stages of classifier and each stage is applied one-by-one.
Initial stages have less features and the number of features increases as per the order of stages.
As openCV uses coco dataset in the backend developed by YOLO, to provide labels to the detected objects. Even the dataset in the backend has some features which classifier tries to match with the features in the image at each stage.
