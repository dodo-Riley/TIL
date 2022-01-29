# 6. Github

## [1] Github 시작하기

### (1) 회원 가입

> [https://github.com/](https://github.com/) 에 접속합니다.
> 

![1. Github 메인 페이지에 접속해서 Sign up을 클릭합니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/%EA%B7%B8%EB%A6%BC1.png)

1. Github 메인 페이지에 접속해서 Sign up을 클릭합니다.

![2. Username의 경우 앞으로 개발자 인생에서 계속 쓰일 이름이므로 신중해야 합니다!
**이메일은 반드시 git config 설정에서 작성했던 이메일을 기입합니다!**](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/%EA%B7%B8%EB%A6%BC2.png)

2. Username의 경우 앞으로 개발자 인생에서 계속 쓰일 이름이므로 신중해야 합니다!
**이메일은 반드시 git config 설정에서 작성했던 이메일을 기입합니다!**

![Untitled](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled.png)

![3. 작성한 이메일로 보내진 코드를 입력하여 인증 받습니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%201.png)

3. 작성한 이메일로 보내진 코드를 입력하여 인증 받습니다.

![4. 간단한 설문조사가 진행됩니다. 사용에 있어서 크게 중요하지 않기 때문에, 빠르게 넘깁니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%202.png)

4. 간단한 설문조사가 진행됩니다. 사용에 있어서 크게 중요하지 않기 때문에, 빠르게 넘깁니다.

![5. 위 화면이 나타나면 정상적으로 회원 가입이 완료 된 것입니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%203.png)

5. 위 화면이 나타나면 정상적으로 회원 가입이 완료 된 것입니다.

### (2) Github 설정 변경

![Untitled](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%204.png)

1. 오른쪽 상단 프로필을 클릭합니다.
2. `Settings` 를 클릭합니다.
3. 왼쪽 안내 바에서 `Repositories`를 선택합니다.
4. `Repository default branch`의 입력 창에서  `main`을 지우고 `master`로 작성합니다.
5. `Update`를 클릭합니다.

<aside>
💡 **main vs master**

위에서 설정한 것은 앞으로 Github에서 원격 저장소를 생성할 때 자동으로 생기는
기본 브랜치의 이름을 main이 아니라 master로 나오도록 지정한 것입니다.

2020년에 Black Lives Matter라고 하는 아프리카계 미국인을 향한 폭력과 제도적 인종주의에 반대하는 사회운동이 있었습니다. Github는 기본 브랜치 이름이었던 master가 주인과 노예 (master and slave)를 떠올리게 하는 것을 개선하기 위해 main 이라는 이름으로 기본 브랜치의 이름을 변경했습니다.

하지만 수업에서는 진행 상 편의를 위해서 master 브랜치를 사용하도록 하겠습니다.

</aside>

## [2] 원격 저장소 (Remote Repository)

> 여태 까지는 내 컴퓨터라는 한정된 공간에 있는 로컬 저장소에서만 버전 관리를 진행했습니다.
이제는 Github의 원격 저장소를 이용해 내 컴퓨터의 로컬 저장소를 다른 사람과 `공유`해봅시다.
Git의 주요 목적 중 하나인 `협업`을 위해 로컬 저장소와 원격 저장소의 연동 방법을 학습합니다.
> 

### (1) Github에서 원격 저장소 생성

![화면 오른쪽 상단 더하기(+) 버튼을 누르고 New repository를 클릭합니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/%EA%B7%B8%EB%A6%BC3.png)

화면 오른쪽 상단 더하기(+) 버튼을 누르고 New repository를 클릭합니다.

![저장소의 이름, 설명, 공개 여부를 선택하고 Create repository를 클릭합니다. (체크 박스는 건드리지 않습니다!)](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/%EA%B7%B8%EB%A6%BC4.png)

저장소의 이름, 설명, 공개 여부를 선택하고 Create repository를 클릭합니다. (체크 박스는 건드리지 않습니다!)

### (2) 로컬 저장소와 원격 저장소 연결

1. 원격 저장소가 잘 생성되었는지 확인 후, 저장소의 주소를 복사합니다.
    
    ![그림5.png](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/%EA%B7%B8%EB%A6%BC5.png)
    
2. 기존에 실습 때 만들었던 홈 디렉토리의 TIL 폴더로 가서 vscode를 엽니다.

1. git init을 통해 TIL 폴더를 로컬 저장소로 만들어줍니다.
    
    ```bash
    kyle@KYLE MINGW64 ~/TIL
    $ git init
    Initialized empty Git repository in C:/Users/kyle/TIL/.git/
    ```
    

1. **git remote**
    - 로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어
    1. **원격 저장소 등록**
        
        `git remote add <이름> <주소>` 형식으로 작성합니다.
        
        ```bash
        $ git remote add origin https://github.com/edukyle/TIL.git
        
        [풀이]
        git 명령어를 작성할건데, remote(원격 저장소)에 add(추가) 한다.
        origin이라는 이름으로 https://github.com/edukyle/TIL.git라는 주소의 원격 저장소를
        ```
        
    2. **원격 저장소 조회**
        
        `git remote -v` 로 작성합니다.
        
        ```bash
        $ git remote -v
        origin  https://github.com/edukyle/TIL.git (fetch)
        origin  https://github.com/edukyle/TIL.git (push)
        
        add를 이용해 추가했던 원격 저장소의 이름과 주소가 출력됩니다.
        ```
        
    3. **원격 저장소 연결 삭제**
        
        `git remote rm <이름>` 혹은 `git remote remove <이름>` 으로 작성합니다.
        
        > 로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체를 삭제하는 게 아닙니다.
        > 
        
        ```bash
        $ git remote rm origin
        $ git remote remove origin
        
        [풀이]
        git 명령어를 작성할건데, remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다.
        그 원격 저장소의 이름은 origin이다.
        ```
        

### (3) 원격 저장소에 업로드

- 실습 때 작성했던 TIL 파일을 Github 원격 저장소에 업로드 해보겠습니다.
- **정확히 말하면, 파일을 업로드하는 게 아니라 커밋을 업로드 하는 것입니다!**
- 따라서 먼저 로컬 저장소에서 커밋을 생성해야 원격 저장소에 업로드 할 수 있습니다.

1. **로컬 저장소에서 커밋 생성**
    
    ```bash
    # 현재 상태 확인
    
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            day1.md
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    
    ```bash
    $ git add day1.md
    ```
    
    ```bash
    $ git commit -m "Upload TIL Day1"
    [master (root-commit) f3d6d42] Upload TIL Day1
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 day1.md
    ```
    
    ```bash
    # 커밋 확인
    
    $ git log --oneline
    f3d6d42 (HEAD -> master) Upload TIL Day1
    ```
    

1. **git push**
    - 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어
    - `git push <저장소 이름> <브랜치 이름>` 형식으로 작성합니다.
    - `-u` 옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능합니다.
    
    ```bash
    $ git push origin master
    
    [풀이]
    git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
    
    ------------------------------------------------
    
    $ git push -u origin master
    이후에는 $ git push 라고만 작성해도 push가 됩니다.
    ```
    

1. **vscode 자격 증명**
    
    ![Sign in with your browser를 클릭합니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%205.png)
    
    Sign in with your browser를 클릭합니다.
    
    ![Authorize GitCredentialManager를 클릭합니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%206.png)
    
    Authorize GitCredentialManager를 클릭합니다.
    
    ![정상적으로 자격 증명이 완료 되었습니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%207.png)
    
    정상적으로 자격 증명이 완료 되었습니다.
    
    이후 git push 완료
    
    ```bash
    $ git push -u origin master
    info: please complete authentication in your browser...
    Enumerating objects: 3, done.
    Counting objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 218 bytes | 218.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    To https://github.com/edukyle/TIL.git
     * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
    ```
    
2. **원격 저장소에서 정상 업로드 확인**
    
    ![Untitled](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%208.png)
    

<aside>
❗ **(주의) Github 원격 저장소에 절대로 파일을 드래그해서 업로드 하지 않습니다!!!!**

가끔 Github를 구글 드라이브처럼 여겨서, 파일을 직접 드래그해서 올리는 경우가 있습니다.
Git 명령어를 학습했기 때문에, 반드시 git add → git commit → git push 의 단계로만
업로드 해야합니다.

그 이유는 로컬 저장소와 원격 저장소의 동기화 때문입니다.
로컬 저장소에서 변경이 먼저 일어나고, 그 변경 사항을 원격 저장소에 반영하는 형태여야 합니다. 하지만, Github에 드래그를 해서 파일을 업로드하면 원격 저장소에 변경이 먼저 일어나는 형태가 되기 때문에 이러한 행동을 지양해야 합니다.

</aside>

1. `git push`를 그림으로 이해하기

![로컬 저장소의 commit 이력이 원격 저장소에 그대로 반영됩니다.](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%209.png)

로컬 저장소의 commit 이력이 원격 저장소에 그대로 반영됩니다.

## [3] 실습

### (1) README.md 파일 push 해보기

- `README.md`는 원격 저장소의 소개와 설명이 담겨있는 일종의 대문 역할을 합니다.
- 반드시 파일 이름을 `README.md`로 지정해야 Github가 인식할 수 있습니다.
- 홈 디렉토리에 있는 TIL 폴더에 `README.md` 파일을 생성하고, 자유롭게 `설명, 각오, 분류 등`을 마크다운 문법으로 작성하고 자신의 Github TIL 원격 저장소에 push를 해봅니다.
- 예시
    
    ![[https://github.com/namjunemy/TIL](https://github.com/namjunemy/TIL)](6%20Github%2079f7beec9c7943828fbf9eff5ec5a72a/Untitled%2010.png)
    
    [https://github.com/namjunemy/TIL](https://github.com/namjunemy/TIL)