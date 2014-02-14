# About This Website

This website is hosted at [maggick.github.com](maggick.github.com) and is
generated with [MDwiki](http://dynalon.github.io/mdwiki/#!index.md).

## History

This is the fifth version of this website :

* The first version was an home made website. Entirely write in HTML, CSS and PHP. It was a great exercise 
  to learn the base of web 3-tier architecture with a client, a server and a database.
* The second version was powered by Word Press. In fact this was a classic WP with a plug-in for 
  multi-languages and some simple changes in the default pages style.
* The third was generated using Middleman, a static site generator in Ruby wich
  generate HTML pages from markdown files.
* The fourth was build in html using the `markdown` command.

## Reasons that killed old versions

* The First version was huggly and almost without content.
* With the Word Press version I always have to use the online interface to create or update articles and pages.
  Moreover the data were on the site database, meaning that as I do not save them, they were not backuped as 
  my usual data.
* With this version, I write pages in [Markdown format](https://github.com/github/markup#readme) 
  directly on my computer with my favorite text editor, commit them on GitHub and finally put them on the server.
  There is no more database (meaning no more commentary, see the [About Me section](/about/me/#contact) for contact).
  The site is entirely static.
* The fourth version was not far from this one but it was long to make a small
  correction on a page (a spell correction for instance). I had to re-build the
  entire website and it was not autmoaticly done.

## Technically

I use the [MDwiki](http://dynalon.github.io/mdwiki/#!index.md) CMS in order to
directly generate HTML pages from the markdown files. This build is done in
javascript, meaning the work is totaly deported on the client side.
Moreover I use [github pages](http://pages.github.com/) to host my website. This
mean that every push to my github repository will lead to a direct update of the
website !

## License

This site is licensed under [WTFPL](www.wtfpl.net).

