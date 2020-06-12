import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from utils import label_map_util
from utils import visualization_utils as vis_util
import pyttsx3
import webbrowser
def speak(tell):
    engine = pyttsx3.init()
    engine.say(str(tell))    
    engine.runAndWait()
# # Model preparation 
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing `PATH_TO_CKPT` to point to a new .pb file.
# What model to download.
MODEL_NAME = 'ssd_inception_v2_coco_2018_01_28'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90


# ## Download Model

if not os.path.exists(MODEL_NAME + '/frozen_inference_graph.pb'):
	print ('Downloading the model')
	opener = urllib.request.URLopener()
	opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
	tar_file = tarfile.open(MODEL_FILE)
	for file in tar_file.getmembers():
	  file_name = os.path.basename(file.name)
	  if 'frozen_inference_graph.pb' in file_name:
	    tar_file.extract(file, os.getcwd())
	print ('Download complete')
else:
	print ('Model already exists')

# ## Load a (frozen) Tensorflow model into memory.

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')


# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

#intializing the IP Camera device

import cv2
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
   ret = 1
   while (ret):
      ipcam = cv2.VideoCapture("http:/192.168.0.100:8080/shot.jpg")
      check, frame=ipcam.read()
      image_np = frame 
      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
      image_np_expanded = np.expand_dims(image_np, axis=0)
      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
      # Each box represents a part of the image where a particular object was detected.
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
      # Each score represent how level of confidence for each of the objects.
      # Score is shown on the result image, together with the class label.
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0')
      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})
      
      vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          np.squeeze(boxes),
          np.squeeze(classes).astype(np.int32),
          np.squeeze(scores),
          category_index,
          use_normalized_coordinates=True,
          line_thickness=8)
      cv2.imshow('IP Camera Object Detection',cv2.resize(image_np,(1080,760)))
      key = cv2.waitKey(1)
      if key == ord('s'):
            path ="search_image"
            cv2.imwrite(os.path.join(path,'saved_img.jpg'), img=frame)
            ipcam.release()
            img_new = cv2.imread(os.path.join(path,'saved_img.jpg'), cv2.IMREAD_UNCHANGED)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            if os.path.exists("search_image/saved_img.jpg"):
                print("Image is Captured look at directory..")
                speak("Image is Captured look at directory..")
                print("Now your image start processing and prepare for search")
                speak("Now your image start processing and prepare for search")
                final_score = np.squeeze(scores)    
                count = 0
                for i in range(100):
                    if scores is None or final_score[i] > 0.5:
                            count = count + 1
                print('count',count)
                printcount =0;
                for i in classes[0]:
                      printcount = printcount+1
                      print(category_index[i]['name'])
                      data = category_index[i]['name']
                      print("Processing image data")
                      speak("Processing image data")
                      print("Process completed now searching on webbrowser")
                      speak("Process completed now searching on webbrowser")
                      urL='https://www.google.com/search?query='+data
                      urL1="https://en.wikipedia.org/wiki/"+data
                      chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                      webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
                      webbrowser.get('chrome').open_new_tab(urL)
                      webbrowser.get('chrome').open_new_tab(urL1)
                      break
            break
      if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          ipcam.release()
          break




