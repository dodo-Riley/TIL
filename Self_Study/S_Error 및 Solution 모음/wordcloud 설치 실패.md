# wordcloud 설치 실패

### 1. 상황

> `pip install wordcloud` 시 `error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)` 오류 발생
> 

### 2. 원인

> 현재 작업중인 컴퓨터의 `Visual C++`의 버전이 요구 사항보다 낮기 때문
> 

### 3. 해결책

- 최신 `VS community` 설치
- ‘개별 구성 요소’ 탭에서 검색에 '2015'를 입력하여 `MSVC v140 - VS 2015 C++ 빌드 도구(v14.00)` 선택 후 설치
- python 패키지 재설치

### 4. 오류 재발생 시 대처법

- 설치 후에도 설치가 진행되지 않고 `error : command 'C:\\Program Fiels (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\cl.exe' failed with exit code 2`가 발생할 수 있음
- [`https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud`](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)에서 직접 파일을 받고, `prompt`창을 열어 해당 파일이 설치된 폴더에서 `pip install wordcloud-1.8.1-cp39-cp39-win_amd64.whl`와 같이 직접 설치
    - 파일을 받을 때, 본인 컴퓨터의 파이썬 버전과 윈도우 비트 수를 확인해 맞는 파일을 설치해야함

### 5. 다른 해결책

- `anaconda powershell prompt` 에서 `conda install -c conda-forge wordcloud` 입력

### 6. 출처 및 참고

- https://ddbobd.tistory.com/10
- https://hcid-courses.github.io/TA/FAQ/python_wordcloud_troubleshoot.html