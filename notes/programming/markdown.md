# Markdown

Markdown is a wonderful language to write quick text. All this site is write
with markdown.

## The language

Mardown is made to quickly make readable enchanced texts. Here is some element
of the langugage.

### paragraph and end of line

A paragraph is just some lines
if you rally want to put a end of line you would
have to put four space at the end of the line    
There it is.

    A paragraph is just some lines
    if you rally want to put a end of line you would
    have to put four space at the end of the line    
    There it is.

### links

In order to pout some links, you just ahev to put the text between `[]` and the
link between `()`

    [Links](http://plop.me)

[Links](http://plop.me)

or you can just put the links between `<>`: `<http://plop.me>` give
<http://plop.me>

### Bold, Italic, Code line

To put some text in blod just write it between two `**` or two `__`, for
instance `**bold**` and `__bold__` give **bold** and __bold__.

To put some text in italic it the same with just on symbol: `*italic*` and
`_italic_` give *italic* and _italic_.

To put some code put it between to ``` for instance ```curl ifconfig.me``` give
`curl ifconfig.me`

### Title

To make a title just put a `#` before it, the number of `#` would define the depth
of the title:

    # Title 1
    ## Title 2
    ### Title 3
    #### Title 4
    ##### Title 5
    ###### Title 6

# Title 1
## Title 2
### Title 3
#### Title 4
##### Title 5
###### Title 6

### Images

To insert some image it is very similar to the links: `![alt](image address)`

### Code

To insert a code bloc just put 4 space before each line. To use sytax coloration
the first line of the bloc should be in the form `::langagename`:

    ::pyton
    print 'this is a python bloc code'
    for elem in list:
        print elem

### Quote

To quote something put a `>` before each line of the quotation or a single `>`
before the entiere paragraph:

> this is a simple quote.

### Lists

There is two type of lists, the bullet point and the numbered one, for the
bullet one you should just put a `*` or a `+` or a `-` before each line:

    * elem1
    * elem2
    * elem3

* elem1
* elem2
* elem3

for the numbered one just put the number before each element:

    1. elem1
    2. elem2
    3. elem3

1. elem1
2. elem2
3. elem3

[source in french](http://progmod.org/tutoriel/3/utilisez-markdown/)

## Convert

What is wonderful is that you can convert markdown files to html with the bash
`mardown` command.

