from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from pathlib import Path

driver = webdriver.Chrome()
driver.get("https:/#/flushbarRoute")


time.sleep(5)

wait = WebDriverWait(driver, 30)

element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Ваш ИИН']"))
)
element.send_keys("777777777")


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()


wait = WebDriverWait(driver, 30)
password_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Ваш пароль']"))
)
password_input.send_keys("77777@123")


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ВОЙТИ']"))
)
button.click()


wait = WebDriverWait(driver, 30)
branch = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[text()='mcrBranch_Алматы_Молл Апорт 052514']"
    ))
)
driver.execute_script("arguments[0].click();", branch)


card_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//flt-semantics[contains(.,'Карта дебетная')]"
    ))
)
card_button.click()


menu = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//flt-semantics[@role='button' and contains(.,'Показать меню')]"
    ))
)
menu.click()


item = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//flt-semantics[@aria-label='Ввести вручную']"
    ))
)
driver.execute_script("arguments[0].click();", item)


WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//*[contains(.,'Вы уверены, что хотите ввести номер ИИН')]"
    ))
)

ok_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "(//flt-semantics[@role='button' and normalize-space(.)='OK'])[last()]"
    ))
)
driver.execute_script("arguments[0].click();", ok_button)


element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((
        By.CSS_SELECTOR,
        "input[aria-label='ИИН клиента']"
    ))
)

element.send_keys("777777777")


try:
    ok_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//flt-semantics[@role='button' and contains(.,'OK')]"
        ))
    )
    driver.execute_script("arguments[0].click();", ok_button)
except Exception:
    pass


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()
time.sleep(3)


field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input"))
)
field.send_keys("7777777766")


wait = WebDriverWait(driver, 30)
time.sleep(3)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()
time.sleep(5)

sms_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//input[contains(@aria-label,'SMS-код')]"
    ))
)
sms_input.send_keys("1111")
time.sleep(3)

wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()



wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()
time.sleep(5)

wait = WebDriverWait(driver, 10)


button_xpath = "//flt-semantics[@role='button' and contains(., 'Тлеуберген')]"
done_xpath = "//*[contains(., 'Поиск предложений завершен')]"

for i in range(20):
    try:
        # ждем кнопку
        button = wait.until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )

        # клик через JS (Flutter-safe)
        driver.execute_script("arguments[0].click();", button)
        print(f"Клик {i+1}")

        # проверяем появление текста завершения
        try:
            wait.until(
                EC.presence_of_element_located((By.XPATH, done_xpath))
            )
            print("✅ Поиск завершен → стоп")
            break
        except:
            pass

        time.sleep(5)

    except Exception as e:
        print("❌ Кнопка не найдена или изменилась")
        break


wait = WebDriverWait(driver, 20)

# Нажимаем круглую кнопку / меню
menu_button = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='button' "
        "and contains(@style, 'z-index: 6') "
        "and contains(@style, 'width: 56px') "
        "and contains(@style, 'height: 56px')]"
    ))
)

driver.execute_script("arguments[0].click();", menu_button)


# Нажимаем 'Результат сверки'
result_button = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='button' and normalize-space(.)='Результат сверки']"
    ))
)

driver.execute_script("arguments[0].click();", result_button)


# Выбираем 'Данные совпадают'
data_match_item = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//flt-semantics[@role='menuitem' and @aria-label='Данные совпадают']"
    ))
)

driver.execute_script("arguments[0].click();", data_match_item)


wait = WebDriverWait(driver, 30)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//flt-semantics[@role='button' and text()='ДАЛЕЕ']"))
)
button.click()


button = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '(//flt-semantics[@role="button" and contains(normalize-space(.), "Виртуальная карта 77777")])[1]'
    ))
)

button.click()

wait= time.sleep (15)

wait = WebDriverWait(driver, 10)
button = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "(//flt-semantics[@role='button' and not(normalize-space(.))])[last()]"
    ))
)
driver.execute_script("arguments[0].click();", button)


wait = WebDriverWait(driver, 30)


def upload_photo(row_xpath, file_name):
    photo_path = Path(__file__).resolve().parent / file_name

    row = wait.until(
        EC.presence_of_element_located((By.XPATH, row_xpath))
    )
    driver.execute_script("arguments[0].click();", row)

    file_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    file_input.send_keys(str(photo_path))
    print(f"Фото загружено: {photo_path}")


upload_photo(
    "//flt-semantics[contains(.,'Портрет')]",
    "Image.png"
)

upload_photo(
    "//flt-semantics[contains(.,'Удостоверение личности') and contains(.,'Лицевая сторона')]",
    "front.png"
)

upload_photo(
    "//flt-semantics[contains(.,'Удостоверение личности') and contains(.,'Обратная сторона')]",
    "back.png"
)

wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "(//flt-semantics[@role='button' and normalize-space(.)='ДАЛЕЕ'])[last()]"
    ))
).click()