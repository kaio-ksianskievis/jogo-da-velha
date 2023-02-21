from cProfile import label
from email.mime import image
from platform import java_ver
from tkinter import *
from random import randint
import tkinter 
cinza = "#3b3b3b"
branco = "#FFFFFF"
amarelo = "#fff873"
verde = "#34eb3d"
marrom = "#8B4513"

janela = Tk()
janela.geometry('340x480')
janela.configure(bg=cinza)
janela.title('kaio')
texto_titulo = Label(janela,text='QUANTOS JOGADORES?',font=('ivy 15'),bg=cinza,fg=branco)
texto_titulo.place(x=50,y=80)
b_1_player = Button(janela,command=lambda:(um_jogadores(),b_1_player.destroy()),text='1 jogador',width=15,height=5,bg=branco,fg=cinza)
b_1_player.place(x=110,y=160)
b_2_player = Button(janela,command=lambda:(dois_jogadores(),b_2_player.destroy()),text='2 jogador',width=15,height=5,bg=branco,fg=cinza)
b_2_player.place(x=110,y=300)
def dois_jogadores():
    global cont
    global outro_contador
    global lista_jogada_x
    global lista_jogada_o
    
    frame_cima = Frame(janela,width=340,height=170,bg=cinza)
    frame_cima.grid(row=0,column=0)
    frame_baixo=Frame(janela,width=340,height=310,bg=cinza)
    frame_baixo.grid(row=1,column=0)
    #pontos/escritas frame
    linha_divisoria = Label(frame_cima,width=340,bg=branco)
    linha_divisoria.place(x=0,y=165)
    frame_jogador_1 = Label(frame_cima,text=0,font=('ivy 50'),bg=cinza,fg=branco)
    frame_jogador_1.place(x=80,y=40)
    frame_jogador_2 = Label(frame_cima,text=0,font=('ivy 50'),bg=cinza,fg=branco)
    frame_jogador_2.place(x=230,y=40)
    frame_doispontos = Label(frame_cima,text=':',font=('ivy 50'),bg=cinza,fg=branco)
    frame_doispontos.place(x=165,y=40)
    frame_player_1 = Label(frame_cima,text='player:',font=('ivy 15'),bg=cinza,fg=branco)
    frame_player_1.place(x=30,y=120)
    foto_player_1 = PhotoImage(file='img\icons8-circle-48 (1).png')
    label_foto1 = Label(frame_cima,image=foto_player_1,bg=cinza)
    label_foto1.photo = foto_player_1
    label_foto1.place(x=95,y=123)
    foto_player_2 = PhotoImage(file='img\icons8-close-50 (1).png')
    label_foto1 = Label(frame_cima,image=foto_player_2,bg=cinza)
    label_foto1.photo = foto_player_2
    label_foto1.place(x=265,y=123)



    frame_player_2 = Label(frame_cima,text='player:',font=('ivy 15'),bg=cinza,fg=branco)
    frame_player_2.place(x=200,y=120)
    #linhas
    l_1 = Frame(frame_baixo,width=315,height=8)
    l_1.place(x=15,y=100)
    l_2 = Frame(frame_baixo,width=315,height=8)
    l_2.place(x=15,y=200)
    l_3 = Frame(frame_baixo,width=8,height=290)
    l_3.place(x=110,y=10)
    l_4 = Frame(frame_baixo,width=8,height=290)
    l_4.place(x=230,y=10)
    #imagens
    imagem_o = PhotoImage(file='img\icons8-circle-48.png')
    imagem_x = PhotoImage(file='img\icons8-close-48.png')
    #funcioes
    cont = 0
    outro_contador = 0
    lista_jogada_x = []
    lista_jogada_o = []
    def mudando_contador():
        global cont
        global imagem
        global outro_contador
        cont = cont+1
        if cont%2 == 0:
            outro_contador= 0
        if cont%2 != 0:
            outro_contador = 1
    def icons(b):
        global lista_jogada_x
        global lista_jogada_o
        if b ==1:  
            if outro_contador ==0:
                b_1['image']=imagem_o
                b_1['width']=80
                b_1['height']=80
                lista_jogada_o.append(1)
            if outro_contador ==1:
                b_1['image']=imagem_x
                b_1['width']=80
                b_1['height']=80 
                lista_jogada_x.append(1)      
        if b ==2:  
            if outro_contador ==0:
                b_2['image']=imagem_o
                b_2['width']=80
                b_2['height']=80
                lista_jogada_o.append(2)
            if outro_contador ==1:
                b_2['image']=imagem_x
                b_2['width']=80
                b_2['height']=80
                lista_jogada_x.append(2)  
        if b ==3:  
            if outro_contador ==0:
                b_3['image']=imagem_o
                b_3['width']=80
                b_3['height']=80
                lista_jogada_o.append(3)    
            if outro_contador ==1:
                b_3['image']=imagem_x
                b_3['width']=80
                b_3['height']=80
                lista_jogada_x.append(3)  
        if b ==4:  
            if outro_contador ==0:
                b_4['image']=imagem_o
                b_4['width']=80
                b_4['height']=80
                lista_jogada_o.append(4)   
            if outro_contador ==1:
                b_4['image']=imagem_x
                b_4['width']=80
                b_4['height']=80
                lista_jogada_x.append(4)  
        if b ==5:  
            if outro_contador ==0:
                b_5['image']=imagem_o
                b_5['width']=80
                b_5['height']=80
                lista_jogada_o.append(5)   
            if outro_contador ==1:
                b_5['image']=imagem_x
                b_5['width']=80
                b_5['height']=80
                lista_jogada_x.append(5) 
        if b ==6:  
            if outro_contador ==0:
                b_6['image']=imagem_o
                b_6['width']=80
                b_6['height']=80
                lista_jogada_o.append(6)    
            if outro_contador ==1:
                b_6['image']=imagem_x
                b_6['width']=80
                b_6['height']=80 
                lista_jogada_x.append(6) 
        if b ==7:  
            if outro_contador ==0:
                b_7['image']=imagem_o
                b_7['width']=80
                b_7['height']=80
                lista_jogada_o.append(7)    
            if outro_contador ==1:
                b_7['image']=imagem_x
                b_7['width']=80
                b_7['height']=80
                lista_jogada_x.append(7) 
        if b ==8:  
            if outro_contador ==0:
                b_8['image']=imagem_o
                b_8['width']=80
                b_8['height']=80
                lista_jogada_o.append(8)    
            if outro_contador ==1:
                b_8['image']=imagem_x
                b_8['width']=80
                b_8['height']=80 
                lista_jogada_x.append(8) 
        if b ==9:  
            if outro_contador ==0:
                b_9['image']=imagem_o
                b_9['width']=80
                b_9['height']=80
                lista_jogada_o.append(9)   
            if outro_contador ==1:
                b_9['image']=imagem_x
                b_9['width']=80
                b_9['height']=80
                lista_jogada_x.append(9)
    def desativar(k):
        if k ==1:
            b_1['state'] = tkinter.DISABLED
        if k ==2:
            b_2['state'] = tkinter.DISABLED
        if k ==3:
            b_3['state'] = tkinter.DISABLED
        if k ==4:
            b_4['state'] = tkinter.DISABLED
        if k ==5:
            b_5['state'] = tkinter.DISABLED
        if k ==6:
            b_6['state'] = tkinter.DISABLED
        if k ==7:
            b_7['state'] = tkinter.DISABLED
        if k ==8:
            b_8['state'] = tkinter.DISABLED
        if k ==9:
            b_9['state'] = tkinter.DISABLED
    def ganhador():
        global lista_jogada_x
        global lista_jogada_o
        if 1 in lista_jogada_o:
            if 2 in lista_jogada_o:
                if 3 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(4),desativar(5),desativar(6),desativar(7),desativar(8),desativar(9)
                    return
        if 1 in lista_jogada_o:
            if 4 in lista_jogada_o:
                if 7 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(2),desativar(3),desativar(5),desativar(6),desativar(8),desativar(9)
                    return
        if 4 in lista_jogada_o:
            if 5 in lista_jogada_o:
                if 6 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(7),desativar(8),desativar(9)
                    return
        if 7 in lista_jogada_o:
            if 8 in lista_jogada_o:
                if 9 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(4),desativar(5),desativar(6)
                    return
        if 2 in lista_jogada_o:
            if 5 in lista_jogada_o:
                if 8 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(3),desativar(4),desativar(6),desativar(7),desativar(9)
                    return
        if 3 in lista_jogada_o:
            if 6 in lista_jogada_o:
                if 9 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(5),desativar(7),desativar(8)
                    return
        if 1 in lista_jogada_o:
            if 5 in lista_jogada_o:
                if 9 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(2),desativar(3),desativar(4),desativar(6),desativar(7),desativar(8)
                    return
        if 3 in lista_jogada_o:
            if 5 in lista_jogada_o:
                if 7 in lista_jogada_o:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(6),desativar(8),desativar(9)
                    return
            if 2 in lista_jogada_x:
                if 3 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(4),desativar(5),desativar(6),desativar(7),desativar(8),desativar(9)
                    return
        if 1 in lista_jogada_x:
            if 4 in lista_jogada_x:
                if 7 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(2),desativar(3),desativar(5),desativar(6),desativar(8),desativar(9)
                    return
        if 4 in lista_jogada_x:
            if 5 in lista_jogada_x:
                if 6 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(7),desativar(8),desativar(9)
                    return
        if 7 in lista_jogada_x:
            if 8 in lista_jogada_x:
                if 9 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(4),desativar(5),desativar(6)
                    return
        if 2 in lista_jogada_x:
            if 5 in lista_jogada_x:
                if 8 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(3),desativar(4),desativar(6),desativar(7),desativar(9)
                    return
        if 3 in lista_jogada_x:
            if 6 in lista_jogada_x:
                if 9 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(5),desativar(7),desativar(8)
                    return
        if 1 in lista_jogada_x:
            if 5 in lista_jogada_x:
                if 9 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(2),desativar(3),desativar(4),desativar(6),desativar(7),desativar(8)
                    return
        if 3 in lista_jogada_x:
            if 5 in lista_jogada_x:
                if 7 in lista_jogada_x:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(6),desativar(8),desativar(9)
                    return
        

        



    #botoes
    b_1 = Button(frame_baixo,image=None,command=lambda:(icons(1),mudando_contador(),desativar(1),ganhador()),width=11,height=5,bg=cinza)
    b_1.place(x=17,y=10)
    b_2 = Button(frame_baixo,image=None,command=lambda:(icons(2),mudando_contador(),desativar(2),ganhador()),width=11,height=5,bg=cinza)
    b_2.place(x=17,y=111)
    b_3 = Button(frame_baixo,image=None,command=lambda:(icons(3),mudando_contador(),desativar(3),ganhador()),width=11,height=5,bg=cinza)
    b_3.place(x=17,y=215)
    b_4 = Button(frame_baixo,image=None,command=lambda:(icons(4),mudando_contador(),desativar(4),ganhador()),width=11,height=5,bg=cinza)
    b_4.place(x=130,y=10)
    b_5 = Button(frame_baixo,image=None,command=lambda:(icons(5),mudando_contador(),desativar(5),ganhador()),width=11,height=5,bg=cinza)
    b_5.place(x=130,y=111)
    b_6 = Button(frame_baixo,image=None,command=lambda:(icons(6),mudando_contador(),desativar(6),ganhador()),width=11,height=5,bg=cinza)
    b_6.place(x=130,y=215)
    b_7 = Button(frame_baixo,image=None,command=lambda:(icons(7),mudando_contador(),desativar(7),ganhador()),width=11,height=5,bg=cinza)
    b_7.place(x=244,y=10)
    b_8 = Button(frame_baixo,image=None,command=lambda:(icons(8),mudando_contador(),desativar(8),ganhador()),width=11,height=5,bg=cinza)
    b_8.place(x=244,y=111)
    b_9 = Button(frame_baixo,image=None,command=lambda:(icons(9),mudando_contador(),desativar(9),ganhador()),width=11,height=5,bg=cinza)
    b_9.place(x=244,y=215)
