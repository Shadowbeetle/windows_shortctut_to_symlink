sc2sl is a simple python3 script that will recursively crawl through a folder and turn every windows shortcut / windows link - or whatever their proper name is - to symlinks. 

# Motivation
If you are anything like me, you cannot really think in directories, butin labels or categories. One file can obviously belong to multiple categories. The easiest way to achieve something similar is done by using shortcuts on windows and symlinks on unix. Now what happens if you move from windows to unix and your lifesaving shortcuts become useless in an instance? (Well more like in 10-20 minutes.)

One thing to do is to crawl through your previous directories and turn all your shortcuts into symlinks. This simple python 3 script does exactly that.

sc2sl is a simple python3 script that will recursively crawl through a folder and turn every windows shortcut / windows link - or whatever their proper name is - to symlinks. 

# usage

**make sure you have python 3 installed**

`python3 sc2sl.py <root> <old> <new> [-c <encoding>] [--remove]`

`**root**`: the directory you whish to crawl

`**old**`: the old directory pattern you wish to switch. Does not have to begin with the drive letter

`**new**`: the new directory pattern you wish to use. Has to start with `/`

`**-c**`,`**--encoding**`: the encoding your previous operating system used. Defaults to ISO-8859-1. In Eastern-Europe it's usually ISO-8859-2. [Check here for further info](https://en.wikipedia.org/wiki/ISO/IEC_8859-1).

`**--remove**`: add this switch is you wish to remove the old shortcuts in one run.
