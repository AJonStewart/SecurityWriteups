# JSONP Vulnerabilities
Long ago there were no protections against cross origin data requests. 
This meant that you could grab information from any site with XMLHttpRequests,
which was a much desired feature for developing websites. This let you shift getting data
from external APIs to the front end, instead of having to set up a backend service to 
act as a middle man for fetching data. This lead to some security issues, however, because hackers could craft clever XSRF 
attacks to steal data. To prevent this, most browsers implemented a Same Origin Policy.
The SOP disallowed communications from sources with different domain names, app 
protocols, and port numbers. To bypass this, developers started using Javascript Serialized
Object Notation with Padding (JSONP).

A clever way attackers created XSRF and XSS attacks in general were through img tags, as
it invokes the browser to make an uncensored GET request.
