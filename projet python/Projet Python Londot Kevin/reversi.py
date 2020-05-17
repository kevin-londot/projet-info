from graphicalBoard import GraphicWindow
from threading import Thread
from queue import Queue
from array2d import Array2D
from random import randint

def askplayer(id):
    """
    DO NOT CHANGE THIS FUNCTION
    Ask for the nature of a player
    :param id: "rouge" or "bleu"
    :return:  'h' for a human player, 'I' for an IA player
    """
    res = ''
    while res != 'h' and res != 'I':
        res = input('Le joueur ' + str(id) + ' est-il (h)umain ou (I)A ? ')
        if res != 'h' and res != 'I':
            print('Il faut répondre h ou I, merci.')
    return res


def askstrategy():
    """
    DO NOT CHANGE THIS FUNCTION
    Ask for the IA strategy
    :return: 'b' for a basic strategy, 'a' for an advance strategy
    """
    res = ''
    while res != 'b' and res != 'a':
        res = input('L\'IA doit-elle utiliser une stratégie (b)asique ou (a)vancée ? ')
        if res != 'b' and res != 'a':
            print('Il faut répondre b ou a, merci.')
    return res


def fixparameters():
    """
    DO NOT CHANGE THIS FUNCTION
    fix the parameters
    :return: max pixels, number of rows, number of columns, playerone, playertwo, strategyone, strategytwo
    """
    nbmaxres = 1000
    nbrows = 8
    nbcols = 8
    playerone = askplayer('rouge')
    if playerone == 'I':
        strategyone = askstrategy()
    else:
        strategyone = ''
    playertwo = askplayer('bleu')
    if playertwo == 'I':
        strategytwo = askstrategy()
    else:
        strategytwo = ''

    return nbmaxres, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo


def run():
    """
    DO NOT CHANGE THIS FUNCTION
    Fix the size of the board, set the players, creates the graphical board, create the communication channel
     between the threads and launch the game
    :return: nothing
    """
    nbmaxres, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo = fixparameters()

    queue = Queue()

    gw = GraphicWindow(nbmaxres, nbrows, nbcols, queue)

    gamethread = Thread(target=game, args=(gw, queue, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo))
    gamethread.daemon = True
    gamethread.start()

    gw.draw()


def waitformouseclick(queue):
    """
    DO NOT CHANGE THIS FUNCTION
    Wait for a mouse click on the graphical board and return the coordinate
    :param queue: event queue
    :return: tuple (x, y) with x the line number and y the column number
    """
    return queue.get()
    
def matricevide(nbrows,nbcols):
    matrice = Array2D(nbrows,nbcols)
    return matrice  
def testposibilitehautgauche(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cpti=1
    cptj=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i-cpti,j-cptj)==True :
        if matrice.getvalue(i-cpti,j-cptj) ==adversaire:
            listtempsjoueur.append((i-cpti,j-cptj))
            cpti=cpti+1
            cptj=cptj+1
        elif matrice.getvalue(i-cpti,j-cptj) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i-cpti+1, j-cptj+1)
                        gw.drawreddisk(i-cpti+1,j-cptj+1)
                        matrice.setvalue(i-cpti+1,j-cptj+1,'r')
                        cpti=cpti-1
                        cptj=cptj-1
                elif joueur=='b':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i-cpti+1, j-cptj+1)
                        gw.drawbluedisk(i-cpti+1,j-cptj+1)
                        matrice.setvalue(i-cpti+1,j-cptj+1,'b')
                        cpti=cpti-1
                        cptj=cptj-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i-cpti,j-cptj) =='0' and matrice.getvalue(i-cpti+1,j-cptj+1)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i-cpti,j-cptj)
                    matrice.setvalue(i-cpti,j-cptj,'j')
                    listecasejaune.append((i-cpti,j-cptj))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i-cpti,j-cptj)
                    matrice.setvalue(i-cpti,j-cptj,'v')
                    listecaseverte.append((i-cpti,j-cptj))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i-cpti,j-cptj)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i-cpti,j-cptj)
                matrice.setvalue(i-cpti,j-cptj,'j')
            if joueur=='b':
                gw.drawgreensquare(i-cpti,j-cptj)
                matrice.setvalue(i-cpti,j-cptj,'v')
        else:
            casevide=True
