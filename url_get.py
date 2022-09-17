import requests
from bs4 import BeautifulSoup
import time
from func_timeout import func_set_timeout

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
}
@func_set_timeout(999999)
def WriteIn(con1):#写入函数
    f = open("文本.doc", mode="a", encoding="utf-8")
    f.write(con1)

def parse_single_html(html):#爬取链接
    soup=BeautifulSoup(html.text,'html.parser')
    datas=[]
    title_nodes=(#返回了一个列表
        soup
        .find("ul",class_="zxxx_list")
        .find_all("a")
    )
    for atitle in title_nodes:
        link = atitle["href"]
        datas.append(link)

    return datas

def download_all_htmls():
    htmls=[]
    for idx in range (41):
        if idx==0:
            url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd'
        else:
            url=f"http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_{idx+1}"

        print("craw html:",url)
        while 1:
            con=requests.get(url,headers=headers)
            con.encoding = 'utf-8'
            print(con)#获取并输出
            if con.status_code ==200:#爬取成功则跳出循环
                break
            time.sleep(0.5)#重爬间隔
        #texts=con.text
        #result=BeautifulSoup(texts,'lxml')
        #div2 = result.find('li')
        htmls= htmls+parse_single_html(con)
        #WriteIn(con.text)#写入函数

        print(parse_single_html(con))
        print(htmls)
        time.sleep(0.5)
    f = open("htmls.txt", "w")
    for ahtml in htmls:  # 将所得所有url导入txt文档中
        f.write('http://www.nhc.gov.cn')  #修改自f.write('http://www.nhc.gov.cn/')
        f.write(ahtml + '\n')
    f.close()
    return htmls

htmls=download_all_htmls()
