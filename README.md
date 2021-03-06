## 개요
yolo와 django를 사용하는 형태의 이미지 분석 api 입니다.

## 설치
* 기본적으로 필요한 패키지는 cuda(gpu를 사용한다면), opencv, yolo, django 입니다.

* 다음 두 가지 방법중 하나로 패키지를 설치하면 됩니다.
1. pip install -r requirements.txt (단, 불필요한 패키지도 많이 포함되어 있습니다.)
2. manage.py 를 실행시켜 (명령어: python manage.py runserver) 필요하다고 나오는 사항들을 설치합니다.

## weights 추가
* 용량초과로 github에 weights파일을 같이 올리지 못했습니다. 직접 파일을 다운받아서 bin폴더에 넣어주면 됩니다.

* 다음 두 가지 방법중 하나로 weights파일을 다운받으면 됩니다.
1. 공식 홈페이지(https://pjreddie.com/darknet/yolo/) 에서 YOLOv2 608x608를 다운받은 후 이름을 yolo.weights로 변경합니다.
2. 명령창에서 다운받는 방법 : 
> curl -o yolo.weights https://pjreddie.com/media/files/yolov2.weights

## 실행 방법 
> python manage.py runserver 0.0.0.0:8000
* 0.0.0.0으로 실행하면 외부에서도 서버에 접속할 수 있습니다.
* 8000이외의 포트를 뚫어 사용해도 무관합니다.

## 결과 
* [{"label":ㅁㅁ,"confidence":0.00},...]형태의 json 값을 반환합니다.
* 전송한 이미지 파일은 photos폴더에 저장됩니다.

## yolo 출처 
* https://pjreddie.com/darknet/yolo/

## 기타 사항들
* yolo의 기본설치는 https://www.youtube.com/watch?v=PyjBd7IDYZs 를 참고했습니다.
* yolo와 django를 합치는 과정에서 인자로 입력해야 하는 값들을 defaults.py파일에 기본값으로 넣었습니다.
* polls/views.py에서 POST방식으로 받은 파일을 yolo로 실행하고 그 결과값을return하는 구조입니다.
* cli.py에서 저장된 이미지를 im 변수로 받고 해당 변수를 return_predict()를 통해 분석합니다.
* darkflow/net/flow.py의 return_predict()에서 label이 Person이고 confidence가 50%이상인 값들만 넘기도록 설정했습니다.
* 초기작업 내용 : https://github.com/qwerty1434/Django-Yolo
