
## Software

Why have one program that does a few common sense things well when you can have multiple programs that do one or two things really badly!

| Program   | Description                                                    |
|-----------|----------------------------------------------------------------|
| apt-get   | install: `apt-get install <prgm>`                              |
|           | remove: `apt-get remove <prgm>` add `--purge` to remove configs|
| apt-cache | search for programs you can install: `apt-cache search <prgm>` |
| dpkg      | list programs you have installed: `dpkg -l`                    |

### Updates, Search, and List

	sudo apt-get update
	sudo apt-get upgrade

Now to just see the list of packages that would be upgraded:

	sudo apt-get upgrade -u

Now some packages will get `kept back` which seems to be some strange apt-get issue. To
update your system completely, do:

    sudo apt-get dist-upgrade

You can also search for software by:

    apt-cache showpkg [packagename]
    
Or list all packages installed on the computer by:

    dpkg -l

