# QUIZBOT  - Pràctica LP 2019/20 Q1 

Pràctica de compiladors i bot de Telegram per l'assignatura de llenguatges de programació de la UPC. Per realitzar la part de compiladors s'ha utilitzat ANTLR4 i Python3 per la part del bot de Telegram. La pràctica consisteix en compilar una enquesta (en un format establert i escrita en format .txt) de manera que se'n extreu tota la informació necessària per tal de que els usuaris la pugin respondre a través de un bot de Telegram. Les característiques del compilador i del bot s'estudiaran en detall a continuació. 


## Instal·lació

Aquestes instruccions et baixaran una còpia del projecte apunt per córrer a la teva màquina local. 

### Prerequisits

Per l'execució del bot es encessita **python3** i **pip3** per la instal·lació d'extencions i llibreries. En cas de no tenir-ho instal·lat, el següent [enllaç](https://realpython.com/installing-python/) explica detalladement com instal·lar-ho. Per la part de compiladors es necessita **ANTLR4**, que es pot instal·lar [aquí](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md). 

```
python3
```
```
pip3
```
```
antlr4
```
### Instal·lació del Bot

Per instal·lar descomprimim el fitxer **.zip**. Un cop a dins la carpeta:

```
pip3 install -r requirements.txt
```
Per la part de compiladors, amb ANTLR4 instal·lat a la màquina és suficient. Un cop finalitzat, ja es podrà executar.

### Execució

Per executar:

```
python3 bot.py
```

## Tests
_* Remarcar que tots els tests del bot s'han realitzat amb l'enquesta facilitada en la presentació de la pràctica. En el següent apartat s'estudia a fons el funcionament del compilador d'enquestes._

Un cop ja tenim el bot funcionant, des de Telegram podrem executar-lo fent click a **start**. El que observarem serà el següent:

<p align="center">
  <img width="400" src="https://i.ibb.co/k1B2cjK/Screenshot-2020-01-06-at-14-59-48.png">
</p>

Amb la opció **/help** observem totes les funcionalitats del bot:
<p align="center">
  <img width="400" src="https://i.ibb.co/pKryzD2/Screenshot-2020-01-06-at-15-10-39.png">
</p>

La primera funcionalitat és **/author** per veure les dades de l'autor del projecte:
<p align="center">
  <img width="400" src="https://i.ibb.co/0XwjkXN/Screenshot-2020-01-06-at-15-14-26.png">
</p>

La segona funcionalitat seria realitzar alguna de les enquestes compilades amb el compilador. Aqui és important posar bé el nom de l'enquesta compilada ja que de l'altre manera no podrem realitzar l'enquesta ni veure els resultats. En aquesta part s'ha intentat desenvolupar el bot per tal de ser escalable pel que fa el nombre d'usuaris que responen l'enquesta i també pel que fa el nombre d'enquestes. És a dir, mitjançant el bot usuaris diferents podrien estar realitzant enquestes diferents. 

Si posem malament el nom de l'enquesta, podem obserar com se'ns mostren el nom de les enquestes disponibles:
<p align="center">
  <img width="400" src="https://i.ibb.co/HxPX1cm/Screenshot-2020-01-06-at-15-23-00.png
">
</p>

Observem doncs com se'ns informa que hi ha l'enquesta amb nom _E_ per respondre:

<p align="center">
  <img width="400" src="https://i.ibb.co/VQFkCRq/Screenshot-2020-01-06-at-15-25-27.png
">
</p>
<p align="center">
  <img src="https://i.ibb.co/VQFkCRq/Screenshot-2020-01-06-at-15-25-27.png" width="300" />
  <img src="https://i.ibb.co/VQFkCRq/Screenshot-2020-01-06-at-15-25-27.png" width="300" /> 
</p>
## Explicació

### COMPILADOR



```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
