from util import *

username = sys.argv[1]  # 登录账号
password = sys.argv[2]  # 登录密码
img_path = os.getcwd() + "/1.png"

def ruikeai():
    try:
        driver = get_web_driver()
        driver.get("https://www.ruike1.com/")

        driver.find_element_by_xpath("//*[@id='ls_username']").send_keys(
            username)
        driver.find_element_by_xpath("//*[@id='ls_password']").send_keys(
            username)
        driver.find_element_by_xpath("//*[@class='fastlg_l']/button").click()

        WebDriverWait(driver, 10, 0.5)
        print(driver.find_element_by_xpath("//*[@class='vwmy']").text())

        print(driver.find_element_by_xpath("//*[@id='k_misign_topb']").text())

        print(driver.find_element_by_xpath("//*[@class='vwmy']/a").text())

        driver.find_element_by_xpath("//*[@id='k_misign_topb']/a").click()

        print('ruikeai签到成功')
    except:
        raise
    finally:
        driver.quit()


if __name__ == '__main__':
    ruikeai()
