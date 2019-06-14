
# Python Starter Kit 0.2.0

## Info

Projekt jest paczką dla tworzenia nowych aplikacji w języku **Python 3.6+**
i jest dostosowane dla edytora [Visual Studio Code](https://code.visualstudio.com) _(ver. [1.35](https://code.visualstudio.com/updates/v1_35) )_


## Wymagania

 1. Środowisko [Python](https://www.python.org) 3.6.x lub nowsze.
 2. Program [Visual Studio Code](https://code.visualstudio.com).
 3. Wtyczka [Python](https://github.com/Microsoft/vscode-python) dla Visual Studio Code.


## Instalacja (Windows 10)

**[1]** Uruchom konsolę (terminal) w katalogu projektu.

**[2]** Zainstaluj VENV, polecenie:

```
python -m venv venv
```

**[3]** Zainstaluj narzędzia deweloperskie, polecenie:

```
"venv/Scripts/python.exe" -m pip install -r requirements_dev.txt
```

**[4]** Zainstaluj moduły których aplikacja potrzebuje do pracy, polecenie:

```
"venv/Scripts/python.exe" -m pip install -r requirements_prod.txt
```

**[5]** Teraz możesz uruchomić aplikację poleceniem:

```
"venv\Scripts\python.exe" app
```
_(aplikacja znajduje się w katalogu `app`)_


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

**[3]** Zainstaluj narzędzia deweloperskie, polecenie:

```
venv/bin/python -m pip install -r requirements_dev.txt
```

**[4]** Zainstaluj moduły których aplikacja potrzebuje do pracy, polecenie:

```
venv/bin/python -m pip install -r requirements_prod.txt
```

**[5]** Teraz możesz uruchomić aplikację poleceniem:

```
venv/bin/python app
```
_(aplikacja znajduje się w katalogu `app`)_


### Konfiguracja VCS _(Linux)_

Plik `.vscode/settings.json` który znajduje się w repozytorium jest przeznaczony dla systemu **Windows**. Jeżeli chcesz aby konfiguracja działała poprawnie w systemie **Linux** to musisz skorzystać z poniższej konfiguracji:

```
{
    "python.pythonPath": "venv/bin/python",
    "python.linting.pep8Enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true
}
```


## Zadania

**[1]** Zadania są obsługiwane przy pomocy programu [Invoke](http://www.pyinvoke.org)

**[2]** Plik `./tasks.py` zawiera definicje zadań.

**[3.1]** Zadanie uruchamiamy prze polecenie (Windows 10):

```
"venv/Scripts/invoke.exe" clean
```

Objaśnienie _(legenda)_:

`"venv/Scripts/invoke.exe"` - lokalizacja pliku wykonywalnego aplikacji **invoke**
`clean` - przykładowa nazwa zadania zdefiniowanego w pliku `./tasks.py`

Można zastosować też skróconą wersję **(tylko Windows 10)**:

```
invoke clean
```

**[3.2]** Uruchamianie zadań w systemie Linux _(Linux Lite 4.4, Ubuntu 18.04.2 LTS)_:

```
venv/bin/invoke clean
```
