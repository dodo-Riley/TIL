# import와 from import

# 1. import (모듈명)

- 모듈 호출
    
    ```python
    import pandas
    import numpy
    ```
    

# 2. from (모듈명) import *

- 해당 모듈의 모든 것을 호출
    
    ```python
    from pandas import * 
    from numpy import *
    ```
    

# 3. from (모듈명) import (특정 함수, 변수, 클래스...)

- 해당 모듈에서 특정 부분만 호출
    
    ```python
    from pandas import Series
    from pandas import DataFrame
    ```
    

# 4. alias 지정

- as (축약명)을 같이 입력
    
    ```python
    import numpy as np
    import pandas as pd
    ```
    

# 5. import와 from import의 차이

- 모듈을 호출하지 않고 일부만 호출할 경우, 해당 함수명으로 사용
- 모듈을 호출했을 경우, `모듈명.함수명`으로 사용

```python
from math import factorial # math에서 factorial만 호출
math.factorial(3)          # factorial만 호출했으므로 에러
factorial(3)               # 정상적으로 6 반환
ceil(2.5)                  # ceil은 호출하지 않았으므로 에러
math.ceil(2.5)             # math를 호출하지 않았으므로 에러

import math                # math 호출
math.ceil(2.5)             # 정상적으로 3 반환

```

> 출처 및 참고
> 
- [https://coding-kindergarten.tistory.com/73](https://coding-kindergarten.tistory.com/73)
- [http://cloudrain21.com/python-difference-between-import-from-import](http://cloudrain21.com/python-difference-between-import-from-import)