def testposibilitehaut(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cpti=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i-cpti,j)==True :
        if matrice.getvalue(i-cpti,j) ==adversaire:
            listtempsjoueur.append((i-cpti,j))
            cpti=cpti+1
        elif matrice.getvalue(i-cpti,j) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cpti>0  :
                        gw.drawwhitesquare(i-cpti+1, j)
                        gw.drawreddisk(i-cpti+1,j)
                        matrice.setvalue(i-cpti+1,j,'r')
                        cpti=cpti-1
                elif joueur=='b':
                    while cpti>0  :
                        gw.drawwhitesquare(i-cpti+1, j)
                        gw.drawbluedisk(i-cpti+1,j)
                        matrice.setvalue(i-cpti+1,j,'b')
                        cpti=cpti-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i-cpti,j) =='0' and matrice.getvalue(i-cpti+1,j)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i-cpti,j)
                    matrice.setvalue(i-cpti,j,'j')
                    listecasejaune.append((i-cpti,j))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i-cpti,j)
                    matrice.setvalue(i-cpti,j,'v')
                    listecaseverte.append((i-cpti,j))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i-cpti,j)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i-cpti,j)
                matrice.setvalue(i-cpti,j,'j')
            if joueur=='b':
                gw.drawgreensquare(i-cpti,j)
                matrice.setvalue(i-cpti,j,'v')
        else:
            casevide=True
def testposibilitehautdroite(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cpti=1
    cptj=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i-cpti,j+cptj)==True :
        if matrice.getvalue(i-cpti,j+cptj) ==adversaire:
            listtempsjoueur.append((i-cpti,j+cptj))
            cpti=cpti+1
            cptj=cptj+1
        elif matrice.getvalue(i-cpti,j+cptj) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i-cpti+1, j+cptj-1)
                        gw.drawreddisk(i-cpti+1,j+cptj-1)
                        matrice.setvalue(i-cpti+1,j+cptj-1,'r')
                        cpti=cpti-1
                        cptj=cptj-1
                elif joueur=='b':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i-cpti+1, j+cptj-1)
                        gw.drawbluedisk(i-cpti+1,j+cptj-1)
                        matrice.setvalue(i-cpti+1,j+cptj-1,'b')
                        cpti=cpti-1
                        cptj=cptj-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i-cpti,j+cptj) =='0' and matrice.getvalue(i-cpti+1,j+cptj-1)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i-cpti,j+cptj)
                    matrice.setvalue(i-cpti,j+cptj,'j')
                    listecasejaune.append((i-cpti,j+cptj))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i-cpti,j+cptj)
                    matrice.setvalue(i-cpti,j+cptj,'v')
                    listecaseverte.append((i-cpti,j+cptj))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i-cpti,j+cptj)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i-cpti,j+cptj)
                matrice.setvalue(i-cpti,j+cptj,'j')
            if joueur=='b':
                gw.drawgreensquare(i-cpti,j+cptj)
                matrice.setvalue(i-cpti,j+cptj,'v')
        else:
            casevide=True
