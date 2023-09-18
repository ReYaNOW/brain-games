### Hexlet tests and linter status:
[![Actions Status](https://github.com/ReYaNOW/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/ReYaNOW/python-project-49/actions)
### CodeClimate tests and Maintainability status:
<a href="https://codeclimate.com/github/ReYaNOW/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/f09f6f2f890183ba1102/maintainability" /></a>  
  
  
Этот проект представляет собой игру - Игры разума  
«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:  

Калькулятор. Арифметические выражения, которые необходимо вычислить.  
Прогрессия. Поиск пропущенных чисел в последовательности чисел.  
Определение четного числа.  
Определение наибольшего общего делителя.  
Определение простого числа.  
  
## Установка  

Для установки игры необходимо использовать команду находясь в корневой директории проекта
```
poetry install
```  
  
<hr>  
  
Так же имеется возможность сделать билд проекта с последующей установкой при помощи двух команд
```
make build
```  
А потом
```
python3 -m pip install --user dist/*.whl
```

![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/install.gif?raw=true)  
  
## Использование  
  
Для запуска игры по определению четного числа необходимо использовать команду  
  
```
brain-even
```  
<a href="https://asciinema.org/a/551560?autoplay=1" target="_blank" rel="noreferrer"><img src="https://media.discordapp.net/attachments/324178393161793536/1153163050870906890/image.png" alt="image" /></a>  

  
Для запуска игры «Калькулятор» необходимо использовать команду 
```
brain-calc
```
<a href="https://asciinema.org/a/551578?autoplay=1" target="_blank" rel="noreferrer"><img src="https://media.discordapp.net/attachments/324178393161793536/1153161070479933531/image.png" alt="image" /></a> 


  
Для запуска игры по определению НОД необходимо использовать команду 
```
brain-gcd
```  
<a href="https://asciinema.org/a/551517?autoplay=1" target="_blank" rel="noreferrer"><img src="https://media.discordapp.net/attachments/324178393161793536/1153394675315638403/image.png" alt="image" /></a> 

  
Для запуска игры по определению простого числа необходимо использовать команду 
```
brain-prime
```  
<a href="https://asciinema.org/a/551539?autoplay=1" target="_blank" rel="noreferrer"><img src="https://cdn.discordapp.com/attachments/324178393161793536/1153394997568229508/image.png" alt="image" /></a> 


Для запуска игры «Прогрессия» необходимо использовать команду 
```
brain-progression
```  
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/progression.gif?raw=true)   
  
<hr>  

Минимальные требования:  
Наличие CLI  
Python^3.10  

Опционально:  
Poetry
