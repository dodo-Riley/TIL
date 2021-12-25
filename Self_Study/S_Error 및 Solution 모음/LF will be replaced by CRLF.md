# LF will be replaced by CRLF

### 1. 상황

> 공부한 내용을 정리하고, `git add` 명령어 실행

### 2. 원인

> 운영체제에 따른 줄바꿈 방식 차이로 인해 발생

- 윈도우OS에서는 `CRLF(Carriage Return + Line Feed)`방식, 유닉스OS에서는 `LF(Line Feed)`방식을 사용하고 있는데, 두 방식이 혼용되었을때 발생하는 `whitespace error`이다.

### 3. 해결책

> 각 방식으로 자동으로 변환해주는 명령어 실행

```python
# global 설정 명령어
  git config --global core.autocrlf true

# local 설정 명령어
  git config core.autocrlf true
```

### 4. 출처 및 참고

- [https://velog.io/@yeoj1n/Git-warning-LF-will-be-replaced-by-CRLF-in](https://velog.io/@yeoj1n/Git-warning-LF-will-be-replaced-by-CRLF-in)
- https://blog.naver.com/PostView.naver?blogId=jsjs2424&logNo=222221145549&redirect=Dlog&widgetTypeCall=true&directAccess=false