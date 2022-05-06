# geminipfs
Gemini IPFS Gateway

## Install, run, and use
Start by generating certificates in the directory where geminipfs.py runs from:

	openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem -subj "/CN=localhost" -addext "subjectAltName=IP:127.0.0.1"

Also install the requirements (gemeaux and requests)

	pip install -r requirements.txt

Optional, run the ipfs daemon. If not, the text will be pulled from https://ipfs.io/ipfs/

	ipfs daemon

Start geminipfs

	python3 ./geminipfs.py

Run a gemini client point it at gemini://127.0.0.1/ipfs/ plus the hash:

	amfora gemini://127.0.0.1/ipfs/QmSZ5rn5f9TMp3e9xfEGSFEnoFG3rxBros3H5zWgLWuWA2

## Adding a gemini site to ipfs
Recursively adding a directory with contents to ipfs:

	ipfs add my_gem_site/ -r

Accessing an individual page

	amfora gemini://127.0.0.1/ipfs/QmSZ5rn5f9TMp3e9xfEGSFEnoFG3rxBros3H5zWgLWuWA2/blah.gmi
