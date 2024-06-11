Autor
V�clav Vlas�k
e-mail: vaclav.vlasak3@gmail.com

Popis
projekt2 je Python skript ur�en� pro web scraping dat z ur�it� webov� str�nky. Skript na��t� tabulkov� data zadan� URL, zpracov�v� je a ukl�d� do CSV souboru. Tento skript je navr�en pro zpracov�n� volebn�ch v�sledk�.

Instalace knihoven
K zaji�t�n� funk�nosti tohoto skriptu je nutn� nainstalovat n�sleduj�c� knihovny:

requests: Pro HTTP po�adavky
beautifulsoup4: Pro parsov�n� HTML
Knihovny lze nainstalovat pomoc� pip:

NAP�. pip install beautifulsoup4 
NEBO pip install -r requirements.txt

UK�ZKA: python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledek_volby.csv
