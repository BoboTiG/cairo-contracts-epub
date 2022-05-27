# EPUB of OpenZeppelin Contracts written in Cairo for StarkNet

Unofficial EPUB of the [OpenZeppelin Contracts written in Cairo for StarkNet, a decentralized ZK Rollup](https://github.com/OpenZeppelin/cairo-contracts).

- Download: [openzeppelin-contracts-in-cairo-for-starknet.epub](output/openzeppelin-contracts-in-cairo-for-starknet.epub)
- Last updated: `2022-05-27`.

## Clone 

```bash
$ git clone --recursive https://github.com/BoboTiG/cairo-contracts-epub.git
```

## Setup

```bash
$ python3 -m venv --copies venv
$ . ./venv/bin/activate
$ python -m pip install -U pip wheel
$ python -m pip install -r requirements.txt
```

Additionally, you want to install `epubcheck`.

## Update, Fetch, and Convert

```bash
$ cd cairo-contracts && git pull --ff-only origin main && cd ..
$ python -m src
```

## Hack

```bash
$ python -m pip install -r requirements-dev.txt
$ ./checks.sh
```
