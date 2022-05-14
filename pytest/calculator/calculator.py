from re import sub
'''
파이썬 테스트 하는 법 ( pytest )

[테스트코드 모듈화]
1. 실제 로직과 테스트 폴더를 분리한다.
    [calculator] 
        |-------> __init__.py
        |-------> calculator.py
    [tests]
        |-------> __init.py
        |-------> test_calculator.py   

2. calculator.py에 있던 테스트코드들을 tests폴더 내 test_calculator.py로 옮긴다
    1) test_calculator.py 상단에 calculator의 메소드 임포트
        from calculator.calculator import add, subtract, multiply, divide
    2) calculator.py의 테스트 코드들을 잘라내서 test_calculator.py에 붙이기

3. 터미널에서 pytest 실행 (test라는 이름을 쓰면 pytest가 자동으로 인식)
    * -v 옵션으로 더 자세히 볼 수 있음.
        tests/test_calculator.py::test_add_two_int PASSED               [ 25%]
        tests/test_calculator.py::test_subtract_two_int PASSED          [ 50%]
        tests/test_calculator.py::test_multiply_two_int PASSED          [ 75%]
        tests/test_calculator.py::test_divide_two_int PASSED            [100%]


 [환경 준비]
 1. venv 설치
    python3 -m venv pytest-venv

 2. venv 구동 (for Mac OS)
    source pytest-venv/bin/activate

3. pytest 설치
    pip install pytest  

    
'''


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

