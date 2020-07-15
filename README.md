# Using the Call of Duty - Modern Warfare API with Python

## Call of Duty: Modern Warfare API Documentation
- This API provides stats for Warzone and Multiplayer and is forked from [https://github.com/EthanC/CallofDuty.py](https://github.com/EthanC/CallofDuty.py)

## Pre-requisites

- Install **python** 3.8.4
  - Check python version
	```cmd
	python3 --version
	```
- Install **git** 2.25.1
- Make project folder
	```cmd
	mkdir CallOfDutyApi
	```
- create a **venv** in that folder
	```cmd
	python3 -m venv .venv
	```
- Activate venv
	```cmd
	.venv\Scripts\activate
	```
- Clone repository
	```cmd
	git clone git@github.com:melwick/CallofDuty.py.git
	```
- Install wheel
	```cmd
	pip install wheel
	```
- Install all other requirements
	```cmd
	pip install -r requirements.txt
	```
- Install **Visual Studio Code** 1.47.1
	- Install python extension
	- Install Code Runner
	- Optional
		- Gitlens
		- GitHistory
		- Vim
		- vscode-icons
- Edit the .env file
```.env
ATVI_EMAIL="oli@gmx.de"
ATVI_PASSWORD="hubbasubba"
```
* * *
end