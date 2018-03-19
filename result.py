import requests

class Result(object):
    def __init__(self, nums):
        self.nums = nums
        self.statusList = []
        self.pre = """<?xml version='1.0' encoding='utf-8'?>
        <map id='ATTABZAA001R08'><pubcUserNo/><mobYn>N</mobYn>
        <inqrTrgtClCd>1</inqrTrgtClCd>
        <txprDscmNo>"""
        self.post = """</txprDscmNo>
        <dongCode>05</dongCode>
        <psbSearch>Y</psbSearch>
        <map id='userReqInfoVO'/>
        </map>"""
        self.requestsUrl = 'https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId='

        for num in nums:
            self.xml = self.pre+str(num)+self.post
            self.headers = {'Content-Type': 'application/xml; charset=utf-8'}
            self.status = requests.post(self.requestsUrl, data=self.xml, headers=self.headers).text.split('trtCntn')[1][1:-2]
            self.statusList.append(self.status)
