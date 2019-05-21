
import requests

class Result:
    
    head = '''<?xml version='1.0' encoding='utf-8'?>
        <map id='ATTABZAA001R08'><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>'''
    tail = '''</txprDscmNo><dongCode>05</dongCode><psbSearch>Y</psbSearch>
        <map id='userReqInfoVO'/></map>'''
    url = 'https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId='
    headers = {'Content-Type': 'application/xml; charset=utf-8'}

    def __init__(self, num):
        self.num = num
        self.xml = '{}{}{}'.format(Result.head, num, Result.tail)
        self.status = ''
        
    def getStatus(self):

        if not self.num.isdigit() or not len(self.num) == 10:
            self.status = '잘못된 형식입니다.'
            return (self.num, self.status)
        try:
            self.status = requests.get(Result.url, data=self.xml, headers=Result.headers).text.split('trtCntn')[1][1:-2]
        except Exception as e:
            self.status = '{}'.format(e)
        finally:
            return (self.num, self.status)
