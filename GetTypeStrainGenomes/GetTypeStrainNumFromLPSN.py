import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import csv
import os
import re
from urllib.request import urlopen
import shutil

#########################################################################
#############“在url = 后输入检索目录网址，要加单引号”#############

url = 'https://lpsn.dsmz.de/genus/nocardioides'

#########################################################################

cookies = {
    '_pk_id.11.93af': 'e86410f72646f46f.1646968761.',
    'lpsn_session': 'npobi3hgoorpqkq9h2cra5k0fv',
    '_pk_ses.11.93af': '1',
}


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_pk_id.11.93af=e86410f72646f46f.1646968761.; lpsn_session=npobi3hgoorpqkq9h2cra5k0fv; _pk_ses.11.93af=1',
    'Referer': 'https://lpsn.dsmz.de/phylum/proteobacteria-1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Mobile Safari/537.36 Edg/100.0.1185.39',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

def get_links(url0, rank, write_file):
    inlink = url0.split('	')
    resp = requests.get(inlink[0], headers=headers, cookies=cookies)
    resp.encoding = resp.apparent_encoding    
    soup = BeautifulSoup(resp.text,'html.parser')
    trs = soup.find_all('tr')
    tds = soup.find_all('td')
    print (f"Getting children taxon links from the {rank}:{inlink[0]}\n")
    a = open(write_file,'a',encoding='UTF-8')   ###########
    link_list = ''
    for tr in trs:
        tds = tr.find_all('td')
        for td in tr:
            if  'correct name'in td or 'not validly published' in td or 'in need of a replacement' in td:
                statu=''
                if  'correct name'in td :
                    statu = 'correct name'
                if  'not validly published' in td:
                    statu = 'not validly published'
                if  'in need of a replacement' in td:
                    statu = 'in need of a replacement'
    
                t1 = tr.find_all('a')
                for t2 in t1:
                    t3 = t2.get('href')
                    parant = inlink[0].replace(f"https://lpsn.dsmz.de/{rank}/","")
                    taxa = f"	{inlink[1].strip()}:{parant.title()}	{statu}"
                    link_list='https://lpsn.dsmz.de'+t3+taxa
                    a.write(link_list+'\n')
    a.close()    

################“确认文件路径即可，无需手动创建文件”###################

phylumfile_directory = 'TEM/phylumlinkfile.txt'
classfile_directory = 'TEM/classlinkfile.txt'
orderfile_directory = 'TEM/orderlinkfile.txt'
familyfile_directory = 'TEM/familylinkfile.txt'
genusfile_directory = 'TEM/genuslinkfile.txt'
speciesfile_directory = 'TEM/specieslinkfile.txt'
result1_directory = 'TEM/result1.txt'
extraction_process1 = 'TEM/process1.txt'
extraction_process2 = 'TEM/process2.txt'
result2_directory = 'TEM/Species_Numbers.txt'


url1 = 'https://lpsn.dsmz.de/domain/bacteria'
url +="	"
if 'phylum' in url:
    sig =5
    a = open(classfile_directory,'w',encoding='UTF-8')
    a.close()
    get_links(url, "phylum", classfile_directory)
elif 'class' in url:
    sig =4
    a = open(orderfile_directory,'w',encoding='UTF-8')
    a.close()
    get_links(url, "clsaa", orderfile_directory)    
elif 'oder' in url:
    a = open(familyfile_directory,'w',encoding='UTF-8')
    a.close()
    get_links(url, "oder", familyfile_directory)    
    sig = 3
elif 'family' in url:
    a = open(genusfile_directory,'w',encoding='UTF-8')
    a.close()
    get_links(url, "family", genusfile_directory)  
    sig = 2
elif 'genus' in url:
    a = open(speciesfile_directory,'w',encoding='UTF-8')
    a.close()    
    get_links(url, "genus", speciesfile_directory)            
    sig =1

if sig > 4:

    a = open(orderfile_directory,'w',encoding='UTF-8')
    a.close()
    m = open(classfile_directory,'r')
    for line in m:
        get_links(line, "clsaa", orderfile_directory)
    m.close()
if sig > 3:
    a = open(familyfile_directory,'w',encoding='UTF-8')
    a.close()    
    m = open(orderfile_directory,'r')
    for line in m:    
        get_links(line, "oder", familyfile_directory)    
    m.close()
if sig > 2:
    a = open(genusfile_directory,'w',encoding='UTF-8')
    a.close()
    m = open(familyfile_directory,'r')    
    for line in m:    
        get_links(line, "family", genusfile_directory)    
    m.close()
if sig > 1:
    a = open(speciesfile_directory,'w',encoding='UTF-8')
    a.close()    
    m = open(genusfile_directory,'r')    
    for line in m:    
        get_links(line, "genus", speciesfile_directory)            
    m.close()    


test = open(speciesfile_directory,'r')
resl = open(result1_directory,'w',encoding='UTF-8')
p3_list = ''
for lis in test:
    splink = lis.split('	')
    resp3 = requests.get(splink[0].strip(),headers=headers,cookies=cookies)
    resp3.encoding = resp3.apparent_encoding
    print (f"Getting informations for species:{splink[0]}\n")
    obj1 = re.compile(r"<p>.*?<b>Type strain:</b>(?P<strain_name>.*?)</p>",re.S)
    result3 = obj1.finditer(resp3.text)
    for it in result3:
        strain_name = it.group('strain_name')
        p3_list = splink[0].strip(),strain_name.strip()
    resl.write(str(p3_list).strip()+'\n')
test.close()
resl.close()

##########“处理结果步骤文档,根据需求提取信息”############

a = open(result1_directory,'r',encoding='UTF-8')
b = open(extraction_process1,'w',encoding='UTF-8')
c = open(extraction_process2,'w',encoding='UTF-8')

for line in a:
    d = line.replace("(","").replace(")","").\
        replace("'","").replace("'","").\
        replace("<","\n").replace(">","\n")
    
    b.write(d)
a.close()
b.close()


n = open(extraction_process1,'r',encoding='UTF-8')
for m in n:
    if 'href=' not in m:
        c.write(m.replace("\n","").\
                replace("https://lpsn.dsmz.de/species/","\n").\
                replace("/a",""))

n.close()
c.close()

a = open(extraction_process2,'r',encoding='UTF-8')
b = open(result2_directory,'w',encoding='UTF-8')

for line in a:
    m = line[0].upper()+line[1:]
    b.write(m.replace('-',' ',1).replace(',','\t'))
    
a.close()
b.close()

os.remove(result1_directory)
os.remove(extraction_process1)
os.remove(extraction_process2)

