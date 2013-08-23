# 3DSpong

Basic Pong game implementation in Petit Computer BASIC language for Nintendo 3DS

## Requirements

- http://petitcomputer.com

## Converter

Petit Computer sabe the source code inside a binary file in 3DS' SD Card. I've
created a converter that basically strip a binary head from file and replace
some characters based on a CHARMAP.

Use the command line below to convert a binary file called `RPRG001.PTC` into a `pong.bas`:

```sh
$ ./binsrc.py RPRG001.PTC pong.bas
```

## Play

Use the following QR Codes to load first version of the game on your Nintendo 3DS's Petit Computer BASIC:

### First Part

![First](/qrcodes_v1/qr0_big.png)

### Second Part

![Second](/qrcodes_v1/qr0_big.png)

