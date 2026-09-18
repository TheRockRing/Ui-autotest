from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://dev-agent.homecredit.kz/#/flushbarRoute")


time.sleep(5)

wait = WebDriverWait(driver, 30)

element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Ваш ИИН']"))
)
element.send_keys("011212551163")


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()


wait = WebDriverWait(driver, 30)
password_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Ваш пароль']"))
)
password_input.send_keys("QWEasd@123")


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ВОЙТИ']"))
)
button.click()


wait = WebDriverWait(driver, 30)
branch = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[text()='mcrBranch_Алматы_ТД Дана 051076']"
    ))
)
driver.execute_script("arguments[0].click();", branch)
time.sleep(5)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='group']//flt-semantics[@role='button'][last()]"
    ))
)
driver.execute_script("arguments[0].click();", element)


wait = WebDriverWait(driver, 30)
branch = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[text()='mcrBranch_Алматы_Молл Апорт 052514']"
    ))
)
driver.execute_script("arguments[0].click();", branch)
