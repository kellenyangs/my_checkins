from util import *

username = sys.argv[1]  # 登录账号
password = sys.argv[2]  # 登录密码
img_path = os.getcwd() + "/1.png"

def cuiunai():
    try:
        driver = get_web_driver()
        driver.get("https://cuiun.cc")
        driver.find_element_by_xpath(
            "//*[@class='header-login-button']/button[1]").click()

        driver.find_element_by_xpath("//*[@id='login-box']//*[@name='username']").send_keys(
            username)
        driver.find_element_by_xpath(
            "//*[@id='login-box']//*[@name='password']").send_keys(password)
        driver.find_element_by_xpath(
            "//*[@id='login-box']//*[@class='login-bottom']").click()

        driver.find_element_by_xpath("//*[@class='b2font b2-coin-line']").click()
        print('cuiunai签到成功')
    except:
        raise
    finally:
        driver.quit()


if __name__ == '__main__':
    cuiunai()
