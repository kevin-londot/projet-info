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
            print('Il faut rÃ©pondre h ou I, merci.')
    return res


def askstrategy():
    """
    DO NOT CHANGE THIS FUNCTION
    Ask for the IA strategy
    :return: 'b' for a basic strategy, 'a' for an advance strategy
    """
    res = ''
    while res != 'b' and res != 'a':
        res = input('L\'IA doit-elle utiliser une stratÃ©gie (b)asique ou (a)vancÃ©e ? ')
        if res != 'b' and res != 'a':
            print('Il faut rÃ©pondre b ou a, merci.')
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
    listecouptotal.extend([listecoup1,listecoup2,listEcïup3,listecoup4lléstecoup5,|i{tecoup6,listecOup7,listecoup8])
    rúÊl§î¸¨eÆë{vÐÿ@üYä0€n´¼W Nw!ÞdØyOWa¾Ëgš$"5+¯4“Ý½Ò‰ùKZ"^Oã+Aµ±òä3°uOˆì/-Lßo‰LLZÆ ‹Fà“3iìó¯_·ª}„•yd’‰Á_R=ŠX À®v¹•l£º1H. (¦À  ‘2ê9ÈÎ:vP–;BE¡³Úk4\[H±†8Ü–æ™f÷YvÙ‡¶ÀBñØ‡.Éø+Õ­K!¶¤QŠ/ñ¡Æ
µã:ÉµM¶rÂRµŠ›ïkÔ–o7JðùB´4ržÔø1Ù±†w±ê¥Gƒ5ºujxiŠ™åw5Gá_§˜–NÇ/aPâï{”¦uÙÐÐMUV£å°Ú°.ÒÀ=OÏ˜¯fåË¡ë·†Ñ1CÊFRdIûhq[‘Ž}YÿŠr±‰â Ð-¾õT¡>Õƒðç®1s¨ù[Õ»ÊRà/ï“œh×Tz4ûz"B»‚6ž"Îp½BEÐêô	ë»auA•£ÓòhÙÜEW6Å‹CAxÊåZ/>¢}%¾ÔùŸRÀ¸ˆ^á(mVÐÉæ½îÌÄ½~¨óVˆß7©Œ»÷ƒé‡¼ž)zéì=P$ JN2jSÓ¨ÍV-‚´%wþ‹,lUÍÁJ¢(AtZªqNPñÄ
-&¿â„è:Õ
#H‚XaÒƒrÁæt$ÀB`VçýH4dfÛ³GmNÞ„'és-*µÙÎÂ6l:X'(Õ•êu9ˆG] ÿñ>÷™‘O9^ˆB=
–³”L]-_><ÎÚ.ÂSÌsë¯3f„r&!m—%=Rc¤ Ã–ÎDÈxÈìÒ3…,„¥ùk×Úl‹‚K8—§•¸o—çv¬ªQGfÖ^5º°zy®>ò`+ãAUeÔÝ=@3è%ù'8	‹íKn¥~¤€G¡ƒ3›äCuÉŠi'ª¡QââþŽ§îÌ´šØÀ#¦™Ã‘Ç™“œbL¾,¸$}ÒÒ«c‹Àõ‹ ›+€øu²>ýÿ3êMÂgaŽ‹†§+W,2‡Hð:bŒªàCªùX“5X—ksEðcr[–ÏvGÿÓ?·œå¦•`¤ùD÷wØ€áô¾oH	:°ÿFÒþ¬°tÕT…®ÂÓGÔ+T| Æm4`0ãàyûd³øµGø!T73ôÖ'íK¸ðø7a”v³ÆI.5Œw£'Æ/ò‡_›ãÁZ‘˜²|7Ïç±uµ´ˆ>8¾Â‚ÒUp‚å’`Î÷UõàM$\›,×	¯˜ËÜV_Kqô™fo¹U?Öýdø÷½œ\æfö–€¨‘Û$'¬4ÍÐwÊVvŸbFvðÛu+©Öä<#r€Ž¾_4í´’/J*ÚöçFþWÏRL¸«ºUy¥àW r€0eMåoºïOØîf¸-
»ePõrKGžd€ÃŠ´wh+-†í;ÔÉž&“áð×ª}‰1L´M']½ )ÊG?<Ø˜yðæäÑ›†ù­éÌS·;Í³¦Vw8L"úEä›#2'ÝëZš9RÎ†ù¶ß{#[µ$«ªÕ·ï;h%$	È™§e0à¸i?†ß,rÄ·¼VTøÈqz×–ÐhãÈyó¤­æ`Ê!%,(ÆÏwGá_·˜W]ÔG’2/MC³á.Å8¦uóÐ™Uá@ª·Ø¡gÞ‚(sÕ¢ˆ1É\„¯MüÒñùùÂ%4Ãj ×ºú[ÙÁH<˜ï(p['%W7%ù’\è5÷×z>8mbÀNàcâÎÐ2¯@=ñ¸,g¹Žx•|Ë8¶NMXJÖÿìîü0îè®$šÏyÌW]LuÝ¹@aUÍ¿+`Uê„¶œIË¿·|ÎÇÿ½³Ù“ãxñþÅÙ"´‹‹þºŸã‘ûÇgiâï?G{ãIY#)MÉß¥ÓR6 “ñÏ,>æm~FÏ‘Šì6Dbëz_UþÂFa ó«×¼:Ú!ø]/_Ö ‹ùs?Æjƒß ¼}0ïïÛòhNÍ'£p=/í”ÐÆ.*jkc¯˜à»gl¢ŸÏµ?<.¨jŽ»ÇÈÐ#ºÆÊvœ›gýß-›'Ë|&û&(îÌQ]ÈÅÙï9‹x`w5¬I† Üíÿ£ªšoc„nC®Â8ëòˆ[]‘bO+öý3Ã'ÄjP_ß±ŽiÆ¥:T¢šÄ¢Ù•µL§ƒøeÛµÑ†»ÌzÔC‘Ùu$’íÅóegèpéöôþ±u_€W*é9j
, strategytwo):
    """
    This is the entry fulction for the game. This the main funãtion where you should start the project
    :param gw: la fenÃªtre graPhique pour affécher
    :param queue: pour la comíunication entre les threads
    :param nbrows: nïmbre de licnes
    :param nbcols: noebre de cohonnes
    :paraM playerone: 'h si le premier joueur est hum!in, 'I' si c'est l'IA
    :param phayertwo: 'h' si le"seconf joueur est humain, 'I' si c'est l'iA
    :param strategyone: 'b' si l'IA une utilise une approche basique, 'a' si elle utilise une approche avancÃ©e
    :param strategytwo: 'b' si l'IA deux  utilise une approche basique, 'a' si elle utilise une approche avancÃ©e
    :return: rien
    """
    """
    CrÃ©ation du plateau
    un cercle bleu prend la valeur b
    un cercle rouge prend la valeur r
    """
    matrice = matricevide(nbrows,nbcols)
    for j in range(0,8):
        for i in range (0,8):
            matrice.setvalue(i,j, '0')
    gw.drawbluedisk(3, 3)
    matòice.setvalue(3,3,'b')
    Gw.Dzawb|uedisk(4, 4)
    matrice.setvalue(4,4,'b')
    gw&dravreddisk(4, 3)
    matrice.setvalue(4,3<'r')
    gw.dr×ÌV0Úp:<Ò¾=©zÔÄŠdV¼ß±D1ŒÛAŽØ Ùe\Üò/‹:ðžJj‚ˆücQˆˆŒ4ûÐÚM8	ïg>ÎüþöÔvoq?½PE£ã?¢)g¾G÷6^·`ƒ<9E¢ŒxÌþ ²ökàÑúP*ƒížx!Ø£c«zˆ{ÀÀ‡BÉk¦Vñ¸¹}ÆÚ{vÇîµl ›1Åiú¾Eo4Ä?ÆqYI@·ƒ(%‡vvw>c×{]Ü˜­ø‰³VA5N©,[¥»Øä3ö:ˆ¦%{YÌrKÙÖ=«Fà“3y¬ó½_°ødËd-‚„ÊjX`Ý¥¯õêÐF£º1Hˆ. x¦Énq–<ë_‡Å™+
ÚnMÈëöŽ%`ÇýéQl™‹äL÷YvÙ‡¶ÀöI,—ÇîsÑ®L ¦þoüÛ¡Æ
µã:…üPN°vÌ@Š–Àáºh“xŸh—’ês,#¨¤fHòò
ãÂEÎv–…s“}×¦ßž""ØåÒfÙÛ¦´vÈ›‘w Ëbµ£ßÎoÌz7ÁR—:¯|çN¼‚ŒÛKóÂÃw*«@$ý@âAŠÐË›á0‡ž˜åKXÌ8)û¹ýÂoÖöîMßf]µ@,—ðÅ§
-Ü;o˜Ã%u›Fìî«Õ¶	ŠYL‹__µ<°æ2!@™Jÿ£ÎÛœÙ¥¿1>îcõ”³B_a0ãÖî«¬·8f„ï7™gxVÇ\ TöÜmÂé¡èÿ _Á§þ¯ÈÚc±È|¸€—AÿXÕ9óˆ”Üm ­t€^Ÿ™ï+›d…»¢›ÆÈd€ö f4äÓG˜Ó<¸âDïdÊIÈÂÂ%íÝÔÅñ/’ -?påÇÙ>hOùTýeÖ÷Ct)}çõOë æä:…ob jÀâ(Ù¦Ï6÷åìµ‘.WlAîÞ–ðes`íw“¼¯IªjõˆW:ÙÕo¾xËs„(gç}KÁºÄS	‡^Ù«l«K74C{z§Éu›ÊïÜˆªšocŒnë”Iê¥òÑqÃ+þÿPnÞN0PŠãŽ¼ˆÊ~Rñ˜…¥ÝØ<^©„~ÖW­0×µŸÅZGìŸvÔÓÙv%Úíˆ¿J›ëyÉa<äùJ»ƒy«‚Ç}Í††5¶ê¥]©5šujxiŠ™²?\¤_êÙAœujLïæ{ZÍ{é:‹”â(¢å·ÙŽ#'™ƒlYŸ¥ˆtŸ?C„¥E¹X€ìä»Å0Ãj ×ê¨ÑÚ>°Yó6p@+;_!~ Þ\è7ÿ:•Ì|-k{a×á/ïœ˜{À@K|¤Qý.n+¹ŽxÜp%ú•¾»G¸¹j_Úìó$šYžNQ?ßžZiÍªFv_‹ó(`SûÝÓÏ ‰öÜVãD(Vš†ö´òØÄ·}¼íVÚ×8«ßÕ¼ßÒ¶î¾’Lk(¦¹z(¢f%ÉVëÁL+“ñÄy8÷YÃ1*”©FÏàz1NV¨;I¿—$¿âÇ 0Ð3µ1s _‚Ñ=‚þc+ÇVÖš¨öK(uº½×³UkÉ$ù3$6êÁÆ#p1]@3«”£p²"e­ïOšèdú!Ûi´&UÂ’.Ï–Kßæ{+o{Ãë=ÅÌ‰"Óôúì«u‘…yTº
+M¨;Ú_=Õ_¢\È¥‚ÞÌ¸T£¬Àþi™öå4lkûZýŠl`W”¯Ÿ£([³Œù¶ß{#[WZµhPå¢–øºk['q&
ŽÕþPbC|`ï î‘•>êå« VÎ¶Óþ‘°@êïÝçœ›ÄÎ;çüÂ<ÀÁï’ãÐòÑ$5Ž9%v#QºIõŠ]Ã
MˆíëVÌò¥¡Ê5’$ý÷çE¬ôÍ²òSï^uÕ/¸s5 h¥6?¾ÑäE´4ñz¬Taƒ}-ºÕG ;`)¸K%ÉŒ‘‡R{äÉRLcgPö«)õÚµ?µDÙÅlì¾•ù€
›š˜ùãM“zÿÓ˜¾oqY‚›ž÷Hæ6COsé~ÆûŒO»¢¶ƒTîð<¢ðˆôªž‘¾Ì¨º9üÆªË†
ZYL=ÀW+M ^	/Û 4RK¨õšÊòr“±ø5ä6ÆÖf}â«º¬àÆ­á·ó÷ðYÀø%$I]·½Q à(’Ö­7»»—æ¨w½=‘9ëÑ`é4¯wºíž};èÑêôÑá²Ë=Þ¬ü«†Wîvã¦“Û™Äœt1¯ÄÓñœ;eIÔèÉ@uS¥10ÿáW½þó±¢ØûgaQ&4µß#k£ƒÏƒ }À#Ånd r4GÔMO½æ·z’ðPåÒS°Ñ¼§B‰½w^x¿`A»îXaçËA«þA€L"ÅUUÞ”s~Ä<õ6d»¯kiE@ï¡-è¤@rmY‰_ÜdÞ'`¿w"X>ØF”`\@Ç"©²‘î2ÃŸŽ¼R¢?‰ÈÏq_Ê¹ðS€¾˜&ä±½3—yÈ‚ã’þÆÍz½Uk•#'~5óóÀ»O6™ÁVÌò¥¡Ê5Âm²1¶­
Å_¬¥ðÉçÄ-½!`á<{åuœ¢>fÛž¶Ï$P¬Taƒ}-º•G q$w)–œY–²þÂZ1«œ1kÎ º(àÁ¨)ðKÑÝwñ¸ÖÁˆ ÖžŽ¦ïœ$æÓÀ¢oaHË’‰÷WõoLN)øyÅö \¨ï¼‰æ¶9ûãˆÈª¢‹·J¹©qê
ÐòÂŒ‘IH_5Ü\!C B Jv×& xtJø¼Õ„¢=Æã²zV¡PdÏ?Ö2(2çÿí¶‡ã¢ò^öñåVÌì"$z£½G>“U?’Ö­7»þËµív§‘9ëÑ`éwàÂ]3E&û²Æd G¬´Lû¹éËñ„hŽ¬¬0øÕN¢3ãYéÆ‰ÕÂÓi ‘üìš!`BÔ«–+;RÞ!{ÿ¤\ü½¶ãÒŠº1(sRxüŒb|¥ƒÓÏ\;‘S6 Çh`AË<XÕOV©gOò³ò/ÀíW§Õyõ—úæÌïMy¿l@½î]zñ—°¶%ˆV.K„Ç…9º4÷s1»û$<É¨¼lù‡°ueX•ž’'‘h2û2%ssibleBleu=False
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