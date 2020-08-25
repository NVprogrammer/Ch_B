from bs4 import BeautifulSoup
from selenium import webdriver
import time
import PGNtoUCi

class Web:
    def __init__(self,lofin,password):
        self.login=lofin
        self.password=password
    def findBestMove(self,browser2,strMoves):
        try:
            browser2.find_element_by_xpath("/html/body/div[3]/div[6]/div[7]/ul/li[1]/input").click()
            time.sleep(0.5)
            browser2.find_element_by_xpath("/html/body/div[3]/div[9]/div/div/div[2]/textarea").clear()
            browser2.find_element_by_xpath("/html/body/div[3]/div[9]/div/div/div[2]/textarea").click()
            browser2.find_element_by_xpath("/html/body/div[3]/div[9]/div/div/div[2]/textarea").send_keys(strMoves)
            time.sleep(1)
            browser2.find_element_by_xpath("/html/body/div[3]/div[9]/div/div/div[3]/input[1]").click()
            time.sleep(2)
            requiredHtml2 = browser2.page_source
            soup2 = BeautifulSoup(requiredHtml2, 'html5lib')
            bestMoves = soup2.findAll("div",id="evalline")

            print(str(bestMoves[0].text))
        except Exception as e :
            print(e)


    def initialize(self):
        prev_str = ""
        chromedriver = 'D:/chromedriver80.exe'
        options = webdriver.ChromeOptions()
        # options2 = webdriver.ChromeOptions()
        # options2.add_argument('headless')  # для открытия headless-браузера
        browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
        # browser2 = webdriver.Chrome(executable_path=chromedriver, chrome_options=options2)
        # Переход на страницу входа
        browser.get('https://lichess.org')
        # # Поиск тегов по имени
        # email = browser.find_element_by_name('username')
        # password = browser.find_element_by_name('password')
        # login = browser.find_element_by_xpath("/html/body/div[1]/main/form/div[1]/button")
        # # # добавление учётных данных для входа
        # email.send_keys(self.login)
        # password.send_keys(self.password)
        # # # нажатие на кнопку отправки
        # login.click()
        # # После успешного входа в систему переходим на страницу «OpenBets»

        # Получение HTML-содержимого
        time.sleep(5)
        browser.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[1]/a[3]").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[5]/button[3]").click()
        # browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[3]").click()

        # browser2.get('https://www.365chess.com/analysis_board.php')
        while (True):
            requiredHtml = browser.page_source
            soup = BeautifulSoup(requiredHtml, 'html5lib')
            table = soup.findAll('div', class_="moves")
            strMoves = ""
            for i in table:
                current = i.findAll("m2")
                for j in current: strMoves += j.text + " "
            strMoves=strMoves.lstrip()

            print("bestMove",PGNtoUCi.getMove(PGNtoUCi.toUCI(strMoves)))