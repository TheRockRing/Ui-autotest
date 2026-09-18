from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://d")


time.sleep(10)

wait = WebDriverWait(driver, 30)

element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Ваш ИИН']"))
)
element.send_keys("77777777")


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()


wait = WebDriverWait(driver, 30)
password_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Ваш пароль']"))
)
password_input.send_keys("777777@123")


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ВОЙТИ']"))
)
button.click()

wait = WebDriverWait(driver, 30)
branch = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[text()='777777 052514']"
    ))
)
driver.execute_script("arguments[0].click();", branch)
time.sleep(3)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='button' and contains(., 'Открыть меню навигации')]"
    ))
)

driver.execute_script("arguments[0].click();", element)



new_request = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='button' and normalize-space()='Новая заявка']"
    ))
)
driver.execute_script("arguments[0].click();", new_request)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='button' and contains(., 'Открыть меню навигации')]"
    ))
)
driver.execute_script("arguments[0].click();", element)


clients = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='button' and normalize-space()='Мои клиенты']"
    ))
)

driver.execute_script("arguments[0].click();", clients)

time.sleep(10)
