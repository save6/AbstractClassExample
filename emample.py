from abc import ABCMeta, abstractmethod

#抽象クラス
class TableCreator(metaclass=ABCMeta):
    #ここから・・・
    def __init__(self,list):
        self.__list = list
    #本当はDBから取ってくるとか
    def getList(self):
        return self.__list
    #・・・ここまでは共通化してしまいたい

    @abstractmethod
    def create(self):
        pass

class CsvTableCreator(TableCreator):
    def create(self):
        LIST = self.getList()
        HEADER = "名前, 得点\n"
        BODY= [l['name'] + "," + str(l['score']) for l in LIST]
        return HEADER + "\n".join(BODY)

class HtmlTableCreator(TableCreator):
    def create(self):
        LIST = self.getList()
        HEADER = "<table>\n<tr><th>名前</th><th>得点</th></tr>\n"
        FOOTER = '\n</table>'
        BODY= ["<tr><td>" + l['name'] + "</td><td>" + str(l['score']) + "</td></tr>" for l in LIST]
        return HEADER + "\n".join(BODY) + FOOTER

if __name__=='__main__':
    items = [{ 'name': '佐藤', 'score': 45 }, \
            { 'name': '小笠原', 'score': 67 },\
             { 'name': '田中', 'score': 89 }]

    #CSVで情報を出力できる
    print("\n-- CSVで出力します -----------------")
    print(CsvTableCreator(items).create())

    #HTMLのTableで情報を出力できる
    print("\n-- HTMLのテーブルでで出力します  -----------------")
    print(HtmlTableCreator(items).create())