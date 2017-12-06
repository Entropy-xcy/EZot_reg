from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DEBUG = False


def get_course_status(id):
    if DEBUG:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.PhantomJS()

    id = str(id)
    get_course_page(driver, id)
    status = get_status(driver)
    driver.close()
    return status


def get_status(driver):

    status_div = driver.find_element_by_xpath(
        "//div[@class='course-list']/table/tbody/tr[last()-1]/td[17]")
    status_text = status_div.text
    return status_text


def get_course_page(driver, id):
    driver.get("https://www.reg.uci.edu/perl/WebSoc")
    assert "Schedule of Classes" in driver.title
    # print(driver.page_source)
    elem_course_num = driver.find_element_by_name("CourseCodes")
    elem_course_num.clear()
    elem_course_num.send_keys(id)
    elem_course_num.send_keys(Keys.RETURN)


def main():
    print(get_course_status(47365))


if __name__ == "__main__":
    main()
