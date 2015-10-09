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
    + -> `200` vrátí:
    + `bot_id`: unikátní ID bota
* `GET /game/<bot_id>` pohled na hrací pole
    + -> vrátí `200` (slovník) s polohou botů
    + `map`: dvorozměrné pole polí v mapě
* `POST /action` tah bota. Očekává parametry:
    + `bot_id`: `<ID bota>`
    + `action`:
        - `0`
        - `1`
        - `2`
    + -> vrátí `200` a mapu s aplikovaným pohybem
    + -> pokud je nutná dodatečná informace k tahu (nemožnost tahu, ukončení hry), je v klíči `state` dostupný stav.
* `GET /info` vrátí výčet akcí a orientací:
    + -> `"action": {"0": "STEP", ...}`
    + -> `"orientation": {"0": "NORTH", ...}`
