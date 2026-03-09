#!/usr/bin/env python3
import requests
from sys import stdout

response = requests.get("https://seattle-biketag.sfo2.digitaloceanspaces.com/main/index.json")

print("Content-Type:", response.headers["Content-Type"] or "application/json")

if ts := response.headers["Last-Modified"]:
    print("Last-Modified:", ts)

print()
stdout.flush()

for chunk in response.iter_content(chunk_size = None):
    stdout.buffer.write(chunk)
