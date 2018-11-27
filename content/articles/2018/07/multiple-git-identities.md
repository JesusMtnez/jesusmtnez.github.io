Title: Managing configuration with multiple git identities
Date: 2018-07-31
Category: Git
Tags: git,vcs,,programming,configuration,dotfiles
Slug: managing-config-with-multiple-git-identities
Lang: en

Git is a versioning control system tools for source code that we can find anywhere nowadays. I use it for almost everything: managing my [dotfiles](https://gitlab.com/JesusMtnez/dotfiles), in all my personal projects and, of course, at work. But using _git_ at work, where it is very common to have multiple identities, could be quite tedious.

<img style="display: block; margin-left: auto; margin-right: auto" src="{static}/images/git-logo.png">

# Problem

I use [GitLab](https://gitlab.com/JesusMtnez) to manage all my personal projects, with a automatic mirror to my [GitHub](https://github.com/JesusMtnez) account. In both services I have used the same username and email to make it easy to configure _git_. I just need to add that information to my `~/.gitconfig`

```
[user]
    name = JesusMtnez
    email = jesusmartinez93@gmail.com
```

But nowadays I'm working in a company where I have to collaborate with multiple clients. It is very common that each client requires an email account in its company domain, which has to be used to author commits. To configure it, I used to set the specific email account per repository, overriding my personal email account.

```
$ cd ~/workspaces/client01/repository
$ git config --local user.email jesus@client01.com
```

Making these configuration one or two times manually is no problem, but in the end clients tend to have multiple repositories (tons of them in some cases), making difficult to know which ones were properly configured and which not. To fix it, I made an interactive _rebase_ just to change commit's author.

# Solution

Since version 2.13, git includes a feature for **conditional includes**, allowing users to load configuration files depending where the user is in the shell session. Syntax looks like:

```
[includeIf "gitdir:/path/group/repo"]
    path = /path/to/config/file
```

- `gitdir:`: defines the condition to load the file. It could be done in two different ways:
    - `gitdir:/path/group/repo`: it will load the file when the shell session is located at repository `/path/group/repo/`
    - `gitdir:/path/group`: it will load the file when the shell session is located at any repository in  `/path/group`
- `path` path to file to load. It could be an absolute location or a file name. In the last case, it will be search at the repository or at `$HOME` if missing.

To solve the issue:

* Create a file `.gitconfig` in each client workspace containing its specific configuration:

```
$ cat  ~/workspaces/client01/.gitconfig
[user]
    email = jesus@client01.com

$ cat ~/workspaces/client02/.gitconfig
[user]
    email = jesus@client01.com

```

* Add conditional include in my global configuration to active those configuration when working on clients repositories. To do that, I added the following code to my `$HOME/.gitconfig`:

```
[includeIf "gitdir:~/workspaces/client01/"]
    path = ~/workspaces/client01/.gitconfig

[includeIf "gitdir:~/workspaces/client02/"]
    path = ~/workspaces/client02/.gitconfig
```

Doing that, each time I go inside one the repositories inside `~/workspaces/client01`, `~/workspaces/client01/.gitconfig` file is loaded and applied. The same goes for `client02`.
