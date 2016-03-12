### Chci si zahrát, co mám dělat?

* vyber si svůj oblíbený programovací jazyk - doporučuji Python, ale zvládne to i Javascript, Java, PHP, C/C++ nebo exotický Haskell
* zjisti si, jak je na tom tvůj jazyk s podporou HTTP protokolu, stačit Ti budou GET a POST metody, a jak vlastně takový požadavek ze svého jazyk pošleš (od pythonu3 je to velmi jednoduché, obsahuje totiž modul `requests`, který to vše zvládne levou zadní)
* pošli si prázdný GET požadavek na jakýkoliv server PYBOTS, třeba `http://hroch.spseol.cz:44822/` a sleduj, co se Ti vrátilo
* správně, je to JSON (pokud nevíš, co to je, [UTFG](https://www.google.cz/search?q=JSON)), překóduj si jej do svého datového typu - nejspíš nějaký slovník či hashmap (v pythonu koukej po modulu `json` a jeho metodě `json.loads`)
* z dekódované odpovědi načti id svého bota z klíče `bot_id` a pokračuj na další bod, koukneme se na mapu
* vem id svého bota a pošli GET požadavek na `/game/{bot_id}`
* opět dekóduj a pojďme se podívat na to, jaké máš klíče v odpovědi:
* *  `map_resolutions` uschovává pole [šířka, výška] mapy, může se hodit
* *  `map` označuje dvourozměrné pole celé mapy, první rozměr označuje výšku, druhý, zanořený, šířku; o hodnotách vevnitř mapy čti dále
* spočítej, co chceš, aby tvůj bot udělal, krok, laser, čekat nebo se třeba otočit?
* pošli POST požadavek na `/action` s parametry `bot_id` = id tvého bota a `action` = jedna z hodnot vyjmenovaných níže v tabulce akcí

* * * 
