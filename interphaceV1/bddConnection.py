import sqlite3

class bddRequest:

    conn = None
    cur = None
    @staticmethod
    def initDatabase():
        global conn, cur
        conn = sqlite3.connect('bddPatient.db')
        cur = conn.cursor()

    @staticmethod
    def getPatientInfo(nom):
        global conn, cur
        cur.execute("SELECT nom,prenom FROM personne where nom='"+nom+"'")
        patient = cur.fetchall()
        conn.commit()
        return patient[0]

    @staticmethod
    def getDoctors():
        global conn, cur
        cur.execute("SELECT user,password FROM compte")
        compte = cur.fetchall()
        conn.commit()
        return compte

    @staticmethod
    def endDatabase():
        global conn, cur
        cur.close()
        conn.close()