# RISCO

RISCO es un Lenguaje de Dominio Específico (DSL) para realizar operaciones matemáticas, implementado con ANTLR4 y Python. Sigue un estilo funcional con variables inmutables (val) y mutables (var), y respeta la precedencia de operadores.

## Características

- Variables inmutables (`val`) y mutables (`var`)
- Funciones built-in (print, length, sum, sqrt)


## Requisitos previos 
Con instrucciones para instalar en
#### Linux (Debian)


- Python 3.8 o superior<br>
`
sudo apt install -y python3-full python3-pip`<br>
`sudo apt install python3-pip python3-venv`<br>
`sudo apt install pipx`<br>

- antlr4 <br>
`pip3 install --user antlr4-tools`<br>
Si no funciona<br>
`pipx install antlr4-tools`<br>
--------------------------------------
`echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`<br>
`source ~/.zshrc`


- Java Runtime (para ANTLR)<br>
`
sudo apt install default-jre
`
## Instalacion

### 1. Ubicarse en la carpeta
`Risco-V1`

### 2. Crear y activar entorno virtual
`python3 -m venv venv`<br>
`source venv/bin/activate`

### 3. Instalar dependencias
`pip install antlr4-python3-runtime==4.13.2`

### 4. Generar el parser
`chmod +x generar.sh`<br>
`./generar.sh`


 ## ¿Cómo usar RISCO?
 ### Modo interactivo:
`python src/risco.py`
 ### Ejecutar un archivo:
 - Crea un archivo con extensión .rc<br>
`python src/risco.py Carpeta/nombre_del_archivo.rc`
 ###
