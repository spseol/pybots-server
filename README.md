Pybots -- server 
====================

[![Build Status](https://travis-ci.org/spseol/pybots-server.svg?branch=master)](https://travis-ci.org/spseol/pybots-server) [![Coverage Status](https://coveralls.io/repos/spseol/pybots-server/badge.svg?branch=master&service=github)](https://coveralls.io/github/spseol/pybots-server?branch=master)

Zajímáš se o programování? Chceš vyřešit základní algoritmické problémy? Chceš si zkusit práci s HTTP protokolem a jeho metodami? Chceš porazit svého kamaráda v pořádné hře pro programátory? Pokud ano, tak přesně pro Tebe je hra PYBOTS!

**PYBOTS** je herní API server napsaný v pythonu, který zajištuje distribuci a zpracování herních map a herních akcí. Hrát může jakýkoliv program, co umí poslat GET/POST HTTP požadavek a vyřešit jednoduchý algoritmický problém.

## Chci si zahrát, co mám dělat?

* vyber si svůj oblíbený programovací jazyk - doporučuji Python, ale zvládne to i Javascript, Java, PHP, C/C++ nebo exotický Haskell
* zjisti si, jak je na tom tvůj jazyk s podporou HTTP protokolu, stačit Ti budou GET a POST metody, a jak vlastně takový požadavek ze svého jazyka pošleš (od pythonu3 je to velmi jednoduché, obsahuje totiž modul `requests`, který to vše zvládne levou zadní)
* pošli si prázdný GET požadavek na jakýkoliv server PYBOTS, třeba `http://hroch.spseol.cz:44822/` a sleduj, co se Ti vrátilo
* správně, je to JSON (pokud nevíš, co to je, [UTFG](https://www.google.cz/search?q=JSON)), překóduj si jej do svého datového typu - nejspíš nějaký slovník či hashmap (v pythonu koukej po modulu `json` a jeho metodě `json.loads`)
* z dekódované odpovědi načti id svého bota z klíče `bot_id` a podíváme se na mapu
* vem id svého bota a pošli GET požadavek na `/game/{bot_id}`
* opět dekóduj a můžeš vidět tyto klíče v odpovědi:
  *  `game_info` uschovává další informace - například objekt `map_resolutions`, zapnutí tahů, laserů nebo baterek, může se hodit
  *  `map` označuje dvourozměrné pole celé mapy, první rozměr označuje výšku, druhý, zanořený, šířku; o hodnotách vevnitř mapy čti dále
* spočítej, co chceš, aby tvůj bot udělal, krok, laser, čekat nebo se třeba otočit?
* pošli POST požadavek na `/action` s parametry `bot_id` = id tvého bota a `action` = jedna z hodnot vyjmenovaných níže v tabulce akcí
* v odpovědi si pohlídej, že jsi úspěšně zahrál
* pokračuj tak, aby jsi vyhrál!

* * * 

## Co můžu v jednom tahu zahrát?

### jakákoliv hra

#### krok
tvůj bot se jednoduše pohne o pole dopředu, samozřejmě to nepůjde mimo mapu, do jiného bota nebo do pevného bloku - avšak při kroku na poklad **vyhraješ!**

při hře s baterkami Tě to bude stát **jednu úroveň baterie** 

#### otočení
tvůj bot se otočí, doprava nebo doleva

nestojí **nic z energie baterky**

### hra s bateriemi

#### nabíjení
tvůj bot bude tah čekat na místě a **nabije si baterii**

### hra s lasery
#### laser paprsek
bot bude soustředit energii jedním směrem a vypálí urychlený proud fotonů, který dokáže **nepřátelskému botu ubrat energii** nebo **zničit pevný blok**

energeticky to nebude úplně nejlevnější, **paprsek sežere** alespoň **dvě úrovně** baterie

* * * 

## Co vše můžu v mapě najít?
každé pole je v mapě reprezentováno jako objekt vždy obsahující klíč `field`, který označuje typ pole, viz následující seznam 
#### prázdné pole
jednoduché prázdné pole, bot na něj může v klidu vstoupit, laserem je propálitelný

reprezentace tohoto pole v mapě je jednoduchá, prostá `0`

#### poklad
cíl tvého bota, uzmi si jej pro sebe vstoupením na něj!

v mapě poklad najdeš jako jednoduchou hodnotu `1`

#### pevný blok
pevný blok, kterým jen tak jednodušše neprojdeš, ale **zničit** jej můžeš **laserem** svého bota

v mapě je identifikován jako `3`

#### cizí bot
tví nepřátelé, za každou cenu jim musíš zamezit přístup k pokladu a nebo je i zpomalit pomocí laseru tvého bota
kromě klíče `field` se v botově objektu nachází i jeho orientace uložená v `orientation` 
```json
{
	"field": 2,	
	"orientation": 2
}
```

při hře s baterkama je to lehce složitější, hodnota klíče `field` je `4` a navíc je známa i hodnota nabití baterie
```json
{
	"field": 4,
	"orientation": 0,
	"battery_level": 3
}
```
## Co se může hodit?
* na `/info` najdeš základní enumerace pro orientace botů, typy bloků v mapě a návratové hodnoty ze zpracování akce
* každý požadavek na `/action` vrací v odpovědi klíč `state`, který identifikuje status provedení žádáné akce, dle něj můžeš jednodušše poznat, zda se akce povedla, případně co bylo problémem (nemožnost vstoupit na blok, nedostatečná úroveň baterie, bot není na tahu, neznámé `bot_id` případné nevalidní akce)

## FAQ
\# TODO

## kontakt
v případě jakýchkoliv problémů se serverem, klientem nebo jen žádostí o radu se na mě nebojte obrátit, [@thejoeejoee](https://github.com/thejoeejoee) na Githubu nebo [@thejoeejoee](https://twitter.com/thejoeejoee) 
