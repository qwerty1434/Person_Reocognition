# Django로 업로드 한 파일 Yolo로 인식하기


## 작동법
먼저 bin 폴더에 yolo.weights파일을 추가하셔야합니다 <br>
<pre><code>
python manage.py runserver
</code></pre>
## 작업하면서 기록해 둔 진행상황인데 나중에 다시 깔끔하게 정리해서 올리겠습니다.
1. defaults.py 에서 기본설정을 변경해 args를 안주고 바로 실행가능하도록 바꿈

2. return 값을 받기 위한 코드 해체 작업
 분류를 실행하고 이미지를 return해주는 코드가 어디있는지 찾아보자
flow파일 -> darkflow폴더에 있는 cli.py파일의 cliHandler(args) 안의 tfnet.predict() ->  net폴더에 있는 build.py파일의 (__init__ 내용이 먼저 실행되고 나서) + TFNet.predict -> net폴더에 있는 flow.py파일의 predict() -> predict 안의 feed_dict(인듯?) -> yolo폴더에 있는 predict.py 의 boxresults의 mess (postprocess의 imgcv,mess)
 결론 : cli.py의 tfnet.predict()를 tfnet.return_predict(이미지)로 바꿔준다 but return이 아직 안되는 중
파일경로를 쉽게 만들자(defaults의 경로를 가져오고 싶다)
신뢰도 얼마 이상인 것들만 뽑아내게 하고 return 값들 중 하나라도 person이 있으면 True로

미해결) 여러 이미지 파일에 대해서는 어떻게 처리할건지 생각해보자

3. django의 views.py에 yolo를 심는과정
 manage.py가 있는 위치에 yolo파일들을 옮겼다 (runserver하는 시점이 root위치가 되기 때문에 상대위치를 참조할려면 이렇게 해야하는거 같다)
 python manage.py -runserver 를 하면 sys.argv로 runserver가 넘어와서 yolo를 실행할때 error가 뜬다(지금 yolo는 python flow만 실행하면 되게끔 , 즉 sus.argv를 아무것도 받지 않아야 하는 상태이다)
-->views.py의 cliHandler(sys.agrsv)에서 sys.argv를 빼고
   cli.py의 cliHandler(args)에서 args를 빼고 FLAG.parseArgs(args)를 삭제했다

4. 디테일 과정
 viewsd의 최종 return 이 HttpResponse(cliHandler(image_name))으로 yolo결과값을 return 해 준다
 분석 파일은 photos폴더 경로 + views에서 넘겨주는 파일의 이름(request.FILES['photo'])이다
 json으로 넘기기 : 처음에 dict형식으로 껍질을 만들고 (result = {}) .update를 써서 dict 형식으로 다 담은 다음에 json.dumps()로 바꿔준다 (dump하면 에러나고 꼭 s붙여 dumps해야 함) 

미해결)  html에 진짜 이미지의 분석 결과 파일이 나올 순 없는건가? 그럴려면 tfnet.predict()도 써야하는건가
## 추가 작업 사항들
0. 서버에 심기
1. face verification 심기
2. 비디오 파일에 대해서 라벨 추출하기
3. 2가 성공하면 비디오를 스트리밍으로 바꾸기




## yolo 출처 
https://pjreddie.com/darknet/yolo/
