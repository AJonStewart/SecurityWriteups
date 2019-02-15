# JSONP Vulnerabilities
## The Wild West
Long ago there were no protections against cross origin data requests. 
This meant that you could grab information from any site with XMLHttpRequests (AJAX),
which was a much desired feature for developing websites. This let you shift getting data
from external APIs to the front end, instead of having to set up a backend service to 
act as a middle man for fetching data. 
## The Problem with the Wild West
This lead to some security issues, however, because hackers could craft clever XSRF 
attacks to intercept the AJAX requests and steal the data. That's a big issue, so developers got to work 
creating a patch at the browser level.
# How did Developers Stop This?
To prevent this, most browsers implemented a [Same Origin Policy](https://en.wikipedia.org/wiki/Same-origin_policy).
The SOP disallowed communications from sources with different domain names, protocols, and port numbers. This 
prevented attackers from creating XSRF AJAX interceptions because the browser would recognize that the user
unknowingly was trying to load code referencing another origin. In most cases, a good site would not try 
to do that. Some legitimate uses of a cross origin request could be
* Hitting an endpoint on a different subdomain, say `api.foo.com` from `foo.com`
* Loading data from an API from the front end.
To bypass this, developers started using Javascript Serialized Object Notation with Padding (JSONP).
## JSONP? Never Heard of it
Wikipedia has a very succinct definition of JSONP. 
"[JSONP](https://en.wikipedia.org/wiki/JSONP) is a javascript pattern to request data by loading a 
`<script>` tag... JSONP enables sharing of data bypassing the Same Origin Policy". Browsers
have to enable the use of the `<script>` tag. Without it, almost every site we know today would not
function. Requesting JSON by itself with a `<script>` tag is technically valid, because JSON data 
is Javascript. However, the browser would interpret this as a block of code with no function, conditional, 
or loop surrounding it. Therefore, the browser would throw a syntax error and not load the page.
So, someone clever proposed the idea of wrapping a returned JSON object in a Javascript function,
and specify the callback function on the request to be said function. For this to work, the API in
which the user called must be expecting to return *JSONP*, not just standard JSON. Now let's look at
the standard architecture of JSONP.

