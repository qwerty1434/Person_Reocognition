from .defaults import argHandler #Import the default arguments
import os
from .net.build import TFNet
import json

def cliHandler(image_name):
    FLAGS = argHandler()
    FLAGS.setDefaults()
    #FLAGS.parseArgs(args)

    # make sure all necessary dirs exist
    def _get_dir(dirs):
        for d in dirs:
            this = os.path.abspath(os.path.join(os.path.curdir, d))
            if not os.path.exists(this): os.makedirs(this)
    
    requiredDirectories = [FLAGS.imgdir, FLAGS.binary, FLAGS.backup, os.path.join(FLAGS.imgdir,'out')]
    if FLAGS.summary:
        requiredDirectories.append(FLAGS.summary)

    _get_dir(requiredDirectories)

    # fix FLAGS.load to appropriate type
    try: FLAGS.load = int(FLAGS.load)
    except: pass

    tfnet = TFNet(FLAGS)
    
    if FLAGS.demo:
        tfnet.camera()
        exit('Demo stopped, exit.')

    if FLAGS.train:
        print('Enter training ...'); tfnet.train()
        if not FLAGS.savepb: 
            exit('Training finished, exit.')

    if FLAGS.savepb:
        print('Rebuild a constant version ...')
        tfnet.savepb(); exit('Done')

#    tfnet.predict() #// 원본
    import cv2

    im = '/Django-Yolo/photos/'+str(image_name) #이미지가 저장된 폴더 위치 + POST형식으로 받은 이미지 이름

    result = {}
    for i in range(len(tfnet.return_predict(cv2.imread(im)))):        
        person_exist=False
        if tfnet.return_predict(cv2.imread(im))[i]['confidence'] >0.5: #신뢰도가 50%이상이면 결과로 반환해 준다
            if tfnet.return_predict(cv2.imread(im))[i]['label'] == "person": #사람인지 판단한다
                person_exist = True
            result.update({i:{'label':tfnet.return_predict(cv2.imread(im))[i]['label'],'confidence':str(tfnet.return_predict(cv2.imread(im))[i]['confidence']),'is_person':person_exist}})
            if person_exist == True: #사람이 있으면 알고리즘을 끝낸다
                break;
    result = json.dumps(result) #json형태로 반환
    #모든 데이터를 넘기는게 아니라 그냥 person유무만 넘겨줘도 될 거 같습니다
    return result
