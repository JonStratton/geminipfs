# geminipfs
Gemini IPFS Gateway

## Install and user
Install the dependencies and clone the repo:

	apt-get install git python3-venv
	git clone https://github.com/JonStratton/geminipfs
	cd geminipfs


Optionally make a venv and install the python requirements (gemeaux and requests):

	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt


Generate certificates in the directory where geminipfs.py runs from:

	openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem -subj "/CN=localhost" -addext "subjectAltName=IP:127.0.0.1"

Optional, run the ipfs daemon. If not, the text will be pulled from https://ipfs.io/ipfs/

	ipfs daemon

Start geminipfs

	python3 ./geminipfs.py

Run a gemini client point it at gemini://127.0.0.1/ipfs/ plus the hash:

	amfora gemini://127.0.0.1/ipfs/QmSZ5rn5f9TMp3e9xfEGSFEnoFG3rxBros3H5zWgLWuWA2

Optionally open gateway to the network. Create a cert with the resolvable name and run with an IP to listen on (0.0.0.0 for all). Warning; this hasn't been security tested:

	openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem -subj "/CN=localhost" -addext "subjectAltName=DNS:localhost,DNS:`hostname`,DNS:`hostname`.lan,IP:127.0.0.1"
	python3 geminipfs.py --ip 0.0.0.0

## Adding a gemini site to ipfs
Recursively adding a directory with contents to ipfs:

	ipfs add my_gem_site/ -r

Accessing an individual page

	amfora gemini://127.0.0.1/ipfs/QmSZ5rn5f9TMp3e9xfEGSFEnoFG3rxBros3H5zWgLWuWA2/blah.gmi
