##################################################################
# Web interface for konto_check, written in Python
# Author: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
# Copyright: 2020 SolidCharity.com
# License: GNU Lesser General Public License v3 (LGPLv3) (LGPLv3)
##################################################################
from flask import Flask
from flask import request
from flask import Response
import traceback
import kontocheck
from kontocheck import KontoCheckError

debug = False
kontocheck.lut_load()

app = Flask(__name__)

def info(testkonten, converted):
    out=""
    out += "<html><head><title>Konto_check Testseite</title></head>"
    out += "<body><h1>Testseite konto_check</h1>"
    out += "Diese Seite liefert auch XML Daten als Antwort auf Anfragen in der Form: "
    out += '<a href="/?kto=648489890&blz=50010517">/?kto=648489890&blz=50010517</a><br/>'
    out += 'und <a href="/?iban=DE12500105170648489890&bic=INGDDEFFXXX">/?iban=DE12500105170648489890&bic=INGDDEFFXXX</a><br/>'
    out += 'und <a href="/?iban=DE12500105170648489890&bic=invalid">/?iban=DE12500105170648489890&bic=invalid</a><br/>'
    out += 'und <a href="/?iban=DE12500105170648489890">/?iban=DE12500105170648489890</a><br/>'
    out += 'und <a href="/?bic=INGDDEFFXXX">/?bic=INGDDEFFXXX</a><br/>'
    out += 'und <a href="/?valid_lut_file=check">/?valid_lut_file=check</a><br/>'

    out += '<br/>'
    out += 'Diese Seite arbeitet mit der unter LGPL Lizenz stehenden Bibliothek <a href="http://kontocheck.sourceforge.net/">konto_check</a> von Michael Plugge, '
    out += '<a href="http://sourceforge.net/projects/kontocheck/files/konto_check-de/6.11/">Version 6.11 vom 12. Dezember 2019</a>. Die blz.lut enth&auml;lt die Bankdaten von 2020-03-09 bis 2020-09-06.<br/><br/>'

    if not kontocheck.lut_is_valid():
        out += '<br/><br/><strong>Die blz.lut Datei ist zu alt!</strong><br/><br/>';

    out += 'Der Code dieser Seite befindet sich hier: '
    out += '<a href="https://github.com/SolidCharity/kontocheck_web.py">https://github.com/SolidCharity/kontocheck_web.py</a>.'
    out += '<br/>';
    out += 'Es wird die kontocheck Implementierung von Thimo Kraemer eingesetzt: '
    out += '<a href="https://pypi.org/project/kontocheck/">https://pypi.org/project/kontocheck/</a>'
    out += '<br/><br/'

    out += '<br/><br/>'
    out += 'Bitte in das folgende Textfeld die zu testenden Bankverbindungen (BLZ/Kto, durch Blanks getrennt) eingeben.'
    out += '<br/>'
    out += '<p><form method="post"><textarea cols="50" rows="15" name="testkonten">'+testkonten+'</textarea>'
    out += '<p><input type="submit" name="testen" value="Konten testen"></p>'
    out += '</form></p>'

    if converted is not None:
        out += '<h2>Testergebnisse:</h2><table>' + converted+ '</table>'

    out += '</body></html>'
 
    return out

def convert(kto,blz):
    try:
        (iban,bic) = kontocheck.create_iban(blz, kto, True);
        bankname = kontocheck.get_name(iban)
        plz = kontocheck.get_postalcode(iban)
        ort = kontocheck.get_city(iban)
        result = 'ok'
    except KontoCheckError as err:
        bic=''
        iban=''
        bankname=''
        plz=''
        ort=''
        result=err._error_codes[err.code]
    return (iban,bic,bankname,plz,ort,result)


def convertMultiple(testkonten):
    try:
        testkonten = testkonten.replace('\t', ' ')
        converted = ''
        for line in testkonten.splitlines():
            (blz,kto) = line.split()
            (iban,bic,bankname,plz,ort,result) = convert(kto,blz)
            converted += '<tr><td>'+blz+'</td><td>'+kto+'</td>'
            converted += '<td>'+result+'</td><td>'+bankname+'</td><td>'+plz+' '+ort+'</td>'
            converted += '<td>'+iban+'</td><td>'+bic+'</td></tr>'
    except:
        converted='Fehler beim Parsen der Eingabedaten'
        
    return info(testkonten, converted)

def validLutFile():
    out = '<?xml version="1.0" encoding="utf-8"?>'
    out += '<result>'
    out += '<lutfile>'+('valid' if kontocheck.lut_is_valid() else 'invalid')+'</lutfile>'
    out += '</result>'
    return Response(out, mimetype='text/xml')

def toIban(kto, blz):
    (iban,bic,bankname,plz,ort,result) = convert(kto,blz)

    out = '<?xml version="1.0" encoding="utf-8"?>'
    out += '<result>'
    out += '<bic>'+bic+'</bic>'
    out += '<iban>'+iban+'</iban>'
    out += '<bankname>'+bankname+'</bankname>'
    out += '<plz>'+plz+'</plz>'
    out += '<ort>'+ort+'</ort>'
    out += '<kontocheck>'+result+'</kontocheck>'
    out += '</result>'
    return Response(out, mimetype='text/xml')

def validateIbanBic(iban, bic):
    valid_iban = kontocheck.check_iban(iban);
    valid_bic = False
    if valid_iban:
        valid_bic = kontocheck.get_bic(iban) == bic
    out = '<?xml version="1.0" encoding="utf-8"?>'
    out += '<result>'
    out += '<iban>'+str(1 if valid_iban else 0)+'</iban>'
    out += '<bic>'+str(1 if valid_bic else kontocheck.get_bic(iban))+'</bic>'
    out += '</result>'
    return Response(out, mimetype='text/xml')

def validateIban(iban):
    valid_iban = kontocheck.check_iban(iban);
    bic = ''
    if valid_iban:
        bic = kontocheck.get_bic(iban)
    out = '<?xml version="1.0" encoding="utf-8"?>'
    out += '<result>'
    out += '<iban>'+str(1 if valid_iban else 0)+'</iban>'
    out += '<bic>'+bic+'</bic>'
    out += '</result>'
    return Response(out, mimetype='text/xml')

def validateBic(bic):
    try:
        bankname = kontocheck.scl_get_bankname(bic)
        valid_bic = bankname is not None
    except:
        valid_bic = False

    out = '<?xml version="1.0" encoding="utf-8"?>'
    out += '<result>'
    out += '<bic>'+(bic if valid_bic else 'invalid')+'</bic>'
    out += '</result>'
    return Response(out, mimetype='text/xml')

@app.route("/", methods=['GET', 'POST'])
def root():
  try:
    kto = request.args.get('kto')
    blz = request.args.get('blz')
    iban = request.args.get('iban')
    bic = request.args.get('bic')
    valid_lut_file = request.args.get('valid_lut_file')

    if request.method == 'POST':
        return convertMultiple(request.form['testkonten'])
    elif valid_lut_file is not None:
        return validLutFile()
    elif kto is not None and blz is not None:
        return toIban(kto, blz)
    elif iban is not None and bic is not None:
        return validateIbanBic(iban, bic)
    elif iban is not None:
        return validateIban(iban)
    elif bic is not None:
        return validateBic(bic)
    else:
        return info('50010517 648489890', None)
  except:
    if debug:
        return("\n\n<PRE>"+traceback.format_exc())
    else:
        return("There is an error.")

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0')
    except:
        print('error')
