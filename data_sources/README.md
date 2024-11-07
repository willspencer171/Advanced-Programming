# Week 2: Data Sources

## Weekly Learning Outcomes

> - Identify different data sources and how they are formatted and encoded (MLO 1)
> - Pull data into a program from different sources (MLO 2)
> - Clean and reformat data into a structure required by your program (MLO 2)

<details><summary><h2>Reading for this Week</h2></summary>

### Core Reading

#### Lesson 1

[Unicode Consortium](www.unicode.org)

[International Standard ISO/IEC 10646](https://www.iso.org/standard/76835.html)

Not much reading this week!

</details>

## Lesson 1: Data Encoding

### Base Conversions

First, let's have a quick look at numerical bases. Typically, in day to day life, we use base 10 mathematics (numbers range from 0 to 9). Computers understand things in binary, however (numbers 1 and 0, representing the states on and off). This means that we need to be able to convert binary to denary (or decimal) and back again so that both we and computers can understand maths.

The number fifteen in base 10 is `15`, while the same in base 2 is `1111`. immediately, we can see that there is an issue of compression and legibility when using binary. To overcome this, we use other bases such as octal (base 8) and hexadecimal (base 16). The number `15` in octal is `17` (1x8 + 7x1) and in hexadecimal is `F` (since the numbers range from 0-9, A-F). This is really useful when looking at larger numbers like 127 for example. In binary, this is `1111111`, `177` in octal and `7F` in hex.

Each place in a number represents a power of the base. Starting from the right, each position is $base^0$, $base^1$, $base^2$, $base^3$ etc. Four places of base 2 can therefore only add to 15, while the same in hexadecimal can add to 65,535 ($16^4$)

A proper conversion method between any two bases can be found at [Maths is Fun](https://www.mathsisfun.com/base-conversion-method.html) and it genuinely is fun to think about. Not so useful to talk about the decimal conversion since computers represent floating points differently to how we do in written practice, but it's a fun exercise when you're not in the context of computing.

### Encoding

Enough about numerical representation. Onto string representation!

How does a computer show us characters on our screens? How does it know from a series of 1s and 0s which character we want? **Character encoding** is your answer here.

#### ASCII

ASCII was one of the first, and simplest ways of representing binary numbers as characters. ASCII (and other encoding methods) is basically a map converting numbers to characters. ASCII uses 7 bits (for a maximum of 128 code points) to represent all English printable characters, as well as spaces, special characters and newline markers like `\n`. This character map can be found ubiquitously [online](https://www.ascii-code.com) (this site includes the extended ASCII set, which uses 8 bits).

#### Unicode

ASCII isn't all-encompassing (the A stands for American after all) so how do people living in countries with other character sets (particularly Chinese and related languages) write with a computer? Enter Unicode

Unicode is a character encoding that operates using 4 (actually 6) bytes of hexadecimal to convert numbers to characters. This far extends the ASCII character set to a maxmimum of 1,114,112. This gargantuan number is broken down into 17 'planes', each of $16^4$ available code spaces. Of these 1,114,112, about 800,000 remain unallocated. However, it is useful that we have these 17 different planes to separate math symbols from Latin and those from Sino-Tibetan characters.

Unicode isn't itself an encoding system, but a family of encodings. UTF-8, -16 and -32 (Unicode Transformation Formats) are the actual encodings used to map numbers to a character. UTF-8 is the most popular. It is a variable-length encoding format that can represent Unicode characters with a minimum of 1 byte (8-bits). This means really space-efficient access to the extended ASCII set of 255 characters, with extensibility to more characters by using more bytes. UTF-16 is the equivalent, but with a minimum of 2 bytes, which is good for getting to code points higher than the extended ASCII (limited practical use, really, but is often used in operating systems). UTF-32 is a fixed-width format that uses all 4 bytes, regardless of which characters are used. This is great for systems where fixed memory allocation is important, but isn't really that popular anyway.

UTF-8 is the most popular encoding format on the Internet, and is the standard for file formats like XML and HTML. Python also uses UTF-8 by default

## Lesson 2: File Formats

In this lesson, we talk about different file formats, particularly `.csv`, `.xml` and `.json`.

### Structured vs. Unstructured Formats

When we talk about file formats, they can fit into either structured (or semi-structured) and unstructured formats. There are fewer unstructured formats, but these consist primarily of text, with little to no metadata about the contents of the file. Structure is introduced to a file format when information about how the document is laid out (style) or objects within the document are labelled (markup).

### Comma-Separated Values `.csv`

CSV files are very simple structured files that work by using a delimiter to separate items. Typically, that delimiter is a comma (hence the name), but it can realistically be anything. This format can be easily manipulated using tools in vanilla Python, as well as with packages like Pandas.

```python
# With built in module csv
import csv
with open("mycsv.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

# Or in Pandas
import pandas as pd
data = pd.read_csv("mycsv.csv")
```

### eXtensible Markup Language `.xml`

XML was developed in the 1970s as a way of adding meaning and structure to otherwise unstructured data. Data is given metadata using tags and other information within those tags. Many believe it to be overly complex, but it has given rise to some important technologies like HTML and modern Microsoft file types (like `.docx`, `.xlsx` and `.pptx`).

We see XML tags most commonly in HTML files, but they originally have a bit of a more arbitrary semantic as in, you can name a tag with anything, like `<game name>` or `<heres a tag name>` rather than the shorter `<body>` or `<html>` tags.

Honestly, I don't like XML, it's ugly and it's why I write the least amount of HTML I can if I ever do anything with web development.

### JavaScript Object Notation `.json`

This is a much nicer file format for giving metadata to data. It works almost exactly like a dictionary and, in fairness, so could XML if you format it the right way, but still. It's structured like a dictionary. It was originally developed as a lightweight transfer file for asynchronous web technologies, but has found further use outside of JavaScript in languages like Python.

Here's an example:

```json
"personal details": {
    "name": "Ross Spectre",
    "age": 24,
    "height": 1.81
}
```

Beautiful. Mwah. Objects can contain strings, integers, real, and list objects

### YAML Ain't Markup Language `.yaml`

This language is similar to JSON, but a little different in that it uses indentation to introduce structures to the language. I'm kinda bored so I'm not gonna talk much more about it. Specification can be found [here](https://yaml.org/spec/1.2.2/#21-collections)

There's some activity stuff where I make some XML and JSON files so have a look at them I guess :)
