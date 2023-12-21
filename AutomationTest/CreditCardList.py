from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# 設定解析度
mobile_emulation = {
    "deviceMetrics": {"width": 740, "height": 960, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

try:
    driver = webdriver.Chrome(options=chrome_options)

    logging.info("-----Navigate to Cathay bank page-------")
    # 訪問國泰世華官網
    driver.get("https://www.cathaybk.com.tw/cathaybk/")

    try:
        logging.info("-----Wait for Up left button-------")
        UpleftButton = WebDriverWait(driver, 10).until(
            # 等待左上角按鈕出現
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cubre-a-burger"))
        )

    except TimeoutException:
        logging.error("Timed out waiting for Upleft button to be visible.")

    logging.info("-----Up left button click-------")
    UpleftButton.click()

    try:
        logging.info("-----Wait for introduce list-------")
        Introduce = WebDriverWait(driver, 2).until(
            # 等待側邊選單出現
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "div.cubre-o-nav__content > div.cubre-o-nav__menu > div > div:nth-child(1)",
                )
            )
        )

    except TimeoutException:
        logging.error("Timed out waiting for Introduce list to be visible.")

    logging.info("-----Introduce list click-------")
    Introduce.click()

    try:
        logging.info("-----Wait for credit card button-------")
        CreditCard = WebDriverWait(Introduce, 2).until(
            # 等待信用卡項目出現
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.cubre-o-menu__content > div > div:nth-child(1)")
            )
        )
    except TimeoutException:
        logging.error("Timed out waiting for Credit card button to be visible.")

    logging.info("-----Credit card button click-------")
    CreditCard.click()

    try:
        logging.info("-----Wait for credit card intrduction-------")
        CreditCardList = WebDriverWait(CreditCard, 2).until(
            # 等待信用卡列表出現
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "a#lnk_Link.cubre-a-menuLink")
            )
        )

        if CreditCardList.is_displayed():
            logging.info("-----Print the item below credit card & screenshot------")
            ElementsInList = CreditCard.find_elements(
                By.CSS_SELECTOR, "a#lnk_Link.cubre-a-menuLink"
            )

            for index in range(0, len(ElementsInList)):
                print(f"{index+1} {ElementsInList[index].text}")

            print(f"信用卡選單下找到 {len(ElementsInList)} 個項目")
            driver.save_screenshot("cathay_credit_card.png")

    except TimeoutException:
        logging.error("Timed out waiting for Credit card list to be visible.")


finally:
    driver.quit()
    logging.info("WebDriver closed successfully.")
