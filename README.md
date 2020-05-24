# Simple Flask App KLS

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:

  ```
  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  $ python3 -m venv .venv

  # aktywowanie hermetycznego środowiska
  $ source .venv/bin/activate
  $ make deps - instalacja srodowiska   (Makefile)
  $ make lint - sprawdzenie wygladu kodu
  $ make test - odpalenie testow
  $ make run  - uruchomienie aplikacji
  $ make docker_build - zbudowanie pakietu dockera (trzeba z sudo wykonac)
  $ make docker_run - uruchomienie aplikacji jako doker (tez z sudo)
  $ docker stop hello-world-printer-dev - zatrzymanie dockera
  $ docker rm hello-world-printer-dev - wywalenie dockera

  # aleternatywnie zamiast make deps
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  # jako zwykły program
  $ python main.py

  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja
  $ source .venv/bin/activate
  ```

- Integracja z TravisCI:

  ```
  # miejsce na twoje notatki
  https://semver.org/ - strona o wersjonowaniu
  semantic versioning - numerowanie wersji w formacie MAJOR.MINOR.PATCH

  dind Docker in Docker - da sie zagniezdzac dokery jedne w drugim


  http codes
  200	OK
  301	Moved Permanently
  302	Found
  400	Bad Request
  403	Forbidden
  404	Not Found
  405	Method Not Allowed
  500	Internal Server Error
  418	I’m a teapot	„Jestem czajnikiem” – tzw. easter egg.
  ```
  
# Dodano monitoring www na statuscake.com - auto SLA

# Pomocnicze

## Ubuntu

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
