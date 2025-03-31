import requests
from bs4 import BeautifulSoup
import os
import re
import argparse
#########################################################################
#############“在url = 后输入检索目录网址，要加单引号”#############
def parse_arguments():
    parser = argparse.ArgumentParser(description='Web scraping script with URL and file directory parameters.')
    parser.add_argument('--url', required=True, help='URL for web scraping')
    parser.add_argument('--output', required=True, help='Directory to save output files')
    return parser.parse_args()


args = parse_arguments()
url = args.url


def check_folder_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
check_folder_exists(args.output)


phylumfile_directory = os.path.join(args.output, 'phylumlinkfile.txt')
classfile_directory =  os.path.join(args.output, 'classlinkfile.txt')
orderfile_directory = os.path.join(args.output, 'orderlinkfile.txt')
familyfile_directory = os.path.join(args.output, 'familylinkfile.txt')
genusfile_directory = os.path.join(args.output, 'genuslinkfile.txt')
speciesfile_directory = os.path.join(args.output, 'specieslinkfile.txt')
result1_directory =os.path.join(args.output, 'result1.txt')
extraction_process1 = os.path.join(args.output, 'process1.txt')
extraction_process2 =os.path.join(args.output, 'process2.txt')
result2_directory = os.path.join(args.output, 'Species_Numbers.txt')

#########################################################################

cookies = {
    'lpsn_session': '5cpeddsi90m8rfrlj9cam84fbe',
    '_pk_ref.11.93af': '%5B%22%22%2C%22%22%2C1735354051%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D',
    '_pk_id.11.93af': '2aede04ae0ff7d8b.1735354051.',
    '_pk_ses.11.93af': '1',
    'modal_mailinglist_pageviews': '3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'lpsn_session=5cpeddsi90m8rfrlj9cam84fbe; _pk_ref.11.93af=%5B%22%22%2C%22%22%2C1735354051%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D; _pk_id.11.93af=2aede04ae0ff7d8b.1735354051.; _pk_ses.11.93af=1; modal_mailinglist_pageviews=3',
    'priority': 'u=0, i',
    'referer': 'https://lpsn.dsmz.de/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


def get_links(url0, rank, write_file):
    inlink = url0.split('	')
    resp = requests.get(inlink[0], headers=headers, cookies=cookies)
    resp.encoding = resp.apparent_encoding    
    soup = BeautifulSoup(resp.text,'html.parser')
    trs = soup.find_all('tr')
    print (f"Getting children taxon links from the {rank}:{inlink[0]}\n")
    a = open(write_file,'a',encoding='UTF-8')   ###########
    link_list = ''
    for tr in trs:
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

#########################################################################

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
    get_links(url, "class", orderfile_directory)    
elif 'order' in url:
    a = open(familyfile_directory,'w',encoding='UTF-8')
    a.close()
    get_links(url, "order", familyfile_directory)    
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
        get_links(line, "class", orderfile_directory)
    m.close()
if sig > 3:
    a = open(familyfile_directory,'w',encoding='UTF-8')
    a.close()    
    m = open(orderfile_directory,'r')
    for line in m:    
        get_links(line, "order", familyfile_directory)    
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

