<h1>BeautifulSoup</h1>

from bs4 import BeautifulSoup

```
html_file = open("files/generic_simple.html", mode = 'r', encoding = 'utf-8')

<_io.TextIOWrapper name='files/generic_simple.html' mode='r' encoding='utf-8'>
````
***
**soup = BeautifulSoup(html_file)**

***

lista de métodos
``` 
print(dir(soup)) 
```
***
**soup.prettify()**


**soup.get_text()**

***

**soup.get_text().replace("\n", "")**

```python
'Um HTML simplesUm tópico aleatórioEu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.\t\tAinda assim, se você está lendo, o problema é seu.\t\tVocê ainda não consegue descobrir, eu sou inútil?\t\tPessoal, parem de me ler agora.\t\tObrigado\tJá utilizou o google hoje? Ir para o google Sou apenas uma nova divisão\tQuer ir para o site do professor?\tIr agoraVamos participar do grupo do curso?Entrar no grupo do telegramSou um rodapé '
```

***

```python
>>> soup.title
<title>Um HTML simples</title>

>>> soup.title.name
'title'

>>> soup.title.parent
</head>

>>> soup.title.parent.parent.name
'html'

````
***

```python
>>> list(soup.div.children)
['\n', <p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.
		Ainda assim, se você está lendo, o problema é seu.
		Você ainda não consegue descobrir, eu sou inútil?
		Pessoal, parem de me ler agora.
		Obrigado
	</p>, '\n']

```

``` python

>>> for i in list(soup.div.children):
...     print(i.name)
... 
None
p
None

```

***

```python
soup.a['href']
```

***

<h2>Soup Find</h2>

```python
>>> soup.find('div')
<div class="article" id="I_AM_Unique" style="background-color:peachpuff">
<p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.
		Ainda assim, se você está lendo, o problema é seu.
		Você ainda não consegue descobrir, eu sou inútil?
		Pessoal, parem de me ler agora.
		Obrigado
	</p>
</div>
```

```python
>>> soup.find('div', id = "imp_article_ID")
<div class="article" id="imp_article_ID" style="background-color:peachpuff">
<h2>Já utilizou o google hoje?</h2>
<a href="http://www.google.com"><h3><b> Ir para o google </b></h3></a>
</div>
```

```python
>>> soup.find('div', class_="article")
<div class="article" id="I_AM_Unique" style="background-color:peachpuff">
<p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.
		Ainda assim, se você está lendo, o problema é seu.
		Você ainda não consegue descobrir, eu sou inútil?
		Pessoal, parem de me ler agora.
		Obrigado
	</p>
</div>
```

```python

>>> soup.find_all('div', class_="article")
[<div class="article" id="I_AM_Unique" style="background-color:peachpuff">
<p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.
		Ainda assim, se você está lendo, o problema é seu.
		Você ainda não consegue descobrir, eu sou inútil?
		Pessoal, parem de me ler agora.
		Obrigado
	</p>
</div>, <div class="article" id="imp_article_ID" style="background-color:peachpuff">
<h2>Já utilizou o google hoje?</h2>
<a href="http://www.google.com"><h3><b> Ir para o google </b></h3></a>
</div>, <div class="article" id="I_AM_AnotherDivID" style="background-color:peachpuff">
<b>Sou apenas uma nova divisão<b><br/>
	Quer ir para o site do professor?
	<a href="https://www.udemy.com/user/gabriel-henrique-casemiro/">Ir agora</a>

</b></b></div>, <div class="article" id="I_AM_AnotherDivID" style="background-color:peachpuff">
<b>Vamos participar do grupo do curso?<b><br/>
<a href="https://t.me/criandoroboscompython">Entrar no grupo do telegram</a>

</b></b></div>]

```

```python
>>> soup.find_all('div', class_="article")[3].a.string
'Entrar no grupo do telegram'

```
```python

>>> soup.find_all('div', class_="article")[3].a["href"]
'https://t.me/criandoroboscompython'
```

***

<h3>Todos os linkds da página</h3>

```python
>>> soup.find_all('a')
[<a href="http://www.google.com"><h3><b> Ir para o google </b></h3></a>, <a href="https://www.udemy.com/user/gabriel-henrique-casemiro/">Ir agora</a>, <a href="https://t.me/criandoroboscompython">Entrar no grupo do telegram</a>]

```

```python

>>> for i in soup.find_all('a'):
...     i['href']
... 
'http://www.google.com'
'https://www.udemy.com/user/gabriel-henrique-casemiro/'
'https://t.me/criandoroboscompython'
>>> 

```
