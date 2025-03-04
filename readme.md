# Newman Automation Testing 

## Description

Automate Postman API collections using Newman in Python

Automation Planning::

Phase1: Automate Postman collections in local 

Phase2: Automate Postman collections in Jenkins

Phase3: Automate Postman collection in Jenkins + automatically update Jira status

## Getting Started

### Installing

* Install python3
* 

### Executing program

1) Know what collections, environments & folder/subfolder (optional) to run
2) Open terminal, and cd to the folder directory
3) Run command below:

    python3 api_test.py [collections] [environments] "[Folder in the specific collection]" 

    **Collections: Sample, FlashRegression, FlashRegression2

    **Environments: SIT, UAT, PROD

    **Folder: This is optional to only specific run certain folder in the collection. By default, it will run the whole specified collection

```sh
#Example:

python3 api_test.py FlashRegression2 SIT "PF eInvoice R25_MVP 7.2"
```# pyman
