# Match Strike's Django Template

This is a template for new Django projects that [Match Strike](http://matchstrike.net/) maintains.

## Requirements

django 1.2
[django-command-extensions (django_extensions)](http://code.google.com/p/django-command-extensions/)
[django-compress](http://south.aeracode.org/)
[south*](http://south.aeracode.org/)
[Django Debug Toolbar*](http://github.com/robhudson/django-debug-toolbar)

*These things are commented out by default. If you leave them commented out, you can get by without installing them. Similarly, if you'd like to make do without django_extensions or django_compress, comment out their corresponding lines in settings.py's INSTALLED_APPS list. I highly recommend against that though. For complicated django apps, these four extras will make your life much easier.

## Overview

### settings.py and local_settings.py
I've broken settings.py into settings.py and local_settings.py. As you might assume based on the names, put settings that are specific to an instance of the code base in local_settings.py and put settings that are standard across all instances of the code base in settings.py. Don't commit local_settings.py to your repository because you'll be keeping passwords and such in it. Instead, keep local_settings.template.py updated with an example local config for your application (again, don't use real passwords).

### context_processors.base()
I've added a context processor that adds these nice variables to the default context: DEBUG, SITE_NAME, path, and domain.

### Admin
django.contrib.admin and ulrs are enabled by default.

### assets/
The structure is fairly straightforward. You'll want to tell your repository to ignore assets/css/site.r[0-9]*.css and assets/js/site.r[0-9]*.js if you decide to use django-compress. On a related note, I use /assets/users/ to store user uploaded media. If you do the same, you'll probably also want to tell your repo to ignore all non-directories in assets/users/.

#### Javascript
javascript: By default we include the jQuery form plugin and a [Google Analytics plugin written by SquareFACTOR](http://squarefactor.com/words/2009/feb/13/google-analytics-jquery-plugin/). Note that we do not include jQuery itself. base.phtml instead links [Google's non-minified jQuery.js file](http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.js) when in debug mode and [Google's minified jQuery.js file](http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.min.js) when DEBUG==False.

#### assets/googlexxxxxxxxxxx.html, assets/robots.txt, assets/img/favicon.ico
When you deploy your application, you'll want to configure your web server to serve all three of these files at the root of your application. Follow the links for a brief explanation of what they are:
* [googlexxxxxxxxxxx.html](http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=35658)
* [robots.txt](http://en.wikipedia.org/wiki/Robots_exclusion_standard)
* [assets/img/favicion.ico](http://en.wikipedia.org/wiki/Favicon)

### templates/
We use *.phtml* instead of *.html* for our templates so that we can tell our text editors to do syntax highlighting for .phtml files specifically as django template files rather than as just HTML files. If that bothers you, all you need to do is rename the files to *.html, change home.phtml in urls.py, an the you should be good to go. Aside from that, there isn't too much else to note. Be sure to read the comments in the templates (in particular, look at the big one at the end of base.phtml) and look to home.phtml for a nice example of using base.phtml to it's fullest.

##Step by step:

1. Export project_template to wherever you need it to be.
2. Copy local_settings.template.py to local_settings.py.
3. In settings.py change:
	* *ADMINS*
	* *SITE_NAME*
	* *INSTALLED_APPS* - uncomment south if you want it, comment out compress and	django_extensions if you don't want to use either of those.
	* *COMPRESS_CSS* (see django_compress documentation)
	* *COMPRESS_JS* (see django_compress documentation)
4. In local_settings.py change:
	* *DATABASES*
5. Tell your repository to ignore local_settings.py, assets/css/site.r[0-9]*.css, and assets/js/site.r[0-9]*.js
6. By default, your app will generate a log called site.log when you use the logging library, and it will use site.css and site.js. I like to rename those to something that reflects the name of my application. For example, for a site where SITE_NAME="Match Strike", I'd rename those files to matchstrike.css, matchstrike.js, and matchstrike.log. If you'd like to do the same, rename site.css and site.js. Then change those file names in setting.py's COMPRESS_CSS and COMPRESS_JS vars. To change the name of the log file your site will create, change the filename property of the logging configuration in local_settings.py
7. Replace img/favicon.png with something more appropriate.
8. Develop!

## Copyright

Copyright (c) 2010 Thomas Welfley. See [LICENSE](http://github.com/thomasw/matchstrike_django/blob/master/LICENSE) for details.