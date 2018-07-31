Title: Gestionar configuración con múltiples cuentas de git
Date: 2018-07-22
Category: Git
Tags: git,vcs,,programming,configuration,dotfiles
Slug: managing-config-with-multiple-git-identities
Lang: es

Git es una herramienta de control de versiones de código que hoy en día podemos encontrar en casi todos lados. Yo mismo utilizo git para casi todo: gestionar mis [dotfiles](https://gitlab.com/JesusMtnez/dotfiles), en todos mis proyectos personales, y como no, en el trabajo. Y es justo en este último caso en el que usar git con múltiples cuentas se vuelve un poco tedioso.

# El problema

Yo utilizo [GitLab](https://gitlab.com/JesusMtnez) para todos mis proyectos personales, junto con un mirror automático en mi cuenta de [GitHub](https://github.com/JesusMtnez). Para configurar mi cuenta en ambos servicios he usado mi propio correo personal y el mismo nombre de usuario, de manera que para utilizar mi configuración de git solo he necesitado añadir mi usuario y mi correo eléctronico a mi `~/.gitconfig`:

```
[user]
    name = JesusMtnez
    email = jesusmartinez93@gmail.com
```

Pero actualmente me encuentro trabajando en una empresa en la que a su vez tengo que trabajar con varios clientes. Es muy común que para cada cliente tenga una cuenta de correo electrónico distinta. Para evitar trabajar con mi cuenta personal en cada cliente, solía configurar de forma local en cada repositorio el correo que queria usar, sobreescribiendo así mi correo personal de mi configuración global de git.

```
$ cd ~/workspaces/client01/repository
$ git config --local user.email jesus@client01.com
```

El hecho de tener que configurar cada repositorio a mano, a demás de pesado si el cliente tiene muchos repositorios, provocaba que se me olvidara alguno por actualizar y terminaba trabajando con mi cuenta personal hasta que me daba cuenta y hacía un _rebase_ interactivo para actualizar el autor del _commit_.

# La solución

Desde la versión 2.13, git ha includio la funcionalidad de _include_ condicionales, es decir, cargar un fichero de configuración de git según dónde nos encontremos en ese momento en nuestra _shell_. La sintaxis es:

```
[includeIf "gitdir:/path/group/repo"]
    path = /path/to/config/file
```

- `gitdir:`: nos permite definir la condición en la que se va a realizar la carga del fichero de configuración. Puede hacerse de dos maneras:
    - `gitdir:/path/group/repo`: incluirá el fichero cuando nos localicemos dentro del repositorio localizado en `/path/group/repo/`
    - `gitdir:/path/group`: incluirá el fichero cuando nos localicemos en cualquier repositorio dentro del directorio `/path/group`
- `path` localización del fichero que queremos que se cargue. Si en lugar de indicar una dirección absoluta indicáramos solo el nombre del fichero, este se buscaría dentro del repositorio o en `$HOME`.

Para solucionar el problema, hacemos lo siguiente:

* Crear un fichero `.gitconfig` en la carpeta de repositorios de cada cliente con la cuenta a utilizar en cada uno:

```
$ cat  ~/workspaces/client01/.gitconfig
[user]
    email = jesus@client01.com

$ cat ~/workspaces/client02/.gitconfig
[user]
    email = jesus@client01.com

```

* Añadir la carga de estos ficheros de forma condicional si estoy trabajando en sus repositorios. Para ello,  añadimos las siguientes entradas nuestro `$HOME/.gitconfig`:

```
[includeIf "gitdir:~/workspaces/client01/"]
    path = ~/workspaces/client01/.gitconfig

[includeIf "gitdir:~/workspaces/client02/"]
    path = ~/workspaces/client02/.gitconfig
```

De esta manera, cada vez que entremos en un repositorio dentro de `~/workspaces/client01` se aplicará el fichero `~/workspaces/client01/.gitconfig`, y de igual forma para `client02`.

# Conclusiones

