# Blog

This blog is:
  * publish with [Pelican] (http://blog.getpelican.com) a static blog generator
  * hosted by [github](https://github.com) with github pages

I use [ghp-import](https://github.com/davisp/ghp-import) to publish the content
of the blog on my github user pages with a dedicated repository:

  pelican && ghp-import output && git push git@github.com:maggick/maggick.github.io.git gh-pages:master

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
