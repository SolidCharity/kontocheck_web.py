Install with Passenger on Hostsharing.net
=========================================

```
export domain=kontocheck.solidcharity.com
export pyenv=$HOME/pyenv

git clone https://github.com/SolidCharity/kontocheck_web.py.git kontocheck
virtualenv -p /usr/bin/python3 $pyenv
source $pyenv/bin/activate
   pip3 install flask kontocheck
   deactivate

cd doms/$domain/
rm -Rf htdocs-ssl
ln -s ~/kontocheck/public htdocs-ssl
ln -s ~/kontocheck/public kontocheck
cat > .htaccess <<FINISH
PassengerPython $pyenv/bin/python
#PassengerAppEnv development
#PassengerFriendlyErrorPages on
FINISH

cat > app-ssl/passenger_wsgi.py <<FINISH
import os, sys
sys.path.append("$HOME/doms/$domain/kontocheck")
os.chdir("$HOME/doms/$domain/kontocheck")
from kontocheck_web import app as application
FINISH
 
mkdir app-ssl/tmp
touch app-ssl/tmp/restart.txt
```
