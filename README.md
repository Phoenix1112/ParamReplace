# ParamReplace

ParamReplace is a program for changing the values of query strings in url addresses.You can use this program together with the waybackurls program. this program has been tried only on linux.

# install

```
git clone https://github.com/Phoenix1112/ParamReplace.git

cd ParamReplace

pip3 install -r requirements.txt

```

# usage

There are 3 different methods in the program(Default method 3). Replaces the default keyword FUZZ with the value. 

Example input file: 

```
cat urls.txt

https://www.example.com/?id=3
https://www.example.com/?page=1&source=test
https://www.example.com/?path=true&admin=true&id=5

```

# replace values with --method 1

```

cat urls.txt | python3 ParamReplace.py --stdin --method 1

or

python3 ParamReplace.py --list urls.txt --method 1


output:
-------

https://www.example.com/?id=FUZZ
https://www.example.com/?page=FUZZ
https://www.example.com/?path=FUZZ
```

# replace values with --method 2

```

cat urls.txt | python3 ParamReplace.py --stdin --method 2

or

python3 ParamReplace.py --list urls.txt --method 2


output:
-------

https://www.example.com/?id=FUZZ
https://www.example.com/?page=FUZZ&source=FUZZ
https://www.example.com/?path=FUZZ&admin=FUZZ&id=FUZZ

```

# replace values with --method 3 (This is Default method.. )

You do not need to use the --method 3 parameter. Also You can change the FUZZ keyword with the --param parameter.

```

cat urls.txt | python3 ParamReplace.py --stdin --param NewKeyword

or

python3 ParamReplace.py --list urls.txt --param NewKeyword


output:
-------

https://www.example.com/?id=NewKeyword
https://www.example.com/?page=NewKeyword
https://www.example.com/?page=NewKeyword&source=NewKeyword
https://www.example.com/?path=NewKeyword
https://www.example.com/?path=NewKeyword&admin=NewKeyword&id=NewKeyword

```
