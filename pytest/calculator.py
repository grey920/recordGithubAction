from re import sub
'''
 파이썬 테스트 하는 법 ( pytest )

 [테스트코드 작성]
 1. 테스트파일 만들기 (~~~.py)

 2. 테스트 코드를 함수로 모듈화 한다.
    assert 사용


 [환경 준비]
 1. venv 설치
    python3 -m venv pytest-venv

 2. venv 구동 (for Mac OS)
    source pytest-venv/bin/activate

3. pytest 설치
    pip install pytest  

4. pytest 실행
    pytest [테스트파일.py]

    * -v 옵션 사용
    pytest -v [테스트파일.py]
    
'''


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# 테스트 코드 작성
def test_add_two_int():
    assert add(3, 5) == 8
    assert add(1, 1) == 2
    assert add(-52, 5) -47

def test_subtract_two_int():
    assert subtract(7, 5) == 2
    assert subtract(2, 1) == 1
    assert subtract(1, 99) == -98

def test_multiply_two_int():
    assert multiply(5, 7) == 35
    assert multiply(4, 3) == 12
    assert multiply(-6, 8) == -48

def test_divide_two_int():
    assert divide(5, 1) == 5
    assert divide(1024, 5) == 204.8
    assert divide(36, -3) == -12

