# Git 자주 하는 실수 모음

## [1] **자주 하는 실수 모음**

### (1) **submodule => git 속 git**

- 가끔 Github에 폴더에 화살표가 있을 때
    - => Git 저장소 내부에 Git 저장소가 있는 경우
- 솔루션 : submodule 형식으로 활용할 수는 있지만, 처음에는 복잡하게 가지말자!

### (2) **경로 공백 처리**

- `마크다운_문법.md`  공백을 _로 변환해서 사용하는걸 권장!

### (3) **약속**

- git 명령어는 항상 .git 폴더가 있는 곳에서 하자!
- git 저장소로 활용되는 폴더에 다른 git 저장소를 옮기지 말자!

### (4) **커밋 없는 경우**

- 커밋이 없어서 push할 수가 없음. 혹은 브랜치가 없다.
- remote 설정은 되어 있는 것을 확인할 수 있음.

### (5) Commit을 하나도 안하면 branch를 만들 때 에러가 발생해요!

컴퓨터로 git clone 명령어를 통해 clone해와서 branch를 생성하려고 하니 다음과 같은 오류를 얻었습니다.

```
$ git branch develop
```

```
fatal: Not a valid object name: 'master'.
```

**원인**

아직 commit을 한번도 하지 않은 repository이기 때문입니다.

**해결방법**

최소 1번이상 commit을 진행하면 됩니다.

### (6) git push가 안되는 경우

error: failed to push some refs...

원격 레포지토리를 처음 등록하고(`git remote add origin 깃허브주소` ) 

git push를 하면 에러가 납니다. github에 master 브랜치와 내 로컬의 master 브랜치가 연결되어 있지 않기 떄문입니다.

`git push -u origin master`해서 내 로컬의 master 브랜치와 github의 master 브랜치를 연결 시켜줘야 합니다.

하지만 만약에 해당 명령어가 에러가 난다면, 아마도 github에 기본 브랜치가 master 브랜치가 아니라 main 브랜치이기 때문입니다.

![Git%20%E1%84%8C%E1%85%A1%E1%84%8C%E1%85%AE%20%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%AE%20%E1%84%86%E1%85%A9%E1%84%8B%E1%85%B3%E1%86%B7%2079632319e5714e4193c9675fb9cc1d0c/Untitled.png](Git%20%E1%84%8C%E1%85%A1%E1%84%8C%E1%85%AE%20%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%AE%20%E1%84%86%E1%85%A9%E1%84%8B%E1%85%B3%E1%86%B7%2079632319e5714e4193c9675fb9cc1d0c/Untitled.png)

해결책은 github의 default branch를 변경하거나, `git push -f` 를 설정해주는 것입니다.

![Git%20%E1%84%8C%E1%85%A1%E1%84%8C%E1%85%AE%20%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%AE%20%E1%84%86%E1%85%A9%E1%84%8B%E1%85%B3%E1%86%B7%2079632319e5714e4193c9675fb9cc1d0c/Untitled%201.png](Git%20%E1%84%8C%E1%85%A1%E1%84%8C%E1%85%AE%20%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%AE%20%E1%84%86%E1%85%A9%E1%84%8B%E1%85%B3%E1%86%B7%2079632319e5714e4193c9675fb9cc1d0c/Untitled%201.png)

## [2] **가능? 불가능?**

### (1) **TIL 폴더명 바꿔도 되나요? .git 의 상위폴더! => O 바꿔도됨! 전혀 상관 없음**

- 폴더 이동도 자유롭게 해도 되지만, 항상 이동할 때 해당 폴더가 다른 git 저장소인지 체크는 할 필요가 있다!
- 프로젝트 폴더 이름이 바뀌는 것은 커밋과 상관이 없다.

### (**2) 원격저장소 이름이랑 로컬 폴더 이름은 같아야 할까요? => X**

원격 저장소 이름이랑 로컬 폴더 이름은 전혀 상관이 없습니다.

그러면 상관이 있는 것은 무엇일까요?

```
$ git remote -v # 원격 저장소 정보 조회
```

그리고 정보만 기록되어 있어서 `clone` `pull` `push` 등의 명령어를 입력할 때 활용되는 것이지, sync가 되어 있는 것은 아니다!