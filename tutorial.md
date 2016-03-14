## Chci si zahrát, co mám dělat?

* vyber si svůj oblíbený programovací jazyk - doporučuji Python, ale zvládne to i Javascript, Java, PHP, C/C++ nebo exotický Haskell
* zjisti si, jak je na tom tvůj jazyk s podporou HTTP protokolu, stačit Ti budou GET a POST metody, a jak vlastně takový požadavek ze svého jazyk pošleš (od pythonu3 je to velmi jednoduché, obsahuje totiž modul `requests`, který to vše zvládne levou zadní)
* pošli si prázdný GET požadavek na jakýkoliv server PYBOTS, třeba `http://hroch.spseol.cz:44822/` a sleduj, co se Ti vrátilo
* správně, je to JSON (pokud nevíš, co to je, [UTFG](https://www.google.cz/search?q=JSON)), překóduj si jej do svého datového typu - nejspíš nějaký slovník či hashmap (v pythonu koukej po modulu `json` a jeho metodě `json.loads`)
* z dekódované odpovědi načti id svého bota z klíče `bot_id` a pokračuj na další bod, koukneme se na mapu
* vem id svého bota a pošli GET požadavek na `/game/{bot_id}`
* opět dekóduj a pojďme se podívat na to, jaké máš klíče v odpovědi:
  *  `map_resolutions` uschovává pole [šířka, výška] mapy, může se hodit
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
při hře s baterkama Tě to bude stát **jednu úroveň baterie** 

#### otočení
tvůj bot se otočí, doprava nebo doleva
nestojí **nic z baterie**

### hra s bateriemi

#### nabíjení
tvůj bot bude tah čekat na místě a **nabije si baterii**

### hra s lasery
#### laser paprsek
bot bude soustředit energii jedním směrem a vypálí urychlený proud fotonů, který dokáže **nepřátelskému botu ubrat energii** nebo **zničit pevný blok**
energeticky to nebude úplně nejlevnější, **paprsek sežere** alespoň **dvě úrovně** baterie

* * * 

## Co vše můžu v mapě najít?
#### prázdné pole
jednoduché prázdné pole, bot na něj může v klidu vstoupit, laserem je propálitelný
reprezentace tohoto pole v mapě je jednoduchá, prosté `0`

#### poklad
cíl tvého bota, uzmi si jej pro sebe vstoupením na něj!
v mapě poklad najdeš jako jednoduchou hodnotu `1`

#### pevný blok
pevný blok, kterým jen tak jednodušše neprojdeš, ale **zničit** jej můžeš **laserem** svého bota
v mapě je identifikován jako `3`

#### cizí bot
tví nepřátelé, za každou cenu jim musíš zamezit přístup k pokladu a nebo je i zpomalit pomocí laseru tvého bota
s reprezentací bota v mapě to bude trochu složitější, každý bot je reprezentován jako JSON objekt ```JSON
{
	"field": 2,
	"orientation": 2
}```
při hře s baterkama je to lehce složitější, typ pole je odlišný a navíc je známa i hodnota nabití ```JSON
{
	"field": 4,
	"orientation": 0,
	"battery_level": 3
}```



