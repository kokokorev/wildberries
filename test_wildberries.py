from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_go_to_first_catalog_item():
    # открыть wildberris
    driver.get('https://www.wildberries.ru/')
    # нажать на кнопку открытия каталога
    driver.find_element(by=By.CLASS_NAME, value='nav-element__burger').click()
    # нажать на первый пункт каталога
    driver.find_element(by=By.CLASS_NAME, value='menu-burger__main-list-link').click()
    
    # отображается название католога
    # название каталога == 'Сделано в России!'
    assert driver.find_element(by=By.CLASS_NAME, value='catalog-title').text == 'Сделано в России!'


def test_empty_container_lable_text():
    # открыть wildberris
    driver.get('https://www.wildberries.ru/')
    # нажать кнопку 'Корзина'
    driver.find_elements(by=By.CLASS_NAME, value='navbar-pc__link')[2].click()
    
    # отображается интерфейс пустой Корзины
    assert driver.find_element(by=By.CLASS_NAME, value='basket-page__basket-empty').is_displayed()
    # отображается заголовок Корзины 'В корзине пока ничего нет'
    assert driver.find_element(by=By.XPATH, value="//div[@class='basket-page__basket-empty basket-empty']/h1").text == 'В корзине пока ничего нет'


def test_check_language_list():
    # открыть wildberris
    driver.get('https://www.wildberries.ru/')
    # навести курсор на кнопку смены языка
    hover = ActionChains(driver=driver).move_to_element(
        driver.find_element(by=By.CLASS_NAME, value='simple-menu__link--country')
    )
    hover.perform()
    
    # отображается список стран
    # количество элементов = 7
    assert len(driver.find_elements(by=By.CLASS_NAME, value='radio-with-text__country')) == 7


def test_add_item_in_basket():
    # открыть wildberris
    driver.get('https://www.wildberries.ru/')
    # нажать на кнопку открытия каталога
    driver.find_element(by=By.CLASS_NAME, value='nav-element__burger').click()
    # нажать на первый пункт каталога
    driver.find_element(by=By.CLASS_NAME, value='menu-burger__main-list-link').click()
    # кликнуть на первый товар
    driver.find_element(by=By.CLASS_NAME, value='product-card__img').click()
    # нажать на кнопку "Добавить в корзину"
    driver.find_element(by=By.CLASS_NAME, value='btn-main').click()
    # закрыть быстрый просмотр товара
    driver.find_element(by=By.CLASS_NAME, value='popup__close').click()
    # перейти в Корзину
    driver.find_elements(by=By.CLASS_NAME, value='navbar-pc__link')[2].click()
    
    # товар отображается в Корзине
    assert driver.find_element(by=By.CLASS_NAME, value='list-item__wrap').is_displayed()
    
    hover = ActionChains(driver=driver).move_to_element(
        driver.find_element(by=By.CLASS_NAME, value='list-item__wrap')
    )
    hover.perform()
    driver.find_element(by=By.CLASS_NAME, value='btn__del').click()


def test_teardown():
    driver.close()
    driver.quit()
