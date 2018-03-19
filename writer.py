import pandas as pd

class Writer(object):
    def __init__(self, ncolumn, nums, status):
        self.nums = nums
        self.ncolumn = ncolumn
        self.status = status
        self.fileName = input('새로 생성할 파일명을 입력해주세요.\n')
        self.column = input('열 이름을 입력해주세요.\n')
        self.writer = pd.ExcelWriter(self.fileName+'.xlsx')
        pd.DataFrame({self.ncolumn: self.nums, self.column: self.status}).to_excel(self.writer, index=False)
        self.writer.save
