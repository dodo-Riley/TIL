# Mac 터미널 업그레이드

# <Git Init 후 Master 보이게 하기>

## 1. 터미널 열기

![Untitled](Mac%20%E1%84%90%E1%85%A5%E1%84%86%E1%85%B5%E1%84%82%E1%85%A5%E1%86%AF%20%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%80%E1%85%B3%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%83%E1%85%B3%20448f10dd49064ef7b1c280c39bcda536/Untitled.png)

## 2. **터미널에 명령어 입력하기**

![Untitled](Mac%20%E1%84%90%E1%85%A5%E1%84%86%E1%85%B5%E1%84%82%E1%85%A5%E1%86%AF%20%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%80%E1%85%B3%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%83%E1%85%B3%20448f10dd49064ef7b1c280c39bcda536/Untitled%201.png)

- 터미널에 아래 명령어를 입력합니다.

```bash
$ code ~/.zshrc
```

- 그러면 vscode 가 켜지고, .zshrc 파일이 열리게 됩니다.

## 3. vscode에 아래의 내용 복사-붙여넣기 하기

```bash
# Find and set branch name var if in git repository.
function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo '- ('$branch')'
  fi
}

# Enable substitution in the prompt.
setopt prompt_subst

# Config for prompt. PS1 synonym.
prompt='%2/ $(git_branch_name) > '
```

- 화면에서 이렇게 보이면 됩니다!

![Untitled](Mac%20%E1%84%90%E1%85%A5%E1%84%86%E1%85%B5%E1%84%82%E1%85%A5%E1%86%AF%20%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%80%E1%85%B3%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%83%E1%85%B3%20448f10dd49064ef7b1c280c39bcda536/Untitled%202.png)

## 4. 터미널 종료 후 재시작

- **열려있는 모든 터미널 (vs code 포함)을 종료하고 다시 시작합니다!**
- 모든 터미널을 종료하고 다시 실행합니다.

## 5. 결과 확인

- 바탕화면에 test 폴더를 하나 생성해 주세요.
    - cd 명령어를 통해 test 폴더 안으로 들어가게 되면 Desktop/test 경로를 확인하실 수 있습니다.
- `$ git init`을 해보면 master 표시가 잘 나타나는 것을 확인할 수 있습니다.
    
    ![Mac%20%E1%84%90%E1%85%A5%E1%84%86%E1%85%B5%E1%84%82%E1%85%A5%E1%86%AF%20%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%80%E1%85%B3%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%83%E1%85%B3%20448f10dd49064ef7b1c280c39bcda536/Screen_Shot_2021-07-06_at_8.40.52_AM.png](Mac%20%E1%84%90%E1%85%A5%E1%84%86%E1%85%B5%E1%84%82%E1%85%A5%E1%86%AF%20%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%80%E1%85%B3%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%83%E1%85%B3%20448f10dd49064ef7b1c280c39bcda536/Screen_Shot_2021-07-06_at_8.40.52_AM.png)