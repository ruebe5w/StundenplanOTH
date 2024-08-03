import pdfplumber


pdf=pdfplumber.open("EDU.pdf")
page = pdf.pages[0]
table=page.extract_table({
"vertical_strategy": "lines_strict", 
"horizontal_strategy": "lines_strict",})

class Vorlesung:
    spalte =0
    name=""
    longname=""
    dozent=""
    raum=""

    def __init__(self):
        self.spalte=[]

    def __str__(self):
        return " " + self.name+ " " + self.dozent+ " " + self.raum + " " +str(self.spalte)
vorlesungen=[]
continueFor=False
for column in range(1,6):
    for row in range(1,8):
        if continueFor:
            continueFor=False
            continue
        if table[row][column] !='':
            vl= Vorlesung()
            vl.name=table[row][column]
            vl.spalte=column
            if 'EMI' not in table[row][column] and 'MBUT' not in table[row][column]:
                spltStr=table[row+1][column].split()
                vl.dozent=spltStr[0]
                vl.raum=spltStr[1]
                continueFor=True
            vorlesungen.append(vl)

print(vorlesungen)
for vl in vorlesungen:
    print(vl)
    
    print('#')