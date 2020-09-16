Kontocheck als Web Service
==========================

Dieses Projekt arbeitet mit der unter LGPL Lizenz stehenden Bibliothek [konto_check](http://kontocheck.sourceforge.net/) von Michael Plugge.

Es wird die kontocheck Implementierung von Thimo Kraemer eingesetzt: https://pypi.org/project/kontocheck/

Es gibt regelmäßig neue Bankdateien von der Bundesbank, die Regeln enthalten, wie die Kontonummern und Bankleitzahlen, bzw. IBAN und BIC zu berechnen sind.

Lizenz
------

Dieses Skript steht unter der Lizenz: GNU Lesser General Public License v3 (LGPLv3) (LGPLv3)

Installation
------------

```
git clone https://github.com/SolidCharity/kontocheck_web.py.git kontocheck
virtualenv -p /usr/bin/python3 $HOME/pyenv
source pyenv/bin/activate
cd ~/kontocheck
pip3 install -r requirements.txt
```

Beispielaufrufe
---------------

* Umrechnen von Kontonummer und BLZ in IBAN und BIC: /?kto=648489890&blz=50010517
* Überprüfung von IBAN und BIC: /?iban=DE12500105170648489890&bic=INGDDEFFXXX
* Korrektur von BIC: /?iban=DE12500105170648489890&bic=invalid
* Liefern von BIC: /?iban=DE12500105170648489890
* Überprüfung von BIC: /?bic=INGDDEFFXXX
* Prüfung ob die Datei mit den Bankleitzahlen noch aktuell ist: /?valid_lut_file=check

Demo Version
------------

Dieses Skript kommt auf der Seite https://kontocheck.solidcharity.com/ zum Einsatz, die bei der [Hostsharing eG](https://hostsharing.net) gehostet ist.

Diese Seite darf gerne für produktiven Einsatz und für Tests genutzt werden.
