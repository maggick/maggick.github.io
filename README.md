# Blog

This blog is:
  * publish with [Pelican] (blog.getpelican.com) a static blog generator
  * hosted by [github](github.com) with github pages

I use [ghp-import](github.com/davisp/ghp-import) to publish the content on the
site with the gh-pages branch of the blog project:

  pelican && ghp-import output && git push origin gh-pages

The theme is based on Maggner theme, created by Templateify and adapted to
pelican by [Klaus Laube](https://github.com/kplaube/maggner-pelican).
To use it a little preparation is necessary:

On the theme directory execute:

  gem install sass
  gem install compass
  (aptitude install / pacman -S / whatever nodejs)
  npm install grunt
  npm install grunt-contrib-compass
  npm install grunt-contrib-watch
  grunt

This commands will deploy an environment where you can use the theme.

