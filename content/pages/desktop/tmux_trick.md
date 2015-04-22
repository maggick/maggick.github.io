Title: tmux trick
Status: hidden

# How to synchronize tmux splits

When you have multiple servers on multiple splits of your tmux,
you may want to launch the same command on each servers. There is a versy simple
solutions : `synchronize-panes`.

In fact you just need to set this option to on in order to write the same
command on each splits.

    :setw synchronize-panes

This is a simple trick but a very useful one.

Source: [Arabesque](http://blog.sanctum.geek.nz/sync-tmux-panes/)

