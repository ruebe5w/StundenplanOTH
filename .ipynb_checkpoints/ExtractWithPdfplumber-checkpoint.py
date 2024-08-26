import pdfplumber
from enum import Enum

pdf = pdfplumber.open("EDU.pdf")
page = pdf.pages[0]
table = page.extract_table(
    {
        "vertical_strategy": "lines_strict",
        "horizontal_strategy": "lines_strict",
    }
)

gridlines = [x for x in page.lines if x["width"] > 10 and x["width"] < 200]
tablelines = []
for i in range(len(gridlines)):
    if i > 0 and gridlines[i]["y0"] == gridlines[i - 1]["y0"]:
        continue
    tablelines.append(gridlines[i])


class Block(Enum):
    EINS = {"id": 1, "start": "08:00", "end": "09:30"}
    ZWEI = {"id": 2, "start": "09:45", "end": "11:15"}
    DREI = {"id": 3, "start": "11:30", "end": "13:00"}
    VIER = {"id": 4, "start": "13:45", "end": "15:15"}
    FUENF = {"id": 5, "start": "15:30", "end": "17:00"}
    SECHS = {"id": 6, "start": "17:15", "end": "18:45"}
    SIEBEN = {"id": 7, "start": "19:00", "end": "20:30"}
    ERROR = "Fehler in der Blockzuordnung!"

    def __str__(self) -> str:
        # print(self)
        if self == Block.ERROR:
            return self.value
        return str(self.value["id"])


class Wochentag:
    def __init__(self, nummer):
        self.nummer = nummer
        switch = {
            0: "Montag",
            1: "Dienstag",
            2: "Mittwoch",
            3: "Donnerstag",
            4: "Freitag",
        }
        self.wochentag = switch.get(nummer, 0)
        if self.wochentag == 0:
            raise ValueError(str(nummer) + " is not a valid number for class Tag!")

    def __str__(self) -> str:
        return self.wochentag


class Vorlesung:

    def __init__(self):
        self.tag = ""
        self.name = ""
        self.longname = ""
        self.dozent = ""
        self.raum = ""
        self.startBlock = ""
        self.endBlock = ""

    def __str__(self):
        return (
            " "
            + self.name
            + ". "
            + self.dozent
            + ". "
            + self.raum
            + ". "
            + str(self.tag)
            + ". "
            + str(self.startBlock)
            + "-"
            + str(self.endBlock)
        )


vorlesungen = []
continueFor = False
for column in range(1, 6):
    for row in range(1, 8):
        if continueFor:
            continueFor = False
            continue
        if table[row][column] != "":
            vl = Vorlesung()
            if "\n" in table[row][column]:
                spltStr = table[row][column].split()
                vl.name = spltStr[0]
                vl.dozent = spltStr[1]
                if len(spltStr) > 2:
                    vl.raum = spltStr[2]
            else:
                vl.name = table[row][column]
            vl.tag = Wochentag(column - 1)
            if "EMI" not in table[row][column] and "MBUT" not in table[row][column]:
                spltStr = table[row + 1][column].split()
                vl.dozent = spltStr[0]
                vl.raum = spltStr[1]
                continueFor = True
            vorlesungen.append(vl)


x = 110  # Montag
x = 248  # Dienstag
x = 385  # Mittwoch
x = 532  # Donnerstag
x = 661  # Freitag

blockCoord = {
    486: 1,  # Block1
    425: 2,  # Block2
    365: 3,  # Block3
    304: 4,  # Block4
    243: 5,  # Block5
    182: 6,  # Block6
}
wochentage = [[], [], [], [], []]


for line in tablelines:
    if 110 == round(line["x0"]):
        wochentage[0].append(blockCoord[round(line["y0"])])
    elif 248 == round(line["x0"]):
        wochentage[1].append(blockCoord[round(line["y0"])])
    elif 385 == round(line["x0"]):
        wochentage[2].append(blockCoord[round(line["y0"])])
    elif 532 == round(line["x0"]):
        wochentage[3].append(blockCoord[round(line["y0"])])
    elif 661 == round(line["x0"]):
        wochentage[4].append(blockCoord[round(line["y0"])])

for wochentagNummer in range(5):
    vlList = [vl for vl in vorlesungen if vl.tag.nummer == wochentagNummer]
    wochentage[wochentagNummer] = iter(wochentage[wochentagNummer])
    for i in range(len(vlList)):
        vlList[i].startBlock = list(Block)[next(wochentage[wochentagNummer], 0) - 1]
        vlList[i].endBlock = list(Block)[next(wochentage[wochentagNummer], 7) - 2]


# print(vorlesungen)
for vl in vorlesungen:
    print(vl)

    print("#")
