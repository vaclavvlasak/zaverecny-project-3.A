"""
projekt: projekt2
autor: Václav Vlasák
e-mail: vaclav.vlasak3@gmail.com

"""
from io import TextIOWrapper
import requests
from bs4 import BeautifulSoup
import argparse


def cela_url(url, href):
    if '/' in url:
        return url[:url.rfind('/')]+"/"+ href
    return url

def step_1(url, output_file):
    

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        cislo_radku = 0
        with open(output_file, 'w', encoding='cp1250') as f: 
            f.write("code;location;registered;envelopes;valid;")
            for row in rows:
                cells = row.find_all("td")
                
                if len(cells)>=2:
                    cislo_radku = cislo_radku + 1
                    cell1 = cells.pop(0)
                    cell2 = cells.pop(0)
                    links = cell1.find_all("a")
                    if len(links)>=1:
                        link1 = links.pop(0)
                        href = link1.get('href')
                        url2 = cela_url(url, href)
                        
                        zacatek_radku = (cell1.get_text()+";"+cell2.get_text())
                        step_2(url2, f, zacatek_radku, cislo_radku)
                        
    else:
        print("Chyba při získávání dat")

def step_2(url, f: TextIOWrapper, zacatek_radku, cislo_radku):
    

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        
        seznam_nazvu = []
        seznam_hlasu = []
        for row in rows:
            cells = row.find_all("td")
            
            if len(cells)==9:
                cell1 = cells.pop(3)
                cell2 = cells.pop(3)
                platny_hlasy = cells.pop(5)
                pokracovani_radku = (cell1.get_text()+";"+cell2.get_text()+";"+platny_hlasy.get_text())
            if len(cells)==5:
                nazev_strany = cells.pop(1)
                hlasy_pro_stranu = cells.pop(1)
                seznam_nazvu.append(nazev_strany.get_text())
                seznam_hlasu.append(hlasy_pro_stranu.get_text())
                #f.write(hlasy_pro_stranu.get_text()+";")
        if cislo_radku == 1:
            f.write(";".join(seznam_nazvu))
            f.write("\n")
        f.write(zacatek_radku+";"+pokracovani_radku+";")
        f.write(";".join(seznam_hlasu))    

        f.write("\n")

    else:
        print("Chyba při získávání dat")

def main(url, output_file):
    #url = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'předělat na prní argument programu
    step_1(url, output_file)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web scrapingovy script')
    parser.add_argument('url', type=str, help='URL of the website to scrape')
    parser.add_argument('output_file', type=str, help='Name of the output file')
    args = parser.parse_args()
    main(args.url, args.output_file)
