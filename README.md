Pybots -- server 
====================

[![Build Status](https://travis-ci.org/spseol/pybots-server.svg?branch=master)](https://travis-ci.org/spseol/pybots-server)
[![Coverage Status](https://coveralls.io/repos/spseol/pybots-server/badge.svg?branch=master&service=github)](https://coveralls.io/github/spseol/pybots-server?branch=master)

Malý herní server pro soutěže robotů


Pravidla hry a komunikace
---------------------------

Server komunikuje pomocí `http` na portu `44822`. Vrací vždy řetězec 
[JSON](https://cs.wikipedia.org/wiki/JavaScript_Object_Notation). Data jsou 
vždy uspořádána do slovníku.


* `GET /` založí novou hru
    + -> `200` vrátí (slovník) ID hráče
    + `id`: ID hráče
* `GET /game/<ID>` pohled na hrací pole
    + -> vrátí `200` (slovník) s polohou hráčů
    + `map`: seznam řádků s kódy jednotlivých políček
* `POST /action` tah hráče. Očekává parametry:
    + `id`: `<ID hráče>`
    + `action`:
        - `step`
        - `turn left`
        - `turn right`
    + -> vrátí `202` a `Location` odpovědi. Odpověď bude možné číst až poté
      co všichni hráči oznámí svůj tah.
* `GET /answer/<answerID>` odpověď na tah
    + -> vrátí `200` s oznámením o úspěšném, nebo neúspěšném tahu
    + -> vrátí `423` s časovým údajem, za jak dlouho se má klient znovu zeptat