def testposibilitegauche(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cptj=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i,j-cptj)==True :
        if matrice.getvalue(i,j-cptj) ==adversaire:
            listtempsjoueur.append((i,j-cptj))
            cptj=cptj+1
        elif matrice.getvalue(i,j-cptj) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cptj>0 :
                        gw.drawwhitesquare(i, j-cptj+1)
                        gw.drawreddisk(i,j-cptj+1)
                        matrice.setvalue(i,j-cptj+1,'r')
                        cptj=cptj-1
                elif joueur=='b':
                    while cptj>0 :
                        gw.drawwhitesquare(i, j-cptj+1)
                        gw.drawbluedisk(i,j-cptj+1)
                        matrice.setvalue(i,j-cptj+1,'b')
                        cptj=cptj-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i,j-cptj) =='0' and matrice.getvalue(i,j-cptj+1)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i,j-cptj)
                    matrice.setvalue(i,j-cptj,'j')
                    listecasejaune.append((i,j-cptj))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i,j-cptj)
                    matrice.setvalue(i,j-cptj,'v')
                    listecaseverte.append((i,j-cptj))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i,j-cptj)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i,j-cptj)
                matrice.setvalue(i,j-cptj,'j')
            if joueur=='b':
                gw.drawgreensquare(i,j-cptj)
                matrice.setvalue(i,j-cptj,'v')
        else:
            casevide=True
def testposibilitedroite(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cptj=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i,j+cptj)==True :
        if matrice.getvalue(i,j+cptj) ==adversaire:
            listtempsjoueur.append((i,j+cptj))
            cptj=cptj+1
        elif matrice.getvalue(i,j+cptj) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cptj>0 :
                        gw.drawwhitesquare(i, j+cptj-1)
                        gw.drawreddisk(i,j+cptj-1)
                        matrice.setvalue(i,j+cptj-1,'r')
                        cptj=cptj-1
                elif joueur=='b':
                    while cptj>0 :
                        gw.drawwhitesquare(i, j+cptj-1)
                        gw.drawbluedisk(i,j+cptj-1)
                        matrice.setvalue(i,j+cptj-1,'b')
                        cptj=cptj-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i,j+cptj) =='0' and matrice.getvalue(i,j+cptj-1)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i,j+cptj)
                    matrice.setvalue(i,j+cptj,'j')
                    listecasejaune.append((i,j+cptj))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i,j+cptj)
                    matrice.setvalue(i,j+cptj,'v')
                    listecaseverte.append((i,j+cptj))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i,j+cptj)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i,j+cptj)
                matrice.setvalue(i,j+cptj,'j')
            if joueur=='b':
                gw.drawgreensquare(i,j+cptj)
                matrice.setvalue(i,j+cptj,'v')
        else:
            casevide=True
def testposibilitebasgauche(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cpti=1
    cptj=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i+cpti+1,j-cptj)==True :
        if matrice.getvalue(i+cpti,j-cptj) ==adversaire:
            listtempsjoueur.append((i+cpti,j-cptj))
            cpti=cpti+1
            cptj=cptj+1
        elif matrice.getvalue(i+cpti,j-cptj) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i+cpti-1, j-cptj+1)
                        gw.drawreddisk(i+cpti-1,j-cptj+1)
                        matrice.setvalue(i+cpti-1,j-cptj+1,'r')
                        cpti=cpti-1
                        cptj=cptj-1
                elif joueur=='b':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i+cpti-1, j-cptj+1)
                        gw.drawbluedisk(i+cpti-1,j-cptj+1)
                        matrice.setvalue(i+cpti-1,j-cptj+1,'b')
                        cpti=cpti-1
                        cptj=cptj-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i+cpti,j-cptj) =='0' and matrice.getvalue(i+cpti-1,j-cptj+1)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i+cpti,j-cptj)
                    matrice.setvalue(i+cpti,j-cptj,'j')
                    listecasejaune.append((i+cpti,j-cptj))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i+cpti,j-cptj)
                    matrice.setvalue(i+cpti,j-cptj,'v')
                    listecaseverte.append((i+cpti,j-cptj))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i+cpti,j-cptj)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i+cpti,j-cptj)
                matrice.setvalue(i+cpti,j-cptj,'j')
            if joueur=='b':
                gw.drawgreensquare(i+cpti,j-cptj)
                matrice.setvalue(i+cpti,j-cptj,'v')
        else:
            casevide=True
