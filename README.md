# **Data Generator API – Python API**

**The API is ready for use. Everything is in order.**

It is a rest api that generates some kind of random or stored-based data for the user.

> **1º** The user makes a server request and chooses what type of data he wants to obtain. <br>
> **2º** The server returns the data requested by the user.
## Types of data that can be generated

**People** <br>
**CPF** <br>
**Name** <br>
**Password**

> Obs: In Brazil, the CPF is the Individual Taxpayer Registry. It is a document made by the Federal Revenue and serves to identify taxpayers. CPF is an 11-digit number.

## The process of generating

-   **People** – _It generates a CPF and a people name._

-   **CPF** – _It generates a valid CPF number using some math formulas. Can validate whether it is a valid one._

-   **Name** – _It generates some names based on the data stored in a tuple _._

-   **Password** – _It generates a password randomly._

 
## How to run the server
RUN
```
uvicorn main:app
```

or 

```
uvicorn main:app --reload
```

If you want to see every single change in the files.

> Obs: run it in your terminal; inside lib folder.

## Routes

People
```
http://localhost:8000/
```

CPF
```
http://localhost:8000/cpf/
```

Male Name
```
http://localhost:8000/name/male/
```

Female Name
```
http://localhost:8000/name/female/
```

Password
```
http://localhost:8000/password/
```

Password -- providing a length
```
http://localhost:8000/password/{length}
```

## Language and library

-   **Language** – Python
-   **Library** – fastapi

<br>

## Video
https://user-images.githubusercontent.com/61123877/186533444-52a427f6-4cdb-44c7-b074-da55a246036c.mp4

### Attention!

> **If you want to access the API on your network, through your smartphone, tablet, etc. Look for your ipv4 and initialize the API using this ip.**

EX IP: 192.168.0.26
Run:
```
uvicorn --host "192.168.0.26" main:app
```

