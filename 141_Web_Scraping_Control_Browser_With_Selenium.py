# ---------------------------------------------------
# -- Web Scraping => Control Browser With Selenium --
# ---------------------------------------------------
# - Control Browser With Selenium For Automated Testing
# - Download File From The Internet
# - Subtitle Download And Add On Your Movies [ Many Modules ]
# - Get Quotes From Websites
# - Get Gold and Currencies Rate
# - Get News From Websites
# ------------------------------------------


# Code Elzero

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome(ChromeDriverManager().install())

# browser.get("https://elzero.org")

# browser.find_element_by_css_selector("#search").send_keys("Front-End Developer")

# browser.find_element_by_css_selector(".search-submit").click() 

# browser.find_element_by_css_selector(".results-container .b-white:first-of-type a").click()

# views_count = browser.find_element_by_css_selector(".z-artical-info .z-info:last-of-type span:last-of-type")
# print(views_count.get_attribute("innerHTML"))




# Code Cloude Becouse Elzero not Working

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://elzero.org")

# استنى لحد ما العنصر يظهر فعليًا (بدل الاعتماد على الحظ)
search_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
)
search_field.send_keys("Front-End Developer")

browser.find_element(By.CSS_SELECTOR, ".search-submit").click()

# استنى صفحة نتائج البحث تحمّل قبل ما تدور على أول نتيجة
first_result = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".results-container .b-white:nth-of-type(3) a"))
)
first_result.click()

browser.implicitly_wait(10)  # استنى لحد ما الصفحة تتحمّل

views_count = browser.find_element(By.CSS_SELECTOR, ".z-artical-info .z-info:last-of-type span:last-of-type")
print(views_count.get_attribute("innerHTML"))

input("اضغط Enter عشان تقفل البروزير...")  # يخلي البروزير مفتوح لحد ما تدوس Enter
browser.quit()

# الكورس بتاع الزيرو استخدم حاجات قديمه شويه و علشان اشغله استخدمن 
# cloude
#  بس الاستفاده لازم تبقي عارف انت داخل ع انهي موقع
#  علشان تعرف تجيب منه الي انت عايزه و لازم تخلي بالك وانت بتجيب العنصر
#  و تكتبه صح و تبقي تكتب الداله بتاعه الوقت
#  علشان يستني ميحملش ع طول ويطلع خطاء
