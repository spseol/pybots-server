pybots-server 
====================

[![Build Status](https://travis-ci.org/spseol/pybots-server.svg?branch=master)](https://travis-ci.org/spseol/pybots-server)
[![Coverage Status](https://coveralls.io/repos/spseol/pybots-server/badge.svg?branch=master&service=github)](https://coveralls.io/github/spseol/pybots-server?branch=master)

Malý herní server pro soutěže robotů


Pravidla hry a komunikace
---------------------------

* `/` --> založí novou hru, vrátí slovník, ve kterém bude ID kráče
* `/game/<ID>` --> vrátí slovník, s hracím polem
