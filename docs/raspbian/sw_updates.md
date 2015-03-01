# Updating Software

## Debian Packaged Software

Why have one program that does a few common sense things well when you can have multiple programs that do one or two things really badly!

| Program   | Description                                                    |
|-----------|----------------------------------------------------------------|
| apt-get   | install: `apt-get install <prgm>`                              |
|           | remove: `apt-get remove <prgm>` add `--purge` to remove configs|
|           | upgrade: `apt-get upgrade <prgm>` to get latest                |
|           | update: `apt-get update` updates package databases             |
| apt-cache | search for programs you can install: `apt-cache search <prgm>` |
| dpkg      | list programs you have installed: `dpkg -l`                    |

### Updates, Search, and List

`apt-get` is a horrible program and a beautiful example of how not to design software. So if you want to know what packages are outdated, then you need to install this package:

	sudo apt-get install apt-show-versions

Now to figure out what is outdated, do:

	apt-show-versions -u

Now some packages will get `kept back` which seems to be some strange apt-get issue. To
update your system completely, do:

    sudo apt-get dist-upgrade

You can also search for software by:

    apt-cache showpkg [packagename]
    
Or list all packages installed on the computer by:

    dpkg -l

# Python Packages 

Alot of very useful packages are available from [PyPI](https://pypi.python.org/pypi) and can be installed using `pip`.

You can use `pip` to install and keep python libraries up to date. Unfortunately `pip` is a horrible package manager, but it could be worse ... `apt-get` anyone? Some useful, undocumented commands:

| Pip flag        | Description                        |
|-----------------|------------------------------------|
| list            | list installed packages            |
| list --outdated | list packages that can be upgraded |
| install _pkg_   | install a package                  |
| install -U _pkg_| upgrade a package                  |


Why the idiots who run `pip` don't make useful commands like `pip upgrade` or `pip outdated` I don't know. Instead there are duplicate (stupid) commands like `pip freeze` which is the same as `pip list`.

