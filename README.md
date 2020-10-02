
# Python Starter Kit 0.4.0

## Wymagania

 1. Środowisko [Python](https://www.python.org) 3.6.x lub nowsze.
 2. Program [Visual Studio Code](https://code.visualstudio.com).
 3. Opcjonalnie wtyczka [Python](https://github.com/Microsoft/vscode-python) dla **Visual Studio Code**.

```
Name: Python
Id: ms-python.python
Description: Linting, Debugging (multi-threaded, remote), Intellisense, Jupyter Notebooks, code formatting, refactoring, unit tests, snippets, and more.
Version: 2020.8.101144
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python
```
_( ↑ wersja wtyczki która działa poprawnie na dzień 2.X.2020 )_



## Instalacja (Windows 10)

**[1]** Uruchom konsolę (terminal) w katalogu projektu.

**[2]** Zainstaluj VENV, polecenie:

```
python -m venv venv
```

**[3]** Zainstaluj zależności z pliku `requirements.txt`:

```
"venv\Scripts\python.exe" -m pip install -r requirements.txt
```

**[4]** Teraz możesz uruchomić aplikację poleceniem:

```
"venv\Scripts\python.exe" app
```
_(aplikacja znajduje się w katalogu `app`)_

**[5]** _(opcjonalnie)_ Zainstaluj moduły wymagane przez wtyczkę **Python** dla **Visual Studio Code**.

```
"venv\Scripts\python.exe" -m pip install pep8 flake8 pylint autopep8 jedi rope
```

**[6]** _(opcjonalnie)_ Zainstaluj moduł do zarządzania zadaniami.

```
"venv\Scripts\python.exe" -m pip install invoke
```



## Instalacja (Linux Lite 4.4, Ubuntu 18.04.2 LTS)

**[1]** Uruchom konsolę (terminal) w katalogu projektu.

**[2]** Upewnij się że masz zainstalowane pakiety **python3-venv** i **python3-pip**. Jeżeli nie, to je zainstaluj:

```
sudo apt-get install python3-venv
sudo apt-get install python3-pip
```

**[2]** Zainstaluj VENV, polecenie:

```
python3 -m venv venv
```

**[3]** Zainstaluj zależności z pliku `requirements.txt`:

```
venv/bin/python -m pip install -r requirements.txt
```

**[4]** Teraz możesz uruchomić aplikację poleceniem:

```
venv/bin/python app
```
_(aplikacja znajduje się w katalogu `app`)_

**[5]** _(opcjonalnie)_ Zainstaluj moduły wymagane przez wtyczkę **Python** dla **Visual Studio Code**.

```
venv/bin/python -m pip install pep8 flake8 pylint autopep8 jedi rope
```

**[6]** _(opcjonalnie)_ Zainstaluj moduł do zarządzania zadaniami.

```
venv/bin/python -m pip install invoke
```



### Konfiguracja VCS _(Linux)_

Plik `.vscode/settings.json` który znajduje się w repozytorium jest przeznaczony dla systemu **Windows**. Jeżeli chcesz aby konfiguracja działała poprawnie w systemie **Linux** to musisz zamienić format ścieżek dla folderów i plików.

Format **Windows** → `folder1\\folder2\\plik.txt`
Format **Linux**  → `folder1/folder2/plik.txt`

Zamieniamy `\\` na `/` (dotyczy się to tylko pliku JSON)



## Zadania

**[1]** Zadania są obsługiwane przy pomocy programu [Invoke](http://www.pyinvoke.org)

**[2]** Plik `./tasks.py` zawiera definicje zadań.

**[3]** Zadanie uruchamiamy przez polecenie _(Windows 10)_:

```
"venv\Scripts\invoke.exe" clean
```

Objaśnienie _(legenda)_:

`"venv\Scripts\invoke.exe"` - lokalizacja pliku wykonywalnego aplikacji **invoke**
`clean` - przykładowa nazwa zadania zdefiniowanego w pliku `tasks.py`

Można zastosować też skróconą wersję **(tylko Windows 10)**:

```
invoke clean
```

**[4]** Uruchamianie zadań w systemie Linux _(Linux Lite 4.4, Ubuntu 18.04.2 LTS)_:

```
venv/bin/invoke clean
```



## Autor
Adrian Gargula | https://bitbucket.org/Adrosar | https://github.com/Adrosar