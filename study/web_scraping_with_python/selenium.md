## Keyword
`selenium`

## 셀리니움이란
 - 셀레니움은 웹 페이지를 테스트할 목적으로 생성된 기술이였다.
 - 그러나 code를 활용해서 정보를 수집하는 방식을 차단하는 웹 페이지들이 많아지면서 selenium으로 웹페이지를 브라우저를 통해 탐색해 나갔다.

 ## 실행방법
 1. [파이썬 가상환경을 세팅한다.](crawling.md)
 2.     pip install selenium
 3. 브라우저별로 selenium webdriver를 다운받아야 한다.  
    -[Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)  
    -[Firefox](https://github.com/mozilla/geckodriver/releases)  
    -[Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
    -[Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
4. Chrome을 기준으로 설명한다.  
자신이 사용하는 Chrome버전에 맞는 webdriver를 다운받는다.

5. 
```
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
```

6. 불러오기  
```ruby
PATH = 'your chromedriver path'
url = 'https://example.com'
driver = webdriver.Chrome(executable_path=PATH)
driver.get(url)
```

7. 브라우저 닫기
```
diver.close()
```  
<br/>

# Skill Up
1. ## 로딩 대기
    -브라우저에서 해당 웹 페이지의 요소들을 로드하는 데 시간이 좀 걸린다.   
    selenium은 해당 element가 존재하지 않으면 error를 반환한다.  
    이 error를 보기 싫다면 대기를 해줘야 한다.

    - Implicit Wailts(암묵적 대기)  
    
            driver.implicitly_wait(time_to_wait=5)
        찾으려는 element가 로드될 때까지 지정한 시간만큼 대기할 수 있도록 설정한다. 위 코드는 5초까지 기다려준다는 의미다.
    - Explicit Waits(명시적 대기)  
        위의 암묵적 대기는 효율이 별로다.
        ```ruby
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver = webdriver.Chrome('chromedriver')
        driver.get(url='https://www.google.com/')
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME , 'gLFyf'))
            )
        finally:
            driver.quit()
        ```

        selenium webdriver는 maximum 5초동안 기다린다.   
         expected_condition은 selenium webdriver를 500ms(0.5s)마다 호출한다.  
        클래스 이름이 gLFyf인 element를 찾는다면 True를 반환하고  
        아니라면 False를 반환한다.  
        클래스 이름 말고도 여러 조건들이 가능한데, 이 사이트를 참조하면 좋을 것 같다. 
        [조건](https://huddle.eurostarsoftwaretesting.com/how-to-selenium-expected-conditions/)


2. ## 요소 찾기
    - 원하는 element를 찾을 때, 어떤 요소를 찾을지 정해야 한다.  
    chrome을 켜서 `Ctrl + Shift + C` 를 누르고 원하는 요소를 클릭한다.  




## 문제점!!!
 크롤링이 무적인줄 알고 막 사용했다가 이번 [프로젝트](https://github.com/KPUCE2021SP/LiC.git)를 통해 시간이 오래걸린다는 것을 알게 되었다.

 selenium은 이미지같은 파일도 crawling하기 때문에 여러 데이터를 받아야 하는 상황에서는 적합하지 않음을 알게 되었다.
 그래서 scrapy를 공부한다!!!!
 [scrapy vs selenium](https://www.accordbox.com/blog/web-scraping-framework-review-scrapy-vs-selenium/)