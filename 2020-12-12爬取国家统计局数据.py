from selenium import webdriver

zhibiao = []

url = "https://data.stats.gov.cn/easyquery.htm?cn=A01"
browser = webdriver.Chrome(executable_path='./chromedriver.exe')

browser.get(url)

browser.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[3]/table/tbody')


for i in range(1,10):
    zhibiao_xpath = str('//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[')+str(i)+str(']/td[1]/text()')
    zhibiao_text = browser.find_element_by_xpath(zhibiao_xpath).text
    zhibiao.append(zhibiao_text)

print(zhibiao)