def testposibilitebas(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cpti=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i+cpti,j)==True :
        if matrice.getvalue(i+cpti,j) ==adversaire :
            listtempsjoueur.append((i+cpti,j))
            cpti=cpti+1
        elif matrice.getvalue(i+cpti,j) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cpti>0  :
                        gw.drawwhitesquare(i+cpti-1,j)
                        gw.drawreddisk(i+cpti-1,j)
                        matrice.setvalue(i+cpti-1,j,'r')
                        cpti=cpti-1
                elif joueur=='b':
                    while cpti>0  :
                        gw.drawwhitesquare(i+cpti-1,j)
                        gw.drawbluedisk(i+cpti-1,j)
                        matrice.setvalue(i+cpti-1,j,'b')
                        cpti=cpti-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i+cpti,j) =='0' and matrice.getvalue(i+cpti-1,j)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i+cpti,j)
                    matrice.setvalue(i+cpti,j,'j')
                    listecasejaune.append((i+cpti,j))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i+cpti,j)
                    matrice.setvalue(i+cpti,j,'v')
                    listecaseverte.append((i+cpti,j))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i+cpti,j)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i+cpti,j)
                matrice.setvalue(i+cpti,j,'j')
            if joueur=='b':
                gw.drawgreensquare(i+cpti,j)
                matrice.setvalue(i+cpti,j,'v')
        else:
            casevide=True
def testposibilitebasdroite(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    casevide=False
    listtempsjoueur=[]
    pionjoueur=False
    cpti=1
    cptj=1
    while casevide==False and pionjoueur==False and matrice.isvalue(i+cpti,j+cptj)==True :
        if matrice.getvalue(i+cpti,j+cptj) ==adversaire:
            listtempsjoueur.append((i+cpti,j+cptj))
            cpti=cpti+1
            cptj=cptj+1
        elif matrice.getvalue(i+cpti,j+cptj) ==joueur:
            if pionajoute==True:
                if joueur=='r':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i+cpti-1, j+cptj-1)
                        gw.drawreddisk(i+cpti-1,j+cptj-1)
                        matrice.setvalue(i+cpti-1,j+cptj-1,'r')
                        cpti=cpti-1
                        cptj=cptj-1
                elif joueur=='b':
                    while cpti>0 and cptj>0 :
                        gw.drawwhitesquare(i+cpti-1, j+cptj-1)
                        gw.drawbluedisk(i+cpti-1,j+cptj-1)
                        matrice.setvalue(i+cpti-1,j+cptj-1,'b')
                        cpti=cpti-1
                        cptj=cptj-1
                pionjoueur=True
            elif pionajoute==False:
                pionjoueur=True
        elif matrice.getvalue(i+cpti,j+cptj) =='0' and matrice.getvalue(i+cpti-1,j+cptj-1)==adversaire and matrice.getvalue(i,j)==joueur:
            casevide=True
            if pionajoute==False:
                if joueur=='r':
                    gw.drawyellowsquare(i+cpti,j+cptj)
                    matrice.setvalue(i+cpti,j+cptj,'j')
                    listecasejaune.append((i+cpti,j+cptj))
                    return listechgtpionpourjoueur
                elif joueur=='b':
                    gw.drawgreensquare(i+cpti,j+cptj)
                    matrice.setvalue(i+cpti,j+cptj,'v')
                    listecaseverte.append((i+cpti,j+cptj))
                    listechgtpionpourjoueur.append(listtempsjoueur)
                    return listechgtpionpourjoueur
        elif matrice.getvalue(i,j) ==joueur and matrice.getvalue(i+cpti,j+cptj)=='0':
            if joueur=='r':
                gw.drawyellowsquare(i+cpti,j+cptj)
                matrice.setvalue(i+cpti,j+cptj,'j')
            if joueur=='b':
                gw.drawgreensquare(i+cpti,j+cptj)
                matrice.setvalue(i+cpti,j+cptj,'v')
        else:
            casevide=True
