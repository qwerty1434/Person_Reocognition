from .defaults import argHandler #Import the default arguments
import os
from .net.build import TFNet

def cliHandler(args):
    FLAGS = argHandler()
    FLAGS.setDefaults()
    FLAGS.parseArgs(args)

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
#    return print(내용) print를 return 하는게 의미가 있을까? (어차피 print만 해도 결과값이 보이는데 굳이 return??)
# 파일경로를 쉽게 만들자(defaults의 경로를 가져오고 싶다)
# 신뢰도 얼마 이상인 것들만 뽑아내게 하자
# return 값들 중 하나라도 person이 있으면 True
# 여러 이미지 파일에 대해서는 어떻게 처리할건지 생각해보자
    import cv2
    im = '/home/qwerty1434/python_file/django/imageloader/polls/darkflow_master/sample_img/sample_computer.jpg'
    person_exist=False
    for i in range(len(tfnet.return_predict(cv2.imread(im)))):        
        if tfnet.return_predict(cv2.imread(im))[i]['confidence'] >0.5:
            if tfnet.return_predict(cv2.imread(im))[i]['label'] == "person":
                person_exist = True
            print(tfnet.return_predict(cv2.imread(im))[i]['label'],tfnet.return_predict(cv2.imread(im))[i]['confidence'],person_exist)
            
