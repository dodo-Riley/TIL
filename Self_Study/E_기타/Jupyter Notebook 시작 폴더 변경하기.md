# Jupyter Notebook 시작 폴더 변경

### 1. 지정할 폴더 생성

### 2. config 파일 생성

- `Prompt` 실행
- 아래 명령어 입력
    
    ```powershell
    jupyter notebook --generate-config
    ```
    

### 3. 경로 변경

- 생성된 `jupyter_notebook_config`파일 메모장으로 열기
- `ctrl+f`로 `#c.NotebookApp.notebook_dir = ”` 검색
- 주석 처리 삭제(가장 앞에 `#` 제거)
- 원하는 경로 `=` 뒤에 입력(경로 입력 시 `\`는 `/`로 변경)

> 참고 : [https://ooyoung.tistory.com/7](https://ooyoung.tistory.com/7)
>