def um_jogadores():
    frame_cima = Frame(janela,width=340,height=170,bg=cinza)
    frame_cima.grid(row=0,column=0)
    frame_baixo=Frame(janela,width=340,height=310,bg=cinza)
    frame_baixo.grid(row=1,column=0)
    #pontos/escritas frame
    linha_divisoria = Label(frame_cima,width=340,bg=branco)
    linha_divisoria.place(x=0,y=165)
    frame_jogador_1 = Label(frame_cima,text=0,font=('ivy 50'),bg=cinza,fg=branco)
    frame_jogador_1.place(x=80,y=40)
    frame_jogador_2 = Label(frame_cima,text=0,font=('ivy 50'),bg=cinza,fg=branco)
    frame_jogador_2.place(x=230,y=40)
    frame_doispontos = Label(frame_cima,text=':',font=('ivy 50'),bg=cinza,fg=branco)
    frame_doispontos.place(x=165,y=40)
    frame_player_1 = Label(frame_cima,text='player:',font=('ivy 15'),bg=cinza,fg=branco)
    frame_player_1.place(x=30,y=120)
    foto_player_1 = PhotoImage(file='img\icons8-circle-48 (1).png')
    label_foto1 = Label(frame_cima,image=foto_player_1,bg=cinza)
    label_foto1.photo = foto_player_1
    label_foto1.place(x=95,y=123)
    foto_player_2 = PhotoImage(file='img\icons8-close-50 (1).png')
    label_foto1 = Label(frame_cima,image=foto_player_2,bg=cinza)
    label_foto1.photo = foto_player_2
    label_foto1.place(x=265,y=123)



    frame_player_2 = Label(frame_cima,text='player:',font=('ivy 15'),bg=cinza,fg=branco)
    frame_player_2.place(x=200,y=120)
    #linhas
    l_1 = Frame(frame_baixo,width=315,height=8)
    l_1.place(x=15,y=100)
    l_2 = Frame(frame_baixo,width=315,height=8)
    l_2.place(x=15,y=200)
    l_3 = Frame(frame_baixo,width=8,height=290)
    l_3.place(x=110,y=10)
    l_4 = Frame(frame_baixo,width=8,height=290)
    l_4.place(x=230,y=10)
    #imagens
    imagem_o = PhotoImage(file='img\icons8-circle-48.png')
    imagem_x = PhotoImage(file='img\icons8-close-48.png')
    #funcioes
    contador2 = 0
    contador3 = 0
    outro_contador = 0
    lista_jog = []
    lista_pc = []
    def icons(b):
        if b ==1:  
                b_1['image']=imagem_o
                b_1['width']=80
                b_1['height']=80     
                lista_jog.append(b)
        if b ==2:  
                b_2['image']=imagem_o
                b_2['width']=80
                b_2['height']=80 
                lista_jog.append(b)   
        if b ==3:  
                b_3['image']=imagem_o
                b_3['width']=80
                b_3['height']=80    
                lista_jog.append(b)
        if b ==4:  
                b_4['image']=imagem_o
                b_4['width']=80
                b_4['height']=80   
                lista_jog.append(b) 
        if b ==5:
                b_5['image']=imagem_o
                b_5['width']=80
                b_5['height']=80   
                lista_jog.append(b)  
        if b ==6:  
                b_6['image']=imagem_o
                b_6['width']=80
                b_6['height']=80
                lista_jog.append(b)    
        if b ==7:  
                b_7['image']=imagem_o
                b_7['width']=80
                b_7['height']=80    
                lista_jog.append(b)
        if b ==8:  
                b_8['image']=imagem_o
                b_8['width']=80
                b_8['height']=80 
                lista_jog.append(b)    
        if b ==9:  
                b_9['image']=imagem_o
                b_9['width']=80
                b_9['height']=80  
                lista_jog.append(b) 
        
    def desativar(k):
        if k ==1:
            b_1['state'] = tkinter.DISABLED
        if k ==2:
            b_2['state'] = tkinter.DISABLED
        if k ==3:
            b_3['state'] = tkinter.DISABLED
        if k ==4:
            b_4['state'] = tkinter.DISABLED
        if k ==5:
            b_5['state'] = tkinter.DISABLED
        if k ==6:
            b_6['state'] = tkinter.DISABLED
        if k ==7:
            b_7['state'] = tkinter.DISABLED
        if k ==8:
            b_8['state'] = tkinter.DISABLED
        if k ==9:
            b_9['state'] = tkinter.DISABLED
    def ganhador():
        pass
        
    def jogada_pc(n):
        botao = None
        numero = randint(1,9)
        if len(lista_jog) >= 5:
            return
        while True:
            if numero == n:    
                numero = randint(1,9)
            if numero in lista_pc:
                numero = randint(1,9)
            if numero in lista_jog:    
                numero = randint(1,9)
            else: break
        lista_pc.append(numero)
        if numero == 1:
            botao = b_1
        if numero == 2:
            botao = b_2
        if numero == 3:
            botao = b_3
        if numero == 4:
            botao = b_4
        if numero == 5:
            botao = b_5
        if numero == 6:
            botao = b_6
        if numero == 7:
            botao = b_7
        if numero == 8:
            botao = b_8
        if numero == 9:
            botao = b_9
        botao['image']=imagem_x
        botao['width']=80
        botao['height']=80  
        botao['state'] = tkinter.DISABLED

    def ganhador():
        global contador2
        global contador3
        if 1 in lista_jog:
            if 2 in lista_jog:
                if 3 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(4),desativar(5),desativar(6),desativar(7),desativar(8),desativar(9)
                    return
        if 1 in lista_jog:
            if 4 in lista_jog:
                if 7 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(2),desativar(3),desativar(5),desativar(6),desativar(8),desativar(9)
                    return
        if 4 in lista_jog:
            if 5 in lista_jog:
                if 6 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(7),desativar(8),desativar(9)
                    return
        if 7 in lista_jog:
            if 8 in lista_jog:
                if 9 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(4),desativar(5),desativar(6)
                    return
        if 2 in lista_jog:
            if 5 in lista_jog:
                if 8 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(3),desativar(4),desativar(6),desativar(7),desativar(9)
                    return
        if 3 in lista_jog:
            if 6 in lista_jog:
                if 9 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(5),desativar(7),desativar(8)
                    return
        if 1 in lista_jog:
            if 5 in lista_jog:
                if 9 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(2),desativar(3),desativar(4),desativar(6),desativar(7),desativar(8)
                    return
        if 3 in lista_jog:
            if 5 in lista_jog:
                if 7 in lista_jog:
                    frame_jogador_1['text']= 'GANHADOR'
                    frame_jogador_1['font'] = ('ivy 15')
                    frame_jogador_1.place(x=40,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(6),desativar(8),desativar(9)
                    return
            if 2 in lista_pc:
                if 3 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(4),desativar(5),desativar(6),desativar(7),desativar(8),desativar(9)
                    return
        if 1 in lista_pc:
            if 4 in lista_pc:
                if 7 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(2),desativar(3),desativar(5),desativar(6),desativar(8),desativar(9)
                    return
        if 4 in lista_pc:
            if 5 in lista_pc:
                if 6 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(7),desativar(8),desativar(9)
                    return
        if 7 in lista_pc:
            if 8 in lista_pc:
                if 9 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(3),desativar(4),desativar(5),desativar(6)
                    return
        if 2 in lista_pc:
            if 5 in lista_pc:
                if 8 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(3),desativar(4),desativar(6),desativar(7),desativar(9)
                    return
        if 3 in lista_pc:
            if 6 in lista_pc:
                if 9 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(5),desativar(7),desativar(8)
                    return
        if 1 in lista_pc:
            if 5 in lista_pc:
                if 9 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(2),desativar(3),desativar(4),desativar(6),desativar(7),desativar(8)
                    return
        if 3 in lista_pc:
            if 5 in lista_pc:
                if 7 in lista_pc:
                    frame_jogador_2['text']= 'GANHADOR'
                    frame_jogador_2['font'] = ('ivy 15')
                    frame_jogador_2.place(x=190,y=70)
                    desativar(1),desativar(2),desativar(4),desativar(6),desativar(8),desativar(9)
                    return
        
    #botoes
    b_1 = Button(frame_baixo,image=None,command=lambda:(icons(1),jogada_pc(1),desativar(1),ganhador()),width=11,height=5,bg=cinza)
    b_1.place(x=17,y=10)
    b_2 = Button(frame_baixo,image=None,command=lambda:(icons(2),jogada_pc(2),desativar(2),ganhador()),width=11,height=5,bg=cinza)
    b_2.place(x=17,y=111)
    b_3 = Button(frame_baixo,image=None,command=lambda:(icons(3),jogada_pc(3),desativar(3),ganhador()),width=11,height=5,bg=cinza)
    b_3.place(x=17,y=215)
    b_4 = Button(frame_baixo,image=None,command=lambda:(icons(4),jogada_pc(4),desativar(4),ganhador()),width=11,height=5,bg=cinza)
    b_4.place(x=130,y=10)
    b_5 = Button(frame_baixo,image=None,command=lambda:(icons(5),jogada_pc(5),desativar(5),ganhador()),width=11,height=5,bg=cinza)
    b_5.place(x=130,y=111)
    b_6 = Button(frame_baixo,image=None,command=lambda:(icons(6),jogada_pc(6),desativar(6),ganhador()),width=11,height=5,bg=cinza)
    b_6.place(x=130,y=215)
    b_7 = Button(frame_baixo,image=None,command=lambda:(icons(7),jogada_pc(7),desativar(7),ganhador()),width=11,height=5,bg=cinza)
    b_7.place(x=244,y=10)
    b_8 = Button(frame_baixo,image=None,command=lambda:(icons(8),jogada_pc(8),desativar(8),ganhador()),width=11,height=5,bg=cinza)
    b_8.place(x=244,y=111)
    b_9 = Button(frame_baixo,image=None,command=lambda:(icons(9),jogada_pc(9),desativar(9),ganhador()),width=11,height=5,bg=cinza)
    b_9.place(x=244,y=215)

janela.mainloop()