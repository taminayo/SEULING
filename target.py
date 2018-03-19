import pandas as pd

class Target(object):
    def __init__(self):
        self.fileName = input("확장자를 제외한 파일명을 입력하시오.\n")
        self.column = input("엑셀파일의 열 이름을 입력하시오.\n")
        self.nums = pd.read_excel("./"+self.fileName+".xlsx")[self.column].values.tolist()