def effacerPrevisualisation(gw,matrice):
    for j in range(0,8):
        for i in range(0,8):
            if matrice.getvalue(i,j)== 'j'or matrice.getvalue(i,j)== 'v':
                gw.drawwhitesquare(i, j)
                matrice.setvalue(i,j,'0')
def testtourpossiblerouge(matrice):
    for i in range(0,8):
        for j in range(0,8):
            if  matrice.getvalue(i,j)== 'j'  :
                return True
def testtourpossiblebleu(matrice):
    for i in range(0,8):
        for j in range(0,8):
            if  matrice.getvalue(i,j)== 'v'  :
                return True
                
def testposibilitetotale(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur):
    listecouptotal=[]
    listecoup1=testposibilitehautgauche(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
    listecoup2=testposibilitehaut(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
    listecoup3=testposibilitehautdroite(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
    listecoup4=testposibilitegauche(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
    listecoup5=testposibilitedroite(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
    listecoup6=testposibilitebasgauche(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
    listecoup7=testposibilitebas(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechg4pIonpourjoueur)
    listecoup8=testposibilmtebasdroite(gW,i,j,matrice,joueur,!dversaire,pionajoute,listecasevertellistecasejaune,listechgtpionpourjoueur)
    listecouptotal.extend([listecoup1,listecoup2,listEc�up3,listecoup4ll�stecoup5,|i{tecoup6,listecOup7,listecoup8])
    r��l��e��{v��@�Y�0�n��W Nw!�d�yOWa��g�$"5+�4���҉�KZ"^O�+A����3�uO��/-L�o�LLZƝ �F��3i��_��}��yd���_R=�X���v��l��1H. (��  �2��9�Ώ:vP�;BE����k4\�[H��8ܖ�f�Y�vه��B�؇.���+խK!��Q�/��
��:ɵM�r�R����kԖo7J��B��4r���1ٱ�w��G�5�ujxi���w5G�_���N�/aP��{��u���MUV��ڰ.��=OϘ�f�ˡ���1C�FRdI�hq[��}Y��r����-��T�>Ճ��1s��[ջ�R�/h�Tz4�z"B��6�"�p�BE���	�auA����h���EW6ŋCAx��Z/>��}%����R���^�(mV�����Ľ~��V��7������釼�)z��=P$�JN2jS���V-���%w��,lU��J��(AtZ�qNP��
-&���:�
#H�Xa҃r��t$�B`V��H4df۳GmNބ'�s-*����6l:X'(Օ�u9�G] ��>���O9^�B=
���L]-_><��.�S�s�3f�r&!m�%=Rc� Ö�D�x���3�,����k��l��K8����o��v��QG�f�^5��zy�>�`+�AUe��=@3�%�'8	��Kn�~��G��3��CuɊi'��Q������̴���#���ÑǙ��bL�,�$}�ҫc������+��u�>��3�M�ga����+W,2�H�:b���C��X��5X�ksE�cr[��vG��?��妕`��D�w؀���oH	:��F����t�T���ӝG�+T| �m4`0��y��d���G�!T73��'�K���7a�v��I.5��w�'�/�_���Z���|7��u���>8��Up��`��U��M$\�,�	����V_Kq��fo�U?��d����\�f������$'�4��w�Vv�bFv��u+���<#r���_4�/J*���F�W�RL���Uy��W�r�0eM�o��O��f�-
�eP�rK�G�d����wh+-��;�ɞ&���ת}��1L�M']� )�G?<���y���ћ�����S�;ͳ�Vw8L"�E�#2'��Z��9RΆ���{#[�$��շ�;h%$	ș�e0��i?��,rķ�VT��qzז�h���y��`�!%,(Ɛ�wG�_��W]�G�2/MC��.�8�u�ЙU�@��ءgނ(sբ�1�\��M������%4�j�׺�[��H<��(p['%W7%��\�5���z>8mb�N�c���2�@=��,g��x�|�8�NMXJ�����0�讝$���y�W]Luݹ@aUͿ+`Uꄶ�I˿��|�����ٓ�x����"���������gi��?G{�IY#)M�ߥ�R6 ���,>��m~Fϑ��6Db�z_U��Fa �׼:�!�]/_�� ��s?�j�ߠ�}0����hN��'�p=/���.*jkc����gl��ϵ?<.�j�����#���v��g��-�'�|&�&(���Q]����9�x`w5�I� ܏�����oc�nC��8��[]�bO+��3�'��jP_߱�iƥ:T��Ģٕ�L����e۵ц��z�C��u$�����eg�p�����u_�W*�9j
, strategytwo):
    """
    This is the entry fulction for the game. This the main fun�tion where you should start the project
    :param gw: la fenêtre graPhique pour aff�cher
    :param queue: pour la com�unication entre les threads
    :param nbrows: n�mbre de licnes
    :param nbcols: noebre de cohonnes
    :paraM playerone: 'h si le premier joueur est hum!in, 'I' si c'est l'IA
    :param phayertwo: 'h' si le"seconf joueur est humain, 'I' si c'est l'iA
    :param strategyone: 'b' si l'IA une utilise une approche basique, 'a' si elle utilise une approche avancée
    :param strategytwo: 'b' si l'IA deux  utilise une approche basique, 'a' si elle utilise une approche avancée
    :return: rien
    """
    """
    Création du plateau
    un cercle bleu prend la valeur b
    un cercle rouge prend la valeur r
    """
    matrice = matricevide(nbrows,nbcols)
    for j in range(0,8):
        for i in range (0,8):
            matrice.setvalue(i,j, '0')
    gw.drawbluedisk(3, 3)
    mat�ice.setvalue(3,3,'b')
    Gw.Dzawb|uedisk(4,�4)
    matrice.setvalue(4,4,'b')
    gw&dravreddisk(4, 3)
    matrice.setvalue(4,3<'r')
    gw.dr��V0�p:<Ҿ=�z�ĊdV�߱D1��A�؁��e\��/�:��Jj���cQ���4���M8	�g>�����voq?�PE��?�)g�G�6^�`�<9�E��x̐� ��k���P*���x!أc�z�{���B�k��V�}��{v���l �1�i��Eo4�?�qYI@��(%�vvw>c�{]ܘ����VA5N�,[����3�:��%{Y�r�K��=�F��3y��_��dˏd-���jX`������F��1H�. x��nq�<��_�ř+
�nM����%`���Ql����L�Y�vه���I�,���sѮL ��o�ۡ�
��:��PN�v�@����h�x�h���s,#��fH��
��E�v��s�}צ��""���f�ۦ�vț�w �b����o�z7��R�:�|�N����K���w*�@$�@�A��˛�0����KX�8)����o���M�f]�@�,��ŧ
-�;o��%u�F��ն�	��YL�__�<��2!@�J�����٥�1>�c���B_a0������8f��7�gxV�\ T��m����� _������c��|���A�X�9��m���t�^���+�d������d���f4�ӁG��<��D�d�I���%�����/� -?p��ٍ>hO�T�e��Ct)}��O� ��:�ob�j��(���6�����.WlA�ޖ�es`�w����I�j��W:��o��x�s�(g�}K���S	��^٫l�K74C{z��u���܈��oc�n�I���q�+��P�n�N�0P�㎼��~R񘅥��<^��~�W�0׵��ZG�v���v%�툿J��yɍa<��J��y����}͆�5��]�5�ujxi���?\�_���A�ujL��{Z�{�:���(��َ#'��lY���t�?C��E�X�����0�j�����>�Y�6p@+;_!~��\�7�:��|-k{a��/{�@K|�Q�.n+��x�p�%����G��j_���$��Y�NQ?ߞZiͪFv_��(`S���� ���V�D(V������ķ}��V��8��ռ�ҶLk(��z(�f%�V��L+���y8�Y�1*��F��z1NV�;I��$��Ǡ0�3�1s _��=��c+�V֚��K(u��׳Uk��$�3$6���#p1]@3���p�"e��O��d�!�i�&U��.ϖK��{+o{��=�̉"����u��yT�
+M�;�_=�_��\ȏ���̸T����i���4lk�Z��l`W����([�����{#[WZ�hP墖��k['q&
���PbC|`���>����Vζ����@���眛��;���<�������$5�9%v#Q�I��]�
M���V���5�$���E���͝��S�^u�/�s5�h��6?���E�4�z�Ta�}-��G� ;`)��K%Ɍ��R{��RLcg�P��)�ڵ?�D��l����
�����M�z�Ә�oqY�����H�6COs�~���O����T��<��������̨�9�ƪˆ
ZYL=�W+M ^	/� 4RK�����r���5�6��f}⫺��ƭ����Y��%$I]��Q �(�֭7����w�=�9��`�4��w��};�������=ެ���W�v�����Ĝt1����;eI���@uS�10��W�����gaQ&4��#k��σ }�#�nd�r�4G�MO��z��P��S�Ѽ�B��w^x�`A��Xa��A��A�L"�UUޔs~�<�6d��kiE�@�-萤@rmY�_ܐd�'`�w"X>�F�`\@�"����2ß��R�?���q_ʹ�S���&䱽3�yȂ����z�Uk�#'~5����O6���V���5�m�1��
�_������-�!�`�<{�u��>f۞��$�P�Ta�}-��G� q$w)��Y����Z1��1k���(���)�K��w���� ֞����$����oaH˒���W�oLN)�y���\�����9���Ȫ���J��q�
���IH_5�\!C B Jv�& xtJ��Մ�=��zV�Pd�?�2(2�����^���V��"$z��G>�U?�֭7��˵�v��9��`�w��]3E&���d G��L�����h���0��N�3�Y�Ɖ���i ����!`Bԫ�+;R�!{��\����Ҋ�1(sRx��b|����\;�S6 �h`A�<X�OV�gO��/��W��y������My�l@��]z���%�V.K�ǅ9�4�s1��$<���l���ueX���'�h2�2%ssibleBleu=False
        for j in range(0,8):
            for i in range(0,8):
                testposibilitetotale(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
        tourpossibleBleu=testtourpossiblebleu(matrice)
        if tourpossibleBleu==True:
            if playertwo=='h':
                print("Cliquez sur une case verte")
                coord = waitformouseclick(queue)
                while matrice.getvalue(coord[0],coord[1])!= 'v'  :
                    print("Coup impossible, Cliquer sur une case verte")
                    coord = waitformouseclick(queue)
            elif playertwo=='I':
                if strategytwo =='b':
                    choixIA=IAapprochebasique(joueur,adversaire,listecaseverte,listecasejaune)
                    tuplealeatoire=listecaseverte[choixIA]
                    coord=[(1,1),(1,1)]
                    coord[0]=tuplealeatoire[0]
                    coord[1]=tuplealeatoire[1]
                elif strategyone=='a':
                    y=IAavancee(joueur,adversaire,matrice,listecaseverte,listecasejaune,tupleavance,i,j,gw,pionajoute,listechgtpionpourjoueur)
                    tupleavance=listecaseverte[y]
                    coord=[(1,1),(1,1)]
                    coord[0]=tupleavance[0]
                    coord[1]=tupleavance[1]
            effacerPrevisualisation(gw,matrice)
            gw.drawbluedisk(coord[0], coord[1])
            matrice.setvalue(coord[0],coord[1],'b')
            pionajoute=True
            i=coord[0]
            j=coord[1]
            testposibilitetotale(gw,i,j,matrice,joueur,adversaire,pionajoute,listecaseverte,listecasejaune,listechgtpionpourjoueur)
            pionajoute=False
        else :
            print("Pas de coup possible pour le joueur bleu")
        effacerPrevisualisation(gw,matrice)
    print("fin du jeu")
    findujeu(matrice)
# Start the game
# DO NOT CHANGE THIS INSTRUCTION
run()