from enum import Flag
import string
from tkinter import *
import math , random , os
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootroot@@1234",
  database = "python_database",
)
class super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1200x600+30+10')
        self.root.title('Agence de location')
        self.root.resizable(False,False)
        self.root.iconbitmap('C:\\image\\icone.ico')
        title = Label(self.root , text='gestion de : agence de location' , fg='white' , bg='#0B2F3A' , font=('tajawal',15))
        title.pack(fill=X)
        options=[
        "Class A AMG",
        "Class C AMG",
        "Class S AMG",
        "GLA",
        "GLS",]
        clicked = StringVar()
        clicked.set(options[0])
        ooptions=[
        "Opel Astra",
        "Opel CrossLand",
        "Opel GrandLand",
        "OpeL Moukka",
        "Opel coursa",]
        cllicked = StringVar()
        cllicked.set(ooptions[0])
        optionss=[
        "BMW Serie 1",
        "BMW Serie 2",
        "BMW Serie 3",
        "BMW Serie 4",
        "BMW Serie 5",]
        clickedd = StringVar()
        clickedd.set(optionss[0])
        optionsss=[
        "Audit A1",
        "Audit A2",
        "Audit A3",
        "Audit A4",
        "Audit A5",]
        clickeddd = StringVar()
        clickeddd.set(optionsss[0])
        optionssss=[
        "Velar",
        "Sport",
        "Evoque",
        "Vogue",
        "Defender",]
        clickedddd = StringVar()
        clickedddd.set(optionssss[0])
        optionsssss=[
        "Tucson",
        "Creta",
        "Santafe",
        "i30",
        "i10",]
        clickeddddd = StringVar()
        clickeddddd.set(optionsssss[0])
        optionssssss=[
        "CLIO 4",
        "Megane",
        "Megane RS",
        "Kadjar",
        "CLIO 5",]
        clickedddddd = StringVar()
        clickedddddd.set(optionssssss[0])
        optionsssssss=[
        "Logan",
        "Sandero",
        "Duster",
        "Doccker",]
        clickeddddddd = StringVar()
        clickeddddddd.set(optionsssssss[0])
        optionssssssss=[
        "PANDA",
        "UNO",
        "500",
        "500 XXL",]
        clickedddddddd = StringVar()
        clickedddddddd.set(optionssssssss[0])
        optioon=[
        "PICANTO",
        "SORENTO",
        "SELTOS",
        "CERATO",]
        clickeed = StringVar()
        clickeed.set(optioon[0])
        optionn=[
        "LION",
        "LION FR",]
        cliicked = StringVar()
        cliicked.set(optionn[0])
        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        x = random.randint(1000,9999)
        self.fatora.set(str(x))
        self.numero = StringVar()
        
        self.remise = StringVar()

        self.risque = StringVar()

        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()

        self.qq1 = IntVar()
        self.qq2 = IntVar()
        self.qq3 = IntVar()
        self.qq4 = IntVar()
        self.qq5 = IntVar()
        self.qq6 = IntVar()
        self.qq7 = IntVar()
        self.qq8 = IntVar()
        self.qq9 = IntVar()
        self.qq10 = IntVar()
        self.qq11 = IntVar()

        self.qqq1 = IntVar()
        self.qqq2 = IntVar()
        self.qqq3 = IntVar()
        self.qqq4 = IntVar()
        self.qqq5 = IntVar()
        self.qqq6 = IntVar()
        self.qqq7 = IntVar()
        def stock():
            c = mydb.cursor()
            name = self.namo.get()
            num = self.phono.get()
            facture = self.fatora.get()

            insert_data = "INSERT INTO `Client`(`name` , `num` , `facture`) VALUES(%s,%s,%s)"
            vals = (name , num , facture)
            c.execute(insert_data , vals)
            mydb.commit() 
        F1 = Frame(root , bd=2 , width=338 , height=170 , bg='#0B4C5F')
        F1.place(x=3 , y=30)
        tit = Label(F1 , text='INFORMATION DU CLIENT : ' , font=('tajawal' , 13 , 'bold') , bg='#0B4C5F' , fg='tomato')
        tit.place(x=5 , y =0)
        his__name = Label(F1 , text='Nom du client : ' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='white')
        his__name.place(x= 5 , y = 30)
        his__phone = Label(F1 , text='Numero du client : ' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='white')
        his__phone.place(x= 5 , y = 60)
        bill__name = Label(F1 , text='Numero de Facture : ' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='white')
        bill__name.place(x= 5 , y = 90)
        Ent__name = Entry(F1 , textvariable = self.namo , justify='center')
        Ent__name.place(x = 155 , y = 32 )
        Ent__phone = Entry(F1 ,  textvariable = self.phono , justify='center')
        Ent__phone.place(x = 155 , y = 60 )
        Ent__bill = Entry(F1 , textvariable = self.fatora ,  justify='center')
        Ent__bill.place(x = 155 , y = 90 )

        btn__customor = Button(F1 , text='Enreg' , font=('tajawal' , 10 ) , width=5 , height=4  ,bg='tomato'  , command=stock)
        btn__customor.place(x =283 , y = 33)

        tidd = Label(F1 , text='[Les Factures]' , font=('tajawal', 13  ,'bold') , bg="#0B4C5F"  ,fg='gold')
        tidd.place(x = 100 , y = 135)

        F3 =  Frame(root, bd=1  , width= 138  , height=399  , bg='white' ) 
        F3.place(x= 5, y=203 )
        scrol_y  =Scrollbar (F3, orient=VERTICAL) 
        self.textarea= Text (F3 , yscrollcommand=scrol_y.set)
        scrol_y.pack (side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH ,  expand=1)
        F4  =Frame(root , bd = 2 , width=657 , height=112 , bg ="#0B4C5F" )
        F4.place(x = 5 , y = 487)
        calcule = Button (F4 , text="Risque" , width=12 , height=1 , font=('tajawal',12), bg="gold" , command=self.totall )
        calcule.place (x=5,y=5)
        facture =Button(F4, text='Remise' , width=12 , height=1,font=('tajawal',12),bg='gold' , command=self.totalll)
        facture.place(x = 5 , y = 50)
        clear = Button(F4 , text='Remplis Champs' , width=12, height= 1 , font= ('tajawal',12) , bg='gold' , command=self.welcome  )
        clear.place(x = 150 , y=5)
        exite = Button(F4, text='Nb.Jour ' , width=12 , height=1,font=('tajawal',12) , bg='gold' , command=self.Angu)
        exite.place(x = 150 , y=50)
        lbol = Label(F4 , text = 'Calcule des nombre de jours' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='gold')
        lbol.place(x = 300 , y = 5 )
        lbol1 = Label(F4 , text = 'Calcule de la Remise' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='gold')
        lbol1.place(x = 300 , y = 30 )
        lbol2 = Label(F4 , text = 'Calcule des Resiques' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='gold')
        lbol2.place(x = 300 , y = 60 )
        ento11 = Entry(F4 , width=24 , textvariable=self.numero ,  justify='center')
        ento11.place(x = 500 , y = 5 )
        ento1 = Entry(F4 , width=24 ,  textvariable=self.remise , justify='center')
        ento1.place(x = 500 , y = 32 )
        ento2 = Entry(F4 , width=24 , textvariable=self.risque ,  justify='center')
        ento2.place(x = 500 , y = 60 )
        
        FF1 = Frame(root , width=318 , height=664 , bg='#0B4C5F')
        FF1.place(x = 882 , y = 28) 
        
        t = Label(FF1  ,text='Jours et Voiture' , font=('tajawal' , 13 , 'bold') , bg='#0B4C5F' , fg='gold')
        t.place(x =100, y =0  )

        ty1 = Label(FF1 , text= 'Mercedes' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty1.place(x = 10 , y = 50)
        ty2 = Label(FF1 , text= 'Opel' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty2.place(x = 10 , y = 100)
        ty3 = Label(FF1 , text= 'BMW' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty3.place(x = 10 , y = 150)
        t4 = Label(FF1 , text= 'Audi' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        t4.place(x = 10 , y = 200)
        ty5 = Label(FF1 , text= 'Range Rover' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty5.place(x = 10 , y = 250)
        ty6 = Label(FF1 , text= 'Hyundai' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty6.place(x = 10 , y = 300)
        ty7 = Label(FF1 , text= 'Renault' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty7.place(x = 10 , y = 350)
        ty8 = Label(FF1 , text= 'Dacia' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty8.place(x = 10 , y = 400)
        ty9 = Label(FF1 , text= 'Fiat' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty9.place(x = 10 , y = 450)
        ty11 = Label(FF1 , text= 'Kia' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty11.place(x = 10 , y = 500)
        ty12 = Label(FF1 , text= 'Seat' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty12.place(x = 10 , y = 540)

        Bquen = OptionMenu(FF1 , clicked , *options)
        Bquen.place(x = 170  , y = 52)
        Bquen1 = OptionMenu(FF1 , cllicked , *ooptions)
        Bquen1.place(x = 170  , y = 102)
        Bquen2 = OptionMenu(FF1 , clickedd , *optionss)
        Bquen2.place(x = 170  , y = 152)
        Bquen3 = OptionMenu(FF1 , clickeddd , *optionsss)
        Bquen3.place(x = 170  , y = 202)
        Bquen4 = OptionMenu(FF1 , clickedddd , *optionssss)
        Bquen4.place(x = 170  , y = 252)
        Bquen5 = OptionMenu(FF1 , clickeddddd , *optionsssss)
        Bquen5.place(x = 170  , y = 302)
        Bquen6 = OptionMenu(FF1 , clickedddddd , *optionssssss)
        Bquen6.place(x = 170  , y = 352)
        Bquen7 = OptionMenu(FF1 , clickeddddddd , *optionsssssss)
        Bquen7.place(x = 170  , y = 402)
        Bquen8= OptionMenu(FF1 , clickedddddddd  , *optionssssssss)
        Bquen8.place(x = 170  , y = 452)
        Bquen9 = OptionMenu(FF1 , clickeed , *optioon)
        Bquen9.place(x = 170  , y = 502)
        Bquen10 = OptionMenu(FF1 , cliicked , *optionn)
        Bquen10.place(x = 170  , y = 542)

        FF2 = Frame(root , width=538 , height=168 , bg= "#0B4C5F")
        FF2.place(x = 343 , y = 30)
        r = Label(FF2 , text='Remise' , font=('tajawal' , 13 , 'bold') , bg="#0B4C5F" , fg='gold')
        r.place(x = 238 , y = 5)

        his__name = Label(FF2 , text='Jours : ' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='white')
        his__name.place(x= 60 , y = 30)
        his__phone = Label(FF2 , text='Semaine : ' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='white')
        his__phone.place(x= 60 , y = 60)
        bill__name = Label(FF2 , text='Mois : ' , font=('tajawal' , 10 , 'bold') , bg='#0B4C5F' , fg='white')
        bill__name.place(x= 60, y = 90)
        Ent__name = Entry(FF2 , textvariable=self.q1 ,   justify='center')
        Ent__name.place(x = 200 , y = 32 )
        Ent__phone = Entry(FF2 , textvariable=self.q2 ,  justify='center')
        Ent__phone.place(x = 200 , y = 60 )
        Ent__bill = Entry(FF2 , textvariable=self.q3 ,  justify='center')
        Ent__bill.place(x = 200 , y = 90 )
        
        FF3 = Frame(root , width=207 , height=398 , bg= "#0B4C5F")
        FF3.place(x = 674 , y = 200)
        U = Label(FF3 , text='RISQUE' , font=('tajawal' , 13 , 'bold') , bg="#0B4C5F" , fg='gold')
        U.place(x = 70 , y = 5)
        t4 = Label(FF3 , text= 'Roue' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        t4.place(x = 10 , y = 50)
        ty5 = Label(FF3 , text= 'feu-arrier' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty5.place(x = 10 , y = 100)
        ty6 = Label(FF3 , text= 'Rétroviseur' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty6.place(x = 10 , y = 150)
        ty7 = Label(FF3 , text= 'Pare-brise' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty7.place(x = 10 , y = 200)
        ty8 = Label(FF3 , text= 'Pare-chocs' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty8.place(x = 10 , y = 250)
        ty9 = Label(FF3 , text= 'Phare' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty9.place(x = 10 , y = 300)
        ty11 = Label(FF3 , text= 'Autre' , font=('tajawal' , 11 , 'bold') , bg="#0B4C5F" , fg='white')
        ty11.place(x = 10 , y = 350)
        Bquen3 = Entry(FF3 , width=7 , textvariable=self.qqq1  )
        Bquen3.place(x = 120  , y = 50)
        Bquen4 = Entry(FF3 , width=7 , textvariable=self.qqq2 )
        Bquen4.place(x = 120  , y = 100)
        Bquen5 = Entry(FF3 , width=7 , textvariable=self.qqq3 )
        Bquen5.place(x = 120  , y = 150)
        Bquen6 = Entry(FF3 , width=7 , textvariable=self.qqq4 )
        Bquen6.place(x = 120  , y = 200)
        Bquen7 = Entry(FF3 , width=7 , textvariable=self.qqq5 )
        Bquen7.place(x = 120  , y = 250)
        Bquen8= Entry(FF3 , width=7 , textvariable=self.qqq6 )
        Bquen8.place(x = 120  , y = 300)
        Bquen9 =Entry(FF3 , width=7 , textvariable=self.qqq7 )
        Bquen9.place(x = 120  , y = 350)
        self.welcome()
    def totalll(self):
        self.jour = self.q1.get()* 1.5
        self.semaine = self.q2.get()* 2.5
        self.mois = self.q3.get() * 3.5
        self.totalio = float(
            self.jour+
            self.semaine+
            self.mois
            )
        self.remise.set(str(self.totalio)+ ' $ ')
        self.alll = float(
            self.totalio+
            self.totalio
        )
    def totall(self):
        self.roue = self.qqq1.get()* 2.00
        self.feu = self.qqq2.get()* 4.00
        self.retro = self.qqq3.get()* 5.00
        self.pare = self.qqq4.get()* 5.00
        self.chock = self.qqq5.get()* 1.000
        self.phare = self.qqq6.get()* 3.00
        self.autre = self.qqq7.get()* 7.00
        self.tol = float(
            self.roue+
            self.feu+
            self.retro+
            self.pare+
            self.chock+
            self.phare+
            self.autre
            )
        self.risque.set(str(self.tol) + "$")
        self.all = float(
            self.tol+
            self.tol
        )
    def Angu(self):
        self.mercedes = self.qq1.get()* 2.0
        self.opel = self.qq2.get()* 9.0
        self.bmw = self.qq3.get()* 1.5
        self.audi = self.qq4.get()* 1.0
        self.range = self.qq5.get()* 1.7
        self.hyundai = self.qq6.get()* 6.0
        self.renault = self.qq7.get()* 3.0
        self.dacia = self.qq8.get()* 1.5
        self.fiat = self.qq9.get()* 1.5
        self.kia = self.qq10.get()* 1.0
        self.seat = self.qq11.get()* 2.5
        self.tot = float(
            self.mercedes+
            self.opel+
            self.bmw+
            self.audi+
            self.range+
            self.hyundai+
            self.renault+
            self.dacia+
            self.fiat+
            self.kia+
            self.seat
            )
        self.numero.set(str(self.tot) + "$")
        self.all = float(
            self.tot+
            self.tot
        )
    def welcome (self):
            c = mydb.cursor()
            remis = self.remise.get()
            risqu = self.risque.get()
            numer = self.numero.get()

            insert_data = "INSERT INTO `upf`(`res` , `req` , `jr`) VALUES(%s,%s,%s)"
            vals = (remis , risqu, numer)
            c.execute(insert_data , vals)
            mydb.commit() 
            self.textarea.delete ('1.0', END)
            self.textarea.insert(END,"     Bienvenue dans notre Agence")
            self.textarea.insert(END , "\n================================================================================")
            self.textarea.insert(END , f"\n NUM.fACT : {self.fatora.get()} ")
            self.textarea.insert(END , f"\n NAME  : {self.namo.get()}")
            self.textarea.insert(END , f"\n NUM.CLI : {self.phono.get()} ")
            self.textarea.insert(END , "\n================================================================================")
            self.textarea.insert(END , f"\n Nb.Jours   \t        \t Remise              Risque")
            self.textarea.insert(END , f"\n {self.numero.get()}" , f" \t{self.remise.get()}" , f" \t\t                           {self.risque.get()}" ,)
            self.textarea.insert(END , f"\n                    {self.risque.get()}")
            self.textarea.insert(END , "\n================================================================================")


root  =Tk()
ob = super(root)
root.mainloop()   
