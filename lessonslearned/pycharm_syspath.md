# Pitfall: PyCharm & Sys.path
### Issue
Apparently if you're working with PyCharm you're able to import modules
from a second level directory, into another second level directory.  

For me at least, it is an issue, because on other environments I get a **ModuleNotFoundError**.
This happens, because PyCharm automatically adds the project root into the **sys.path**.  

It could introduce bad practices [1] regarding your project structure and import strategies.  
Like: cyclic imports, double imports, partly imported modules

_David Beazley_ explains this topic in his talk [1]. (Link at the _links section_)


### Current State
This is our project structure:  
```Text
project-folder
    |- /core/
        |- foo.py
    |- /conf/
        |- config.py
```

Current state in _PyCharm 2023.1.3 PE_ is: you can do something like that:  
```Python
# File: /core/foo.py
import conf.config as cfg
```

And if you try to execute **core/foo.py** without PyCharm, just via console, you get
a **ModuleNotFoundError**.
```Text
Traceback (most recent call last):
  File "\modulepackageimporttest\core\foo.py", line 2, in <module>
    import conf.config as cfg
ModuleNotFoundError: No module named 'conf'
```

---
### Why?
Because PyCharm adds your root folder automatically to the **sys.path**.
It's very convenient to work with, but if you want to deploy your project to a
different environment or share it to other people, they're getting this error.

There are long and big discussions adding something manually to the **sys.path**.
To this date (2023), there's still no conses.

The exact settings are found in:
1. File -> Settings (Ctrl+Alt+S)
2. Build, Execution, Deployment
3. Console
4. Python Console
   1. Add content roots to PYTHONPATH
   2. Add source roots to PYTHONPATH

Or search for "PYTHONPATH" in the settings.

---
### Solutions?
After inhaling the talk from David Beazley (Link below) about how the Python 
import statement is working, and searching the internet - I've found those "solutions":

1. Modify **sys.path** with **sys.path.extend(["path1, path2, path3"])**
2. Using a flat structure
3. Don't import modules from different folders
4. Design it as a package

<br>

#### Point 1: Sys.path.extend()
Modifying the **sys.path** is considered as a bad practice [1], because it enables
some weird interactions if the project getting bigger and is more prone to errors/bugs.  
But in my case, I want to store unit tests in a separate **/tests/** folder, so I have 
to use this approach.

#### Point 2: Flat structure
Storing every script in the same level is fine for small projects. And since I did simple and
small projects, this issue never was a problem. But with bigger projects, I have to 
organize all files well, to prevent chaos and complexity.

#### Point 3: Just don't
This will be my way to go. It forces me to maintain a clean structure. The only exception will
be unit tests. I want them in a separate place to keep it simple.

#### Point 4: Package
_Currently_, I don't like the idea of packages. Because I never know if there's some malicious
code in the next version. And I don't have the time and expertise to audit every single package
and dependency.  
For some packages I have to bite the bullet, because they're _really_ convenient and saving me
a lot of time. E.g. numpy, matplotlib, seaborn, selenium, flask and cryptographic libraries.  
Plus it is very inconvenient for me, to set up an editable package environment every time. And it
feels not very "pythonic".

---
### Lessons learned

- a 3h talk about the import statement was very informative
- a pile of people recommending bad practices as good practices (scary)
- be aware, that an IDE configs some stuff for you, that could waste your 
  time in some later stage
- EMACS, Nano and Notepad++ are MVP

---

### Links
1. https://youtu.be/0oTh1CXRaQ0 
  (Title: David Beazley - Modules and Packages: Live and Let Die! - PyCon 2015)
2. https://peps.python.org/pep-0008/#imports
  (PEP 8 on imports)
3. https://peps.python.org/pep-0328/#relative-imports-and-indirection-entries-in-sys-modules 
  (PEP 328 on relative and absolute imports)
4. https://peps.python.org/pep-0366/
  (Changing explicit relative imports)
5. https://docs.python.org/3/reference/import.html
   (Documentation of the import statement)
