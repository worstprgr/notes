# Windows Registry
Adding an entry to the context menu  
Create an *.reg file and c/p the following code block - Note: You must escape `\` with `\\`  
```regedit
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\<Name of your Programm>]
@="<Your Text on the Context Menu>"
"Icon"="<Path to the icon file -> .ico or .exe>"

[HKEY_CLASSES_ROOT\Directory\Background\shell\<Name of your Programm>\command]
@="<Path to the Executable/Bat/PS>" "<Optional Argument1>" "<Optional Argument2>"
```

Passing the current path to your programm with `%v=.`    
```regedit
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\<Name of your Programm>]
@="<Your Text on the Context Menu>"
"Icon"="<Path to the icon file -> .ico or .exe>"

[HKEY_CLASSES_ROOT\Directory\Background\shell\<Name of your Programm>\command]
@="C:\\SomePath\\WindowsTerminal.exe" "nt" "--startingDirectory=%v."
```
