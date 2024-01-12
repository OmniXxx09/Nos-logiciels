from tkinter import *
import smtplib
import random as rd
from email.mime.text import MIMEText
import json
fichiercfg= open("config.json")
cfg= json.load(fichiercfg)
a = 2
def stop1():
    global a
    a = 3
   
while a==2 :   
    def dec1():
        f4.destroy()
        fenetre1()
        
    def dec2():
        f3.destroy()
        fenetre1()
        
    def logged1():
        f2.destroy()
        logged()
        
    def logged():
        global f4
        global dec1
        f4 = Tk()
        f4.geometry('1920x1080')
        f4['bg'] = 'lavenderblush1'
        la41 = Label(f4,text="Connexion reussie : ",font=("Verdana",20))
        la41.place(x='800',y='100')
        bul1 = Button(f4, text='Deconnexion', command=dec1, bg='red', fg='white', font=("Verdana", 40))
        bul1.place(x='700', y='650', width=500, height=90)
        
    def nlogged1():
        f2.destroy()
        nlogged()
        
    def nlogged():
        print("f")
        global f4
        global dec1
        f4 = Tk()
        f4.geometry('1920x1080')
        f4['bg'] = 'lavenderblush1'
        la41 = Label(f4,text="Identifiant Invalide : ",font=("Verdana",20))
        la41.place(x='780',y='100')
        bul1 = Button(f4, text="Revenir à la page d'accueil", command=dec1, bg='red', fg='white', font=("Verdana", 20))
        bul1.place(x='700', y='650', width=500, height=90)
        
    def login():
        global f2
        global lmail
        global lmdp
        f2 = Tk()
        f2.geometry('1920x1080')
        f2['bg'] = 'lavenderblush1'
        lmail = StringVar()
        lmdp = StringVar()

        la21 = Label(f2, text="Saisissez votre email : ", font=("Verdana", 20))
        la21.place(x='800', y='100')

        la22 = Label(f2, text=" Saisissez votre mot de passe : ", font=("Verdana", 20))
        la22.place(x='760', y='450')

        en21 = Entry(f2, textvariable=lmail)
        en21.place(x='900', y='250')

        en22 = Entry(f2, textvariable=lmdp)
        en22.place(x='900', y='600')
        
        bu21 = Button(f2, text='Log in', command=check, bg='blue', fg='white', font=("Verdana", 40))
        bu21.place(x='850', y='650', width=200, height=90)
        
    def check():
        cpt=0
        cp=0
        em=False
        md=False
        if lmail.get()=='' or  lmdp.get()=='' :
            nlogged1()
        else:
            for value in MAIL:
                if lmail.get() == value:
                    print("W")
                    md=True
                    break
                else:
                    print("F")
                    cpt=cpt+1
                    
            for value in MDP:
                if lmdp.get() == value:
                    em=True
                    cp2=cp
                    break 
                else:
                    print("F")
                    cp=cp+1
            if cpt==cp:
                logged1()
            else:
                nlogged1()
            
    def log1():
        f1.destroy()
        login()
    def signup1():
        f1.destroy()
        signup()
    def signup():
        global rmail
        global rmdp
        print("f")
        global f3
        global dec1
        f3 = Tk()
        f3.geometry('1920x1080')
        f3['bg'] = 'lavenderblush1'
        
        la31 = Label(f3,text="Saisissez votre email : ",font=("Verdana",20))
        la31.place(x='800',y='100')
        
        la32 = Label(f3,text=" Créer votre mot de passe : ",font=("Verdana",20))
        la32.place(x='760',y='450')
        
        rmail=StringVar()
        email = Entry(f3, textvariable=rmail)
        email.place(x='900',y='250')
        rmdp=StringVar()
        mdp = Entry(f3, textvariable=rmdp)
        mdp.place(x='900',y='600')
        bu31 = Button(f3, text='Sign up', command=register, bg='blue', fg='white', font=("Verdana", 40))
        bu31.place(x='850', y='650', width=200, height=90)
    MAIL=[]
    MDP=[]
    def register():
        global Rmail
        global Rmdp
        Rmail = rmail.get()
        MAIL.append(Rmail)
        Rmdp = rmdp.get()
        MDP.append(Rmdp)
        print(MAIL)
        print(MDP)
        dec2()
        
    def stre():
        f1.destroy()
    def stop():
        stop1()
        stre()
    def fenetre1():
        global f1
        f1 = Tk()
        f1.geometry('1920x1080')
        f1['bg'] = 'lavenderblush1'

        la11 = Label(f1, text="Bonjour et bienvenue ", font=("Verdana", 40), bg='lavenderblush1', fg='blue')
        la11.place(x='680', y='100')

        la12 = Label(f1, text="Avez vous un compte ? ", font=("Verdana", 20), bg='lavenderblush1', fg='blue')
        la12.place(x='800', y='250')

        bu11 = Button(f1, text='Log in', command=log1, bg='blue', fg='white', font=("Verdana", 40))
        bu12 = Button(f1, text='Sign up', command=signup1, bg='blue', fg='white', font=("Verdana", 37))

        bu11.place(x='705', y='450', width=200, height=90)
        bu12.place(x='1000', y='450', width=200, height=90)
        
        bu13 = Button(f1, text='Quitter', command=stop, bg='blue', fg='white', font=("Verdana", 40))
        bu13.place(x='1500', y='10', width=200, height=90)
        
        bu14 = Button(f1, text='Mot de passe oublier ?', command=gmailcdv, bg='blue', fg='white', font=("Verdana", 27))
        bu14.place(x='700', y='600', width=500, height=90)
    
    def gmailcdvgi():
        global f5
        global en51v
        f5 = Tk()
        f5.geometry('1920x1080')
        f5['bg'] = 'lavenderblush1'
        en51v=StringVar()
        gmail= Entry(f5, textvariable=en51v)
        gmail.place(x='900', y='250')
        
        def gmailcdv1() :
                global en51v
                global en61v
                global a4
                global rd51
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                rd51 =rd.randint(100000,999999)
                a1='Bonjour voici votre code de verification :',rd51
                a4=str(a1)
                # Login lel gmail
                server.login(cfg["mail"], cfg["mdp"])

                # chnowa ili fi w<set el gmail
                msg = MIMEText(a4)
                msg['Subject'] = 'Mdp Manger:Code de verification'
                msg['From'] = cfg["mail"]
                msg['To'] = en51v.get()

                # Ba3then el mail
                server.sendmail("mdpmanager73@gmail.com", en51v.get() , msg.as_string())
                print("Message envoyé !")
                
                server.quit()
                
                f5.destroy()
                f6 = Tk()
                f6.geometry('1920x1080')
                f6['bg'] = 'lavenderblush1'
                en61v=StringVar()
                en61=Entry(f6,textvariable=en61v)
                en61.place(x='900', y='250')
                def verifcdv():
                    def nvmdp():
                        global fenetre1
                        nvmd=StringVar()
                        f8 = Tk()
                        f8.geometry('1920x1080')
                        f8['bg'] = 'lavenderblush1'
                        en81=Entry(f8,textvariable=nvmd)
                        en81.place(x='900', y='250')
                        def verifnmdp():
                            MDP[cpte]=nvmd.get
                            fenetre1()
                            f8.destroy
                        bu81 = Button(f8, text='Valider', command=verifnmdp, bg='blue', fg='white', font=("Verdana", 27))
                        bu81.place(x='700', y='600', width=500, height=90)

                    def newlog():          
                            global cpte 
                            global mdpn
                            cpte=0
                            cp=0
                            em=False
                            md=False
                            mdpn=StringVar()
                            f7 = Tk()
                            f7.geometry('1920x1080')
                            f7['bg'] = 'lavenderblush1'
                            en71=Entry(f7,textvariable=mdpn)
                            en71.place(x='900', y='250')
                            def valider():
                                global MDP
                                global cpte
                                cpte=0
                                for i in MAIL:
                                    if en51v.get() == i :
                                        nvmdp()
                                        f7.destroy
                                        break
                                    else:
                                        print("Frh")
                                        cpte=cpte+1

                            bu71 = Button(f7, text='Valider', command=valider, bg='blue', fg='white', font=("Verdana", 27))
                            bu71.place(x='700', y='600', width=500, height=90)
                    print(a4)
                    print(en61v.get())
                    rd51s=str(rd51)
                    if rd51s==en61v.get() :
                        newlog()
                        f6.destroy()
                    else :
                        print("error")
                bu61 = Button(f6, text='Valider', command=verifcdv, bg='blue', fg='white', font=("Verdana", 27))
                bu61.place(x='700', y='600', width=500, height=90)
    
        bu51 = Button(f5, text='Valider', command=gmailcdv1, bg='blue', fg='white', font=("Verdana", 27))
        bu51.place(x='700', y='600', width=500, height=90)

    def gmailcdv():
        f1.destroy()
        gmailcdvgi()
    
        
        
    
        
       
    
    fenetre1()
    mainloop()
