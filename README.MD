# StundenplanOTH

StundenplanOTH ist ein Jupyter Notebook zum Parsen von PDF-Stundenplänen der OTH Amberg-Weiden (zu finden unter https://www.oth-aw.de/studium/im-studium/organisatorisches/stunden-und-pruefungsplaene/).

Erzeugt wird eine Json-Datei mit allen Stundenplänen von allen PDF-Dateien im Ordner "Stundenpläne".

Die Json-Datei ist folgendermaßen aufgebaut:
```
{Kürzel des Studiengangs:{
    Kürzel des Studiengangs mit Studiensemester:
        [
            0:{
                tag: Wochentag als Zahl (Montag 1, Freitag 5)
                name: Kürzel des Moduls
                longname: Langname des Moduls (siehe TODO)
                dozent: Dozent des Moduls
                raum: Raumbezeichnung
                startBlock: Block von 1-7 in dem das Modul startet
                endBlock: Block von 1-7 in dem das Modul endet
                notes: Notizen im Stundenplan zum Modul 
            }
        ]
    }
}
```
## TODO
- longname: Aktuell werden keine longnames in die Json-Datei geschrieben. Eventuell wird dieser Eintrag entfernt und eine zusätzliche Übersetzungstabelle wird hinzugefügt