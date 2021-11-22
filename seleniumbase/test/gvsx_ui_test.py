from seleniumbase import BaseCase
import requests

class BaseTestCase(BaseCase):
    def check_and_click(self, selector, text):
        self.assert_element(selector)
        self.assert_text(text, selector)
        self.click(selector)

    def check(self, selector, text):
        self.assert_element(selector)
        self.assert_text(text, selector)

class LoginPage():
    def login(self, sb, username, pwd):
        #-------------------------------------
        # Belépés
        #-------------------------------------
        url = "http://10.11.132.5:8080/"
        mezo_nev = 'input#userName' 
        mezo_jelszo = 'input#password'
        gomb_belepes = 'button[class="MuiButtonBase-root MuiButton-root MuiButton-contained jss4 MuiButton-containedPrimary MuiButton-fullWidth"]'
        #-------------------------------------
        sb.open(url)
        sb.type(mezo_nev,username)
        sb.type(mezo_jelszo,pwd)
        sb.click(gomb_belepes)

#-------------------------------------
# Menüpontok
#-------------------------------------
menu_confi = 'span:contains("Konfiguráció")'
menu_event = 'span:contains("Események")'
menu_stati = 'span:contains("Statisztika")'
menu_statu = 'span:contains("Státusz")'

menu = 'div#root>div>div>div>ul>div'
icon = '>div>svg'

menu_confi_icon = menu+icon
menu_event_icon = menu+':nth-of-type(2)'+icon
menu_stati_icon = menu+':nth-of-type(3)'+icon
menu_statu_icon = menu+':nth-of-type(4)'+icon
#-------------------------------------
gomb_edit = 'div#root>div>main>div>div>div:nth-of-type(2)>div:nth-of-type(2)>div>div>div>div>div>div>div:nth-of-type(4)>button'
gomb_menu_hide = 'path#ic_chevron_right_24px'
text_error = 'div.MuiAlert-message'
#-------------------------------------
headers = {'Accept':'*/*', 'Content-Type': 'application/json'}

class TrafficSpotUI(BaseTestCase):
    def test_01_belepes_hibas_nev(self):
        LoginPage().login(self, "akarmi","Password1")
        self.check(text_error, "Hibás név vagy jelszó")

    def test_02_belepes_ures_nev(self):
        LoginPage().login(self, "","Password1")
        text_error = 'p#userName-helper-text'
        self.check(text_error, "Felhasználónév kötelező")

    def test_03_belepes_hibas_jelszo(self):
        LoginPage().login(self, "admin","Password2")
        self.check(text_error, "Hibás név vagy jelszó")

    def test_04_belepes_ures_jelszo(self):
        LoginPage().login(self, "admin","")
        text_error = 'p#password-helper-text'
        self.check(text_error, "Jelszó kötelező")

    def test_05_belepes_sikeres(self):
        LoginPage().login(self, "admin","Password1")
        self.check(menu_confi, "Konfiguráció")

    def test_06_health_check_menu(self):
        LoginPage().login(self, "admin","Password1")
        self.check_and_click(gomb_edit, "Szerkesztés")
        self.check_and_click(menu_confi, "Konfiguráció")
        self.check_and_click(menu_event, "Események")
        self.check_and_click(menu_stati, "Statisztika")
        self.check_and_click(menu_statu, "Státusz")
        self.click(gomb_menu_hide)
        self.click(menu_confi_icon)
        self.click(menu_event_icon)
        self.click(menu_stati_icon)
        self.click(menu_statu_icon)
        self.click(gomb_menu_hide)

    def test_07_health_check_esemenyek(self):
        LoginPage().login(self, "admin","Password1")
        self.click(menu_event)
        #-------------------------------------
        sor = 'div#root>div>main>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>div>div>div>div>div>div'
        sor1 = sor+'>div'
        sor2 = sor+':nth-of-type(2)>div'
        gomb_kovetkezo = 'div#root>div>main>div>div>div:nth-of-type(3)>button'
        gomb_elozo = 'div#root>div>main>div>div>div>button'
        #-------------------------------------

        self.assert_element(sor1)
        self.click(sor1)
        self.sleep(1)
        self.driver.close()
        self.switch_to_default_window()

        self.assert_element(sor2)
        self.click(sor2)
        self.sleep(1)
        self.driver.close()
        self.switch_to_default_window()

        self.click(sor1)
        self.sleep(1)
        self.check_and_click(gomb_kovetkezo, "Következő")
        self.click(gomb_kovetkezo)
        self.sleep(1)
        self.click(gomb_kovetkezo)
        self.sleep(1)
        self.check_and_click(gomb_elozo, "Előző")
        self.click(gomb_elozo)
        self.sleep(1)
        self.click(gomb_elozo)
        self.sleep(1)
        self.driver.close()
        self.switch_to_default_window()
