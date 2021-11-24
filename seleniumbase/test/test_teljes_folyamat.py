from seleniumbase import BaseCase
from datetime import datetime ,timedelta
import uuid



class MyTestClass(BaseCase):
   def test_basics(self):      
        mezo_nev = 'input[type="email"]'
        mezo_jelszo = 'input[type="password"]'
        gomb_belepes = 'button[type="submit"]'
        email = "admin@admin.hu"
        jelszo = "Password1!"        
        self.open('https://szevnexius.northeurope.cloudapp.azure.com:2433/Identity/Account/Login?ReturnUrl=https://szevnexius.northeurope.cloudapp.azure.com:1433')   
        self.maximize_window()
        self.sleep(2)
        self.type(mezo_nev, email)
        self.type(mezo_jelszo, jelszo)
        self.click(gomb_belepes)
        #IDOPONTOK#
        vizsga_nyitása = (datetime.today() + timedelta(hours=4)).strftime('%H') 
        vizsga_kezdete = (datetime.today() + timedelta(hours=5)).strftime('%H')
        vizsga_nap_vege = (datetime.today() + timedelta(days=1)).strftime('%d')
         
        menu_jegyzokonyvek = 'li[data-controller="ExamReports"]'
        gomb_uj_jegyzokonyv = 'button[aria-controls="exam-report-table"]'
        mezo_azonosito = 'input[name="Identifier"]'
        mezo_helyszin = '#ExamAddressId'
        helyszin_option = '#ExamAddressId>option:nth-child(2)'
        gomb_mentes = 'button[type="submit"]'
        date_time_picker_nyitas='div[class="col-6"]>div:first-child>input[class="form-control datetimepicker form-control input"]'
        date_time_picker_kezdet = 'div[class="col-6"]>div:nth-child(2)>input[class="form-control datetimepicker form-control input"]'
        date_time_picker_vege = 'div[id="ExamReportEditTabContent"]>div[id="ExamReport"]>div[class="row"]>div:nth-child(2)>div:nth-child(2)>input:nth-child(3)'
        blank = 'div[class="main p-4 flex-grow-1"]'
        date_time_picker_hour = 'input[class="numInput flatpickr-hour"]'  
        date_time_picker_hour2 = 'body>div:nth-child(4)>div:nth-child(3)>div:first-child>input'
        date_time_picker_day = 'body>div:nth-child(8)>div[class="flatpickr-innerContainer"]>div[class="flatpickr-rContainer"]>div[class="flatpickr-days"]>div>span:nth-child('+vizsga_nap_vege+')'
        
        #Uj VJK + Helyszín
        self.click(menu_jegyzokonyvek)
        self.click(gomb_uj_jegyzokonyv)
        self.type(mezo_azonosito,"Test Automation VJK")
        self.click(date_time_picker_nyitas)
        self.type(date_time_picker_hour,vizsga_nyitása)    
        self.click(blank)   
        self.click(date_time_picker_kezdet)         
        self.type(date_time_picker_hour2,vizsga_kezdete)
        self.click(blank)  
        self.click(date_time_picker_vege)
        self.click(date_time_picker_day) 
        self.click(mezo_helyszin)  
        self.click(helyszin_option) 
        self.click(blank)  
        self.click(gomb_mentes)

        #Vizsgázó felvétele
        nav_vizsgazok = '#ExamReportEditTab>li:nth-child(3)'
        gomb_hozzaadas  =  '#students-table_wrapper>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>button:nth-child(1)'
        mezo_nyilvantartasi_szam =  '#RegistrationNumber'
        mezo_vezeteknev = '#Surname'
        mezo_keresztnev = '#Forename1'
        mezo_allampolgarsag = '#Citizenship'
        mezo_anyja_neve = '#MothersName'
        mezo_szuletsi_hely = '#BirthPlace'
        date_picker_szuletesi_ido = 'div>div[class="row student-edit-rows"]:nth-child(9)>div:nth-child(2)>div>input:nth-child(2)'
        date_picker_mezo_evszam = 'body>div:nth-child(3)>div:nth-child(1)>div:nth-child(2)>div>div>input'
        date_picker_mezo_nap = 'body>div:nth-child(3)>div:nth-child(2)>div>div:nth-child(2)>div>span:nth-child(18)'
        mezo_email =  '#Email'
        mezo_nyelv = '#Language'
        option_nyelv_magyar = '#Language>option[value="0"]'
        mezo_viszsgagep = '#ComputerNumber' 
        date_time_picker_vizsga_kezdes =  '#student-edit-exam-info>div[class="row student-edit-rows"]:nth-child(2)>div:nth-child(2)>div>input:nth-child(2)'
        date_time_picker_hour_vizsga_kezdes = 'body>div:nth-child(2)>div[class="flatpickr-time time24hr"]>div:nth-child(1)>input'
        gomb_mentes = 'div[class="button-group text-center"]>button'
        gomb_szinkronizálás = 'button[title="Szinkronizálás"]'
        id = str(uuid.uuid4());
        self.click(nav_vizsgazok)
        self.click(gomb_hozzaadas)

        self.type(mezo_nyilvantartasi_szam,id)
        self.click(date_picker_szuletesi_ido)
        self.type(date_picker_mezo_evszam,"1990")
        self.click(date_picker_mezo_nap)
        self.click(blank) 
        self.click(mezo_nyelv)
        self.click(option_nyelv_magyar)   
        self.type(mezo_viszsgagep,"0") 
        self.click(date_time_picker_vizsga_kezdes )
        self.type(date_time_picker_hour_vizsga_kezdes,vizsga_kezdete)
        self.click(blank)
        self.type(mezo_vezeteknev,"Baka")
        self.type(mezo_keresztnev,"Béla")
        self.type(mezo_allampolgarsag,"magyar")
        self.type(mezo_anyja_neve,"Bicske Boglárka")
        self.type(mezo_szuletsi_hely,"Mucsaröcsöge")
        self.type(mezo_email,"nem.tudom@gmail.com")
        self.click(gomb_mentes)
        #----------------------------------------------------------------------------------
        #Vizsga hozzáadása
        #----------------------------------------------------------------------------------
        sor_vizsgazo = '//td[text()="'+id+'"]'
        gomb_vizsga_hozzadas = '#exam-subjects-table_wrapper>div[class="d-flex flex-row align-items-center mt-3"]>div[class="col-6 d-flex"]>div[class=dt-buttons]>button'
        mezo_brutto_idokeret = '#GrossTimeLimitMinutes'
        mezo_vizsga_hozzadaas_date_time_picker = '#add-exam-subject-modal>div>div>div:nth-child(2)>div:nth-child(6)>input:nth-child(3)'
        mezo_date_time_picker_hour = 'body>div:nth-child(10)>div:nth-child(3)>div:first-child>input'

        self.wait_for_element(sor_vizsgazo,"XPATH",60)
        self.click(sor_vizsgazo)
        self.click(gomb_vizsga_hozzadas)
        self.type(mezo_brutto_idokeret,"90")
        self.click(mezo_vizsga_hozzadaas_date_time_picker)
        self.type(mezo_date_time_picker_hour,vizsga_kezdete)




        #self.click(gomb_szinkronizálás)
        self.sleep(5)
        

        





