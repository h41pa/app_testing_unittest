"""
Pentru autocomplete pentru metodele Webdriver in cadrul claselor in pages
trebuie sa te asigura ca instanta self.driver este de tip WebDriver , si nu este necesar sa configurezi fisier
pentru driver , doar folosing BDD  trebuie

from selenium.webdriver.remote.webdriver import WebDriver
si dupa initializeaza in clasa

class Name:

    def __init__(self, driver: WebDriver):
        self.driver = driver

####### pentru driver pentru a porni driver pentru teste  ######

~~ in teste poti inilitliza browser direct in clasa

(unittest.Tclass TestPaginaestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.pagina = PaginaMetode(self.driver)

    def tearDown(self):
        self.driver.quit()


~~ sau vrei sa folosesti driver.py separat :

driver.py - contine

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

## si il importi in pagina de test ##

from driver import Driver

class TestPagina(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.pagina = PaginaMetode(self.driver.driver)

    def tearDown(self):
    self.driver.close()

"""

"""
# pentru unittest rulare rapoarte

rulare test - python -m unittest tests/test_something.py

python -m unittest tests/test_something.py
- ruleaza din interfata din pycharm dupa rulare in stranga jos la test results
     cauti export results buton si alegi formatul html sa salvezi

------ 
Pentru a rula teste unittest cu descoperire automată, puteți folosi următoarea comandă în linia de comandă:
 - python -m unittest discover -s cale_catre_directorul_cu_teste -p "*_test.py"
Aceasta va căuta toate fișierele care se termină cu _test.py în directorul specificat și va rula toate testele.

Folosirea modulului unittest-xml-reporting pentru rapoarte XML:
 - pip install unittest-xml-reporting

python -m unittest test_module.py --reportxml=test_report.xml


"""