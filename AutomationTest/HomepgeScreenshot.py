from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

    # 訪問國泰世華官網
    logging.info("-----Navigate to Cathay bank page-------")
    driver.get("https://www.cathaybk.com.tw/cathaybk/")

    try:
        logging.info("-----Wait for Login button-------")
        element = WebDriverWait(driver, 5).until(
            # 等待登入按鈕出現
            EC.presence_of_element_located((By.ID, "lblLoginText"))
        )

        # 執行截圖
        logging.info("-----Screen Shot Home-------")
        driver.save_screenshot("cathay_homepage.png")

    except TimeoutException:
        logging.error("Timed out waiting for Login button to be visible.")

finally:
    driver.quit()
    logging.info("WebDriver closed successfully.")
