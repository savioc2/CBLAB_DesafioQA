# Desafio QA - Sávio Cunha de Carvalho

- [Link do video da automatização](https://youtu.be/xHMyIHnnY5I) 


### Scripts:
Os scripts foram desenvolvidos conforme o plano de teste escrito na primeira etapa do desafio. O arquivo "desafio_test.py" contém as scripts que sustetam a segunda parte do desafio, cuja as instruções para sua execução está listado no final deste arquivo. 

### Dificuldades:
Durante a exceção do teste de cadastro de usuário, o xpath de "notificação" não foi encontrada, pois a label não estava com o xpath competo, desta maneira, o teste é cancelado quando chegar neste determinado ponto. Uma forma alternativa de realizar a operação é passando um By.ID pegando o id da label com identificador do campo.

No decorrer do desenvolvimento, foi encontrado bugs na aplicação, onde foi relatado no arquivo da primeira etapa. 

Tenho muita experiência com testes desenvolvidos em java, desta forma, o python foi um desafio para o desenvolvimento, mas segui a sujestão descrita no desafio. 


## Instrução para exceltar os testes:


### Faça um clone do repositorio remeto:
``` bash
git clone git@github.com:savioc2/CBLAB_DesafioQA.git
```

### Instale as dependências: 
```bash
pip install -r requirements.txt
```

### Execulte os testes utilizando o camando:

```bash
python3 desafio_test.py
```

## Versões

### WebDriverChrome
```bash
 117.0.5938.62
```
### Seleniun
```bash
4.12.0
```