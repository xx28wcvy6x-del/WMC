# WMC · 3AAIF – Lösungen

Grundlage: die drei vorhandenen Lektionen im lokalen Ordner `GRG-WMC/3aaif`.
Die Unterrichtsübungen sind hier mit ihren erwarteten Ergebnissen erklärt. Eigene
Vorhersagen und die persönliche Vorführung im Unterricht bleiben Teil des Lernens.

## 1. Tooling & Git (2026-09-15)

### Vorhersage zur Hausübung
Nach dem ersten Commit meldet `git status` bei unveränderten Dateien einen sauberen
Arbeitsbaum („nothing to commit, working tree clean“). Wenn ein Remote und ein
Tracking-Branch eingerichtet sind, kann außerdem angezeigt werden, dass der lokale
Branch dem Remote um einen Commit voraus ist, bis `git push` ausgeführt wird.

### Jetzt du – drei Aufgaben
1. Nach `git init`: aktueller Branch, noch keine Commits. Ohne angelegte Dateien
   gibt es nichts zu committen; neue Dateien erscheinen als „untracked“.
2. Nach `git add index.html`, `git commit` und erfolgreichem `git push` zeigt GitHub
   die Datei und den neuen Commit. `add` merkt den Inhalt vor, `commit` speichert
   ihn lokal, `push` überträgt die Commits zum Remote.
3. Nach einer gespeicherten Änderung aktualisiert Live Server die Vorschau.
   Git meldet die bereits verfolgte Datei als „modified“; erst `git add` übernimmt
   diese Änderung in den nächsten Commit.

### Quiz
- 1: **B** – `git commit` schreibt den vorgemerkten Stand lokal fest.
- 2: **A** – Live Server zeigt die Seite lokal und lädt sie nach dem Speichern neu.
- 3: **C** – `git clone` kopiert das Repository einschließlich seiner Historie.
- 4: **B** – Name und E-Mail werden über `git config` eingerichtet.

## 2. HTML-Grundlagen (Ordner 2026-09-29)

### Vorhersage zur Hausübung
Die Seite braucht `header` für Titel und Einleitung, `nav` für die Navigation,
`main` für den Hauptinhalt, `article` für das Profil, `aside` für das Hobby und
`footer` für den Abschluss. Eine zusätzliche `section` mit eigener Überschrift
enthält das Schulprojekt; `figure` und `figcaption` verbinden Bild und Beschriftung.

### Umsetzung
`2026-09-29/index.html` enthält das HTML5-Grundgerüst, deutsche Sprache,
UTF-8, Viewport, Titel, die Überschrift „Über mich“, drei Navigationslinks,
drei einleitende Sätze im Artikel, eine Fähigkeitenliste, das Hobby und ein Bild
mit einer Beschreibung des sichtbaren Python-Codes. Das Bild nutzt einen relativen
Pfad und funktioniert nach dem Kopieren auf einen anderen Rechner.

### Jetzt du – drei Aufgaben
1. `header`, `main` und `aside` sind standardmäßig Blockelemente. Ihre Boxen
   erstrecken sich über die verfügbare Breite; DevTools zeigt Inhalt, Padding,
   Rahmen und Margin. In der fertigen Seite begrenzen CSS-Regeln die Breite.
2. Eine `nav` mit korrekt geschriebenen Links ist gültig. Die fertige Seite
   enthält interne Links auf vorhandene IDs.
3. Bei diesem informativen Bild würde ein fehlendes `alt` einen HTML-Fehler
   auslösen. Die fertige Abgabe behält das sinnvolle `alt`-Attribut.

### Quiz
- 1: **B** – Metadaten gehören in `head`.
- 2: **C** – Für diese Seite gibt es genau einen sichtbaren `main`-Bereich.
- 3: **A** – Semantische Tags beschreiben die Bedeutung des Inhalts.
- 4: **B** – `alt` liefert eine barrierefreie Bildbeschreibung.
- 5: **C** – Die Viewport-Angabe ermöglicht ein korrektes mobiles Layout.

## 3. CSS-Basics (Ordner 2026-10_XX)

### Vorhersage zur Hausübung
Bei `content-box` ist die Gesamtbreite einer Karte mit `width: 20rem`,
`padding: 1rem` und `border: 2px solid` gleich `22rem + 4px`.
Bei einer Wurzel-Schriftgröße von 16px sind das 356px.
Mit `border-box` sind Padding und Rahmen bereits in den 20rem enthalten:
Die Gesamtbreite beträgt dann 320px.

### Umsetzung
`2026-09-29/style.css` ist über `link` eingebunden. Es enthält Hintergrund-
und Textfarben, globales `box-sizing: border-box`, wiederverwendbare Klassen
wie `.karte`, Abstände in `rem` und den Überschriftenhintergrund
`rgba(109, 40, 217, 0.15)`. Bilder passen sich der verfügbaren Breite an.
Ein Media Query reduziert Abstände und Schriftgröße auf kleinen Bildschirmen.

### Jetzt du – drei Aufgaben
1. Bei normalen Autorregeln ohne `!important` gewinnt eine direkt am Element
   gesetzte Inline-Farbe gegen die Farbe einer Klasse im externen Stylesheet.
   `body` vererbt seine Farbe nur, wenn das Kind keine eigene Farbe erhält.
2. Mit `border-box` bleibt die beschriebene Karte insgesamt 20rem breit.
   Ohne diese Regel kommen die beiden Padding- und Rahmenanteile dazu.
3. Alpha 0.15 bedeutet 15 Prozent Deckkraft; der Hintergrund scheint durch.
   Alpha 1 bedeutet vollständige Deckkraft.

### Quiz
- 1: **B** – Externes Stylesheet über `link` im `head`.
- 2: **C** – `border-box` rechnet Padding und Rahmen in die Breite ein.
- 3: **A** – Alpha bezeichnet die Deckkraft.
- 4: **B** – Content → Padding → Border → Margin.
- 5: **C** – Klassen ermöglichen wiederverwendbares Styling.
