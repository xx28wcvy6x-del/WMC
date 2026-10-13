# WMC-Hausübungen · 3AAIF

## Fertige Dateien

- `2026-09-29/index.html`: vollständige „Über mich“-Seite mit semantischem HTML.
- `2026-09-29/style.css`: CSS-Basics-Aufgabe auf derselben Seite umgesetzt.
- `2026-09-29/images/schulprojekt.png`: vorhandener Screenshot mit portablem Pfad.
- `LOESUNGEN.md`: Vorhersagen, Erklärungen der Übungen und Quizlösungen aller drei Lektionen.
- `PRUEFUNG.md`: Ergebnisse der tatsächlichen Überprüfung.

HTML und CSS werden als aufeinander aufbauende Aufgaben im bestehenden
Hausübungsordner geführt. Die CSS-Lektion hat im Kurs noch kein genaues Datum
(`2026-10_XX`); deshalb wurde kein Abgabedatum erfunden.

## Lokal öffnen

In VS Code den Ordner `WMC` öffnen, dann
`HÜS/2026-09-29/index.html` mit Live Server starten.
Alternativ im Terminal des Ordners `WMC`:

```sh
python3 -m http.server 5500 --bind 127.0.0.1
```

Danach `http://127.0.0.1:5500/H%C3%9CS/2026-09-29/` öffnen.
Der Python-Server lädt bei Änderungen nicht automatisch neu; dazu im Browser
neu laden. Live Server bietet das automatische Neuladen.

## Setup- und Abgabecheckliste

Am 13.10.2026 tatsächlich geprüft:

- [x] Git verfügbar; WMC ist ein vorhandenes Repository mit Commits.
- [x] Kursrepository GRG-WMC ist lokal vorhanden.
- [x] WMC-Remote: https://github.com/xx28wcvy6x-del/WMC.git
- [x] Git-Name und Git-E-Mail sind bereits konfiguriert.
- [x] VS Code vorhanden.
- [x] W3C Web Validator-Erweiterung vorhanden (`celianriboulet.webvalidator`).
- [x] HTML-Aufgabe umgesetzt und lokal mit dem Nu HTML Checker geprüft.
- [x] CSS-Aufgabe umgesetzt und mit dem W3C CSS-Validator geprüft.
- [x] Vorschau im Browser und Prüfung bei Desktop- und Handybreite.
- [ ] Live Server-Erweiterung installieren (in der Erweiterungsliste nicht gefunden).
- [ ] OpenCode-Verfügbarkeit prüfen/installieren (nicht im aktuellen Suchpfad gefunden).
- [ ] Setup persönlich im Unterricht vorführen.
- [ ] Prüfen, ob das GitHub-Repository öffentlich ist.
- [ ] Hausübungen committen und zu GitHub pushen.
- [ ] Repo-Link an grafg@spengergasse.at senden, falls noch nicht geschehen.

Die öffentliche GitHub-Abgabe und die E-Mail wurden nicht ausgeführt.
Die Seite enthält die im bisherigen HTML vorhandenen persönlichen Daten,
insbesondere das Geburtsdatum. Vor einer öffentlichen Abgabe den Inhalt prüfen.
Die bestehende Datei `experement/graph.py` gehört nicht zu dieser Hausübung.

## Gezielte Abgabe

Im Terminal des Ordners `WMC`, sobald die Veröffentlichung freigegeben ist:

```sh
git add -- 'HÜS'
git commit -m "Complete 3AAIF HTML and CSS homework"
git push origin main
```

## Mailentwurf

Empfänger: grafg@spengergasse.at

Betreff: WMC 3AAIF – Repository Kaurav Gill

Sehr geehrter Herr Graf,

hier ist der Link zu meinem WMC-Repository:
https://github.com/xx28wcvy6x-del/WMC

Meine Hausübungen befinden sich im Ordner HÜS.

Mit freundlichen Grüßen
Kaurav Gill
