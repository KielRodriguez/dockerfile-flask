###Introducción a Dockerfile, sintaxis y comandos básicos para construir y correr un contenedor Docker

####Alcance de la charla:
- Describir las instrucciones básicas  para construir un Dockerfile
- Crear un ejemplo con flask/python

#### FROM

La instrucción FROM configura la imagen base para futuras instrucciones, 
un Dockerfile válido debe iniciar un la instrucción FROM.

```
FROM <image> [AS <name>]
FROM <image>[:<tag>] [AS <name>]
```
#### ARG

#### ENV

#### RUN

La instrucción RUN ejecuta cualquier comando en un una nueva capa por encima 
de la actual imagen y se hará un commit con el resultado, esto será usado para 
subsecuentes instrucciones.

```
RUN <command>
```

#### LABEL

La instrucción LABEL  agrega metadatos a una imagen. Un LABEL es un par de clave-valor.

```
LABEL <key>=<value> <key>=<value> <key>=<value> ...
```

#### WORKDIR


#### ADD
La instrucción ADD permite agregar archivos o directorios desde el contexto a la construcción de la imagen.
```
ADD [--chown=<user>:<group>] <src>... <dest>
```

#### COPY

#### EXPOSE

La instrucción EXPOSE informa a Docker que el contenedor está escuchando sobre un específico puerto de red.

```
EXPOSE <port> [<port>/<protocol>...]

EXPOSE 80/tcp
EXPOSE 80/udp
```

#### CMD

El propósito de  la instrucción CMD es para proporcionar una ejecución por default para el contenedor.

```
CMD ["executable","param1","param2"]
CMD ["param1","param2"]
CMD command param1 param2 (shell form)
```
