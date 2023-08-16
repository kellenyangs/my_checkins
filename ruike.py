import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


def signin():
    # 设置Chrome浏览器选项
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 创建Chrome浏览器实例
    browser = webdriver.Chrome(options=options)

    # 登陆
    browser.implicitly_wait(
        20)  # 如果找不到元素，每隔半秒钟再去界面上查看一次， 直到找到该元素， 或者过了20秒最大时长。
    url = 'https://www.ruike1.com'  # 目标网站
    browser.get(url)
    print("登陆成功")
    sleep(5)

    username = os.environ.get('RUIKE_USERNAME')
    passwd = os.environ.get('RUIKE_PASSWORD')
    browser.find_element(
        by=By.XPATH, value='//*[@id="ls_username"]').send_keys(username)  # 输入框
    browser.find_element(by=By.XPATH,
                         value='//*[@id="ls_password"]').send_keys(passwd)
    browser.find_element(
        by=By.XPATH, value='//*[@class="fastlg_l"]/button').click()  # 点击登陆按钮

    # 进行签到
    sleep(5)
    browser.find_element(by=By.XPATH,
                         value='//*[@id="k_misign_topb"]/a').click()  # 点击签到

    # 停止爬虫
    browser.quit()


# 主函数
def main():
    # 执行签到
    print("\n--------------ruike begin--------------")
    signin()
    print("--------------ruike end--------------\n")


if __name__ == "__main__":
    main()
