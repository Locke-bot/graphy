import selenium, os, time, random, re, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/ZAINAB/Downloads/chromedriver.exe")
driver.get('https://www.swagbucks.com/surveys')
email_input = driver.find_element_by_css_selector("input[placeholder~=Email]")
password_input = driver.find_element_by_css_selector("input[placeholder~=Password]")
login_btn = driver.find_element_by_id('loginBtn')
email_input.clear()
password_input.clear()
# email_input.send_keys('tachyon9191@gmail.com')
email_input.send_keys('oladosumoses24@gmail.com')
# email_input.send_keys('terrificmoses867@gmail.com')
try:
    password_input.send_keys(os.environ['SWAG_PASSWORD'])
    # password_input.send_keys('LockeLamora')
    # password_input.send_keys('mistotle')
except KeyError:
    driver.close()
    raise
login_btn.click()
print('mo ti click log in o')
wait = WebDriverWait(driver, 10*60)
element = wait.until(EC.title_contains('Gold Surveys'))
ert = driver.execute_script('return document.getElementById("sbBalanceAmount").innerHTML')
try:
    print(f"I have {int(ert.strip().strip('SB'))/100} dollars")
except Exception as e:
    print(e)

def get_survey_question():
    return driver.execute_script('return document.getElementsByClassName("surveyQuestionText")[0].innerHTML')

prev_question = None
# case insensitive
none_matcher = re.compile(r'\bNone\b|\bOther\b|\bOthers\b|\bAll\b|\bNot Apply\b', re.I)
while True:
    while True:
        new_question = get_survey_question()
        print(new_question)
        print(prev_question)
        if new_question.strip().lower() == "You've answered all of the questions we have for now".lower():
            print(f"You now have {int(ert.strip().strip('SB'))/100} dollars, dunno if shit has been updated yet tho")
            driver.quit()
            sys.exit()
        if new_question != prev_question: # new question loaded
            prev_question = new_question
            break
        time.sleep(random.uniform(0.5, 1))
        
    choose_answer = driver.find_element_by_css_selector('.questionDropdownContainer')
    choose_answer.click()
    time.sleep(random.uniform(1, 1.5))
    options = driver.find_element_by_css_selector(".questionDropdownOptions")
    spans = options.find_elements_by_css_selector("span")
    print(len(spans), spans[0].text)
    multiple = driver.execute_script("return arguments[0].matches('span[onclick*=false]')", spans[0])
    print(multiple)
    if not multiple:
        try:
            chosen = random.choice(spans)
            print(chosen.text)
            driver.execute_script("arguments[0].click()", chosen)
        except Exception as e:
            print(f'fuck click error', e)
    else:
        options_number = random.randint(1, len(spans)) # how many options to be selected
        to_be_clicked = random.sample(spans, options_number) # select random option_numbers
        to_be_clicked_text = [i.text for i in to_be_clicked]
    
        for enum, i in enumerate(to_be_clicked_text):
            if none_matcher.findall(i):
                to_be_clicked = [to_be_clicked[enum]] # if options that can't be selected with others are met, select just them-case insensitively.
                break
        for i in to_be_clicked:
            print('trying to click')
            driver.execute_script("arguments[0].click();", i)
            
    time.sleep(random.uniform(0.5, 1))
    answer_btn = driver.find_element_by_css_selector("button[onclick]")
    driver.execute_script("arguments[0].click();", answer_btn)
    time.sleep(random.uniform(1, 2.5))
    # answer_btn.click()