import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from z_models_torie.pages.pagina_metode_model import PaginaMetode

# from driver import Driver

class TestPagina(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.pagina = PaginaMetode(self.driver)

    def tearDown(self):
        self.driver.quit()

    # pentru   from driver import Driver
    # def setUp(self):
    #     self.driver = Driver()
    #     self.pagina = PaginaMetode(self.driver.driver)
    #
    # def tearDown(self):
    #     self.driver.close()

    def test_autentificare_corecta(self):
        self.pagina.deschide_pagina()
        self.pagina.introdu_username("tomsmith")
        self.pagina.introdu_parola("SuperSecretPassword!")
        self.pagina.apasa_autentificare()
        # Adăugați aici aserțiuni pentru test

    def test_autentificare_incorecta(self):
        self.pagina.deschide_pagina()
        self.pagina.introdu_username("utilizator_gresit")
        self.pagina.introdu_parola("parola_gresita")
        self.pagina.apasa_autentificare()
        # Adăugați aici aserțiuni pentru test


if __name__ == "__main__":
    unittest.main()


\