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
*note: if you get the error message "module not found" when running the code, please install this one manually*
*note: go to `JarvIEEEs/temp_run.py` and change the variable "trainpath" for the complete adress of the folder `lib` at your computer. Do the same to the `JarvIEEEs/Geral/Comandos/Comandos.py` file*
## Install database
- Download the postgresql (the version 12.6 is recommended)
- When asked about the additional select all except the "startbuild" option
- When asked to create a password choose "postgres" without quotation marks
- Run the "pgAdmin 4"
- Double left click at "Servers", after PostgreSQL12 and after Databases
- Right click on Databases, select Create --> DataBase. So set the database name as "LocalDataBase" without quotation marks. Click at save
- Right click at the LocalDataBase just created and choose "restore". Set the format as "custom or tar" and import the "Banco_Jarvies" located at `JarvIEEEs/Geral/Database`. *If you the files don't appear click at the bottom right corner and change the file type from 'backup' to 'all files'*
- Click at restore. It's likely you get a error message but if everything is like the image bellow and you see the same tables the process was successful 

![banner](https://github.com/rascimatec/JarvIEEEs/blob/master/resources/verification.jpg?raw=true)


## Package contents
- **Geral/Comandos:** the main file that should be run
- **Geral/DataBase:** the database itself and the functions used to establish the connection with the database
- **lib:** files used to train the Chatterbot. On the root are the files cloned from: https://github.com/gunthercox/chatterbot-corpus and on the custom folder are added train files
- **resources:** general support files for the repository

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