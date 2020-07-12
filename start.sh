#! / bin / bash

# Sair cedo com erros
set -eu

# O buffer do Python stdout. Sem isso, você não verá o que "imprime" nos Logs de atividades
exportar PYTHONUNBUFFERED = true

# Instale o ambiente virtual Python 3
VIRTUALENV = .data / venv

E se [ ! -d $ VIRTUALENV]; então
  python3 -m venv $ VIRTUALENV
fi

E se [ ! -f $ VIRTUALENV / bin / pip]; então
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $ VIRTUALENV / bin / python
fi

# Instale os requisitos
$ VIRTUALENV / bin / pip install -r requirements.txt

# Execute um glorioso servidor Python 3
$ VIRTUALENV / bin / python3 app.py