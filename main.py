from selenium import webdriver
import time
import re
from  bs4 import BeautifulSoup
import socketio
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
url = "https://www.104.com.tw/jobs/main/"

driver1 = webdriver.Remote("http://kobe655218.ddns.net:4444/wd/hub"  , desired_capabilities = {'browserName': 'chrome'},
            options=options)



sio = socketio.Client()

def connent():
    sio.connect('http://kobe655218.ddns.net:9091',namespaces=["/crawl"])


def choose():
    driver1.get(url)
    time.sleep(1)
    # 數入關鍵字
    driver1.find_element_by_css_selector("input#ikeyword").send_keys("python")
    time.sleep(1)
    driver1.find_element_by_css_selector("div.input-group-append span").click()
    time.sleep(1)

    # 選擇位置
    location = driver1.find_elements_by_css_selector("div.second-floor-rect li.category-item.category-item--level-two")
    time.sleep(1)
    location[0].find_element_by_css_selector("span.category-picker-checkbox-input").click()
    location[1].find_element_by_css_selector("span.category-picker-checkbox-input").click()

    #
    driver1.find_element_by_css_selector("button.category-picker-btn-primary").click()
    driver1.find_element_by_css_selector("button.btn.btn-primary.js-formCheck").click()
    driver1.find_elements_by_css_selector("div.b-float-left ul li")[1].click()


def scroll():
    totalOffset = 0
    number = 0
    time.sleep(1)

    '''
    用正則表達式 抓取總共搜尋的頁數 
    我們就可以知道我們究竟要抓幾頁才是完整抓完
    '''
    total_page = driver1.find_elements_by_css_selector("label.b-select option")
    total_page = total_page[0].text
    total_page = re.match(r"第 [\d]+ / ([\d]+) 頁", total_page)
    total_Page = total_page.group(1)
    sio.emit('total_page', {"page": total_Page}, namespace='/crawl')
    print("總共頁數：" ,total_Page)
    driver1.find_element_by_css_selector("div.b-block.b-txt--center")

    # 執行下滑頁面 直到滑到指定的頁面
    count = 0
    while number < int(total_Page):
        totalOffset += 10000
        # 捲動的 js code
        js_scroll = '''(
            function (){{
                window.scrollTo({{
                    top:{}, 
                    behavior: 'smooth' 
                }});
            }})();
            '''.format(totalOffset)

        driver1.execute_script(js_scroll)
        # 抓取滑動過程中，會提示 “手動載入 第幾頁”，嘗試去點擊他，並從中知道滑取到第幾頁
        # 直到爬取到目標頁面
        try:
            button = driver1.find_elements_by_css_selector("button.b-btn.b-btn--link.js-more-page")
            page = button[-1].text
            page = re.match(r"手動載入 第([\d]+)頁", page)
            page = page.group(1)
            print(page)
            sio.emit('page', {"page": page}, namespace='/crawl')
            number = int(page)
            button[-1].click()
        except:
            print("not found")
            # sio.emit('page', {"page":"test"},namespace='/crawl')
        time.sleep(1)

data = []
def get():
    html = driver1.page_source
    soup = BeautifulSoup(html,"lxml")
    artic = soup.select("div#js-job-content article")

    for i in artic:
        title = i.select("h2 a")[0].text
        href = i.select("h2 a")[0]["href"]
        company = i.select("ul a")[0].text
        company_href = i.select("ul a")[0]["href"]
        locat = i.select("ul")[1].select("li")[0].text
        try:
            context = i.select("p")[0].text #有可能回沒有內文
        except:
            context = "none"
        data.append({"title":title.replace("\n","").strip() , "href":href.replace("\n","").replace("//","").strip(),"company":company.replace("\n","").strip(),"context":context.replace("\n","").strip()})

    #     print("title:",title.replace("\n","").strip())
    #     print("="*30)
    #     print("href:",href.replace("\n","").replace("//","").strip())
    #     print("=" * 30)
    #     print("company name:",company.replace("\n","").strip())
    #     print("=" * 30)
    #     print("company_href:",company_href.replace("\n","").replace("//","").strip())
    #     print("=" * 30)
    #     print("location:",locat.replace("\n","").strip())
    #     print("=" * 30)
    #     print("context:",context.replace("\n","").strip())
    #     print("=" * 30)
    # print("total :", len(data))
    driver1.quit()

    # with open("crawler.json",'w') as f :
    #     f.write(json.dumps(data))


if __name__ == "__main__":
    connent()
    choose()
    scroll()
    get()
