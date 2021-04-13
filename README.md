# JarvIEEEs
An open source project called J.A.R.V.IEEE.S in development of a personal desktop assistence by the IEEE RAS CIMATEC Student Branch for personal use of IEEE members or voluntiers

## Install the packages

- Clone this repository:
```bash
$ git clone https://github.com/rascimatec/JarvIEEEs
```

- Install all packages:
```bash
$ pip install -r req.txt
```

## Package contents
- **Comandos:** the main file that should be run
- **DataBase:** functions used to establish the connection with the database
- **lib:** files used to train the Chatterbot. On the root are the files cloned from: https://github.com/gunthercox/chatterbot-corpus and on the custom folder are added train files

## Personalizing
### Adding commands to the database
.
### Adding custom train files
Acess
```bash
$ cd PATH/lib/portuguese/custom
```
and there add new .yml files
for more information acess https://github.com/gunthercox/chatterbot-corpus

Note that this version was developed to the portuguese language. So change the portuguese folder for a new folder with files from the desired language

## Simulation
- run the Comandos.py file

## Creating the executable
```bash
$ cd "PATh/JarvIEEEs"
$ Pyinstaller --path="PATH\JarvIEEEs\Geral" --onefile temp_run.py 
```
where 'PATH' is the location of the 'JarvIEEEs' directory.


#### * This repository was developed on windows operating system, so not all features will work with another operating system