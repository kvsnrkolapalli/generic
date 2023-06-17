
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
import pandas as pd
import _thread



browse_params=False

class Generic:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-dev-shm-usage')
        self.service = Service(driver)
        if browse_params:
            self.browser=webdriver.Chrome()
            # self.browser = webdriver.Chrome(service=self.service)
        else:
            # chromedriver_path = '/usr/bin/chromedriver'
            # self.browser=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
            # self.browser=webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
            # self.browser=webdriver.Chrome(executable_path='C:/Users/HAMZA/Downloads/chromedriver_win32/chromedriver.exe', options=options)
            self.browser= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.browser.maximize_window()

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()
        
    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        
browser=Generic('./chrome_driver')
browser.close_browser()
        
Jan_columns=['Generic (Salt) Combination', 'Pharma Company', 'Brand Label', 'Preparation Type', 'Single Dose', 'Composition', 'Pack Size', 'Price Unit', 'Price Pack', 'Why is this medicine prescribed', 'List of Substitute brands']
Jan_df=pd.DataFrame(columns=Jan_columns)

print('Individual')
not_list=[
    'https://www.genericdrugscan.com/',
    'https://www.genericdrugscan.com/generic',
    'https://www.genericdrugscan.com/brand',
    'https://www.genericdrugscan.com/brand-combination-generics/',
    'https://www.genericdrugscan.com/manufacturer',
    'https://www.genericdrugscan.com/medicine-by-condition',
    'https://www.genericdrugscan.com/disease',
    'https://www.genericdrugscan.com/drug-category',
    'https://www.genericdrugscan.com/hospitals-directory',
    'https://www.genericdrugscan.com/blood-banks',
    'https://www.genericdrugscan.com/jan-aushadhi',
    'https://www.genericdrugscan.com/jan-aushadhi-stores',
    'https://www.genericdrugscan.com/jan-aushadhi-price-comparison',
    'https://www.genericdrugscan.com/jan-aushadhi-therapeutic-group-price-comparison',
    'javascript:void(0);',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=A',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=B',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=C',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=D',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=E',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=F',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=G',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=H',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=I',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=J',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=K',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=L',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=M',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=N',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=O',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=P',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=Q',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=R',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=S',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=T',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=U',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=V',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=W',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=X',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=Y',
    'https://www.genericdrugscan.com/brand-combination-generics/?sort=Z',
    'https://www.genericdrugscan.com/privacy-policy',
    'https://www.genericdrugscan.com/disclaimer',
    'https://www.genericdrugscan.com/contact-us']

def pull(page):
    try:
        print(page)
        browser=Generic('./chrome_driver')
        browser.open_page(page)
        i=2
        global Jan_df
        salt_combination=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[1]/td[2]').text
        company=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[2]/td[2]').text
        brand_label=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[3]/td[2]').text
        preparation_type=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[4]/td[2]').text
        dose=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[5]/td[2]').text
        composition=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[6]/td[2]').text
        composition=composition.replace('\n',',')
        pack_size=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[7]/td[2]').text
        price_unit=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[8]/td[2]').text
        price_pack=browser.browser.find_element(by=By.XPATH,value='/html/body/div/div[3]/div[1]/table[1]/tbody/tr[9]/td[2]').text
        elem=browser.browser.find_element(by=By.TAG_NAME,value='body').text
        why=elem.split('Usage: Why is this medication prescribed?')[1].split(brand_label+' Drug Brands Substitutes')[0].replace('\n',' ')
        elems = browser.browser.find_elements(By.XPATH,"//a[@href]")
        list_of_sub=''
        for elem in elems:
            link=elem.get_attribute("href")
            if link not in not_list:
                if '&page' in link:
                    continue
                else:
                    if '(' in elem.text:
                        list_of_sub=list_of_sub+str(elem.text)+','
        list_of_sub=list_of_sub[:-1]
        list=[salt_combination,company,brand_label,preparation_type,dose,composition,pack_size,price_unit,price_pack,why,list_of_sub]
        new_row_df = pd.DataFrame([list], columns=Jan_df.columns)
        Jan_df = Jan_df.append(new_row_df, ignore_index=True)
        Jan_df.to_csv('brand.csv',index = False)
        browser.browser.close()
        status_list.pop(0)
        print('Total Success : ',page)
    except:
        print('Total Failed : ',page)
        browser.browser.close()
        status_list.pop(0)

status_list=['']
no_bro=20
# max=794

link_df=pd.read_csv('s.csv')
links=link_df.values.tolist()
list_rem=[i[0] for i in links]
print(len(list_rem))

while(len(status_list)!=0):
    if len(list_rem)>0:
        if len(status_list)<=no_bro:
            print(len(status_list))
            _thread.start_new_thread(pull,(list_rem[0],))
            status_list.append(list_rem[0])
            list_rem.pop(0)
