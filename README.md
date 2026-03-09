<https://tsibley.net/seattle/biketag/>

Quick and dirty map for the [Seattle bike tag
game](https://seattle.biketag.org), so I can better review previous tags to
avoid previous spots!

Thrown together by starting from my old [Seattle Fire
map](https://tsibley.net/seattle/fire/).

Run the map locally with:

    python3 -m http.server --cgi

Since the Digital Ocean Spaces bucket doesn't allow open cross-origin resource
access, a proxy endpoint is required (`cgi-bin/tags.cgi`).
