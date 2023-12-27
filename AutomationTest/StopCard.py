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
# Set Resolution
mobile_emulation = {
    "deviceMetrics": {"width": 740, "height": 960, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

try:
    driver = webdriver.Chrome(options=chrome_options)

    logging.info("-----Navigate to Cathay United Bank Official Website-------")
    # 訪問國泰世華官網
    # Visit the Cathay United Bank Official Website
    driver.get("https://www.cathaybk.com.tw/cathaybk/")

    try:
        logging.info("-----Wait for Top Left Corner Button-------")
        UpleftButton = WebDriverWait(driver, 10).until(
            # 等待左上角按鈕出現
            # Wait for the Top Left Corner Button to Appear
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cubre-a-burger"))
        )

    except TimeoutException:
        logging.error("Timed out waiting for Top Left Corner Button to be visible.")

    logging.info("-----Top Left Corner Button click-------")
    UpleftButton.click()

    try:
        logging.info("-----Wait for the Sidebar Menu-------")
        Introduce = WebDriverWait(driver, 2).until(
            # 等待側邊選單出現
            # Wait for the Sidebar Menu to Appear
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "div.cubre-o-nav__content > div.cubre-o-nav__menu > div > div:nth-child(1)",
                )
            )
        )

    except TimeoutException:
        logging.error("Timed out waiting for the Sidebar Menu to be visible.")

    logging.info("-----The Sidebar Menu click-------")
    Introduce.click()

    try:
        logging.info("-----Wait for credit card button-------")
        CreditCard = WebDriverWait(Introduce, 2).until(
            # 等待信用卡項目出現
            # Wait for the Credit Card Section to Appear
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.cubre-o-menu__content > div > div:nth-child(1)")
            )
        )
    except TimeoutException:
        logging.error("Timed out waiting for Credit card button to be visible.")

    logging.info("-----Credit card button click-------")
    CreditCard.click()

    try:
        logging.info("-----Wait for the Card Introduction-------")
        CardIntrduction = WebDriverWait(CreditCard, 2).until(
            # 等待卡片介紹出現
            # Wait for the Card Introduction to Appear
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div > a:nth-of-type(1)")
            )
        )

    except TimeoutException:
        logging.error("Timed out waiting for the Card Introduction to be visible.")

    URL = CardIntrduction.get_attribute("href")
    logging.info(f"Navigate to {URL}")
    driver.get(URL)

    try:
        logging.info("-----Wait for the Discontinued Cards-------")
        StopCards = WebDriverWait(driver, 2).until(
            # 等待停發卡出現
            # Wait for the Discontinued Cards to Appear
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "a.cubre-m-anchor__btn.swiper-slide:last-child")
            )
        )

    except TimeoutException:
        logging.error("Timed out waiting for the Discontinued Cards to be visible.")

    logging.info("-----Discontinued Cards button click-------")
    StopCards.click()

    try:
        logging.info("-----Wait for the Discontinued Card page-------")
        StopCardsPage = WebDriverWait(driver, 3).until(
            # 等待停發卡列表出現
            # Wait for the Discontinued Card List to Appear
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "article.cubre-o-content > section:last-of-type > div.cubre-o-block__wrap > div.cubre-o-block__component  > div.cubre-o-slide.-cardList.swiper-container-initialized.swiper-container-horizontal",
                )
            )
        )

        if StopCardsPage.is_displayed():
            logging.info("-----Get Dot list loaction-------")
            # 定位 Dot List
            # Locate Dot List
            DotList = StopCardsPage.find_elements(
                By.CSS_SELECTOR, " span.swiper-pagination-bullet"
            )

            logging.info("-----Get Card titles loaction-------")
            # 定位 Card Title List
            # Locate Card Title List
            CardTitles = StopCardsPage.find_elements(
                By.CSS_SELECTOR, " div.cubre-m-compareCard__title"
            )

            logging.info("-----Print Card title & screenshot-------")
            count = 1
            for dot, cardtitle in zip(DotList, CardTitles):
                dot.click()
                WebDriverWait(StopCardsPage, 10).until(EC.visibility_of(cardtitle))

                if cardtitle.is_displayed():
                    print(f"{count} {cardtitle.text}")
                    driver.save_screenshot(f"Discontinued_card_{cardtitle.text}_{count}.png")
                    count = count + 1

            print(f"It has {count-1} Discontinued cards")

    except TimeoutException:
        logging.error("Timed out waiting for the Discontinued Card page to be visible.")


finally:
    driver.quit()
    logging.info("WebDriver closed successfully.")
