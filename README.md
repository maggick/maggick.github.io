# My personal website.

This project is my actual website, my window on the cyberspace.

It is the fourth version of my website. You would found more information in the
about website section.

## Blog

This blog is:
  * publish with [Pelican] (http://blog.getpelican.com) a static blog generator
  * hosted by [github](https://github.com) with github pages

I use [ghp-import](https://github.com/davisp/ghp-import) to publish the content
of the blog on my github user pages with a dedicated repository:

  pelican && ghp-import output && git push git@github.com:maggick/maggick.github.io.git gh-pages:master

## Theme

The theme is based on Maggner theme, created by Templateify and adapted to
pelican by [Klaus Laube](https://github.com/kplaube/maggner-pelican) with
my personal modifications in
[a fork of the project](https://github.com/maggick/maggner-pelican).
To use it a little preparation is necessary:

On the theme directory execute:

    gem install sass
    gem install compass
    (aptitude install / pacman -S / whatever nodejs)
    npm install grunt-cli grunt
    npm install grunt-contrib-compass
    npm install grunt-contrib-watch
    grunt

This commands will deploy an environment where you can use the theme.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="b
order-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms
/" property="dct:title">This website</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="lol" p
roperty="cc:attributionName" rel="cc:attributionURL">Matthieu Keller</a> is licensed under a <a rel="license" href="http://cr
eativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br />
