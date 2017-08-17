# IOS auto string obfuscation

### Intro
Using a [library](https://medium.com/theappspace/increase-the-security-of-your-ios-app-by-obfuscating-sensitive-strings-swift-c915896711e6) found in the web, and writing a script to do it automatically.

Way to use the library,
	1. Choose a salt key 
	2. Obfuscate your string
	3. replace your string with the output of Obfuscation

	This script automates step 2 & 3 

### Dependencies
	1. parser.py
	2. Obfuscator.swift

### How to use
* must be in same directory 

1. include Obfuscator.swift into xcode project
2. add this line of code into the file u want to obfuscate
	* `let o = Obfuscator(withSalt: [AppDelegate.self, NSObject.self, NSString.self])` 
	* change the salt key to your own preference
	* Strings that want to be obfuscated need to be inside the tag `/*lapsap*/"<string>"/*lapsap*/`
3. edit parser.py, change cipher to the salt key of your choise
4. Give excutable permission `chmod +x parser.py`
5. `./parser.py <filename>`

![image](http://i.imgur.com/9cj9pNO.png)

### output 
	1. <file>      (obfuscated file)
	2. ori_<file>  (original file)
