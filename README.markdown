# Match Strike's Django Template
This is a template for new Django projects that [Thomas Welfley](http://welfley.me/) at [Match Strike](http://matchstrike.net/) maintains.

## Requirements
See the [requirements.txt](https://github.com/thomasw/matchstrike_django/blob/master/project_template/requirements.txt) file. These packages can be installed easily via PIP:

    > pip install -r /path/to/requirements.txt

## Overview
### settings.py and local_settings.py
settings.py contains the default settings for all instances of your application. The settings listed in this file should be as cross platform compatible and complete as possible so that your app can work just about anywhere. However, if you intend to publish your software publicly, do not include passwords, keys, or other sensitive data in settings.py. Use placeholder values instead.

Use a local_settings.py file to override settings.py settings for specific instances. See the [local_settings.py template](https://github.com/thomasw/matchstrike_django/blob/master/project_template/local_settings.template.py) for an example.

### context_processors.base()
A context processor has been added that provides these nice variables to the default context: DEBUG, SITE_NAME, path, and domain.

### Admin
django.contrib.admin and urls are enabled by default.

### assets/
The structure is fairly straightforward. You'll want to tell your repository to ignore assets/css/site.r[0-9]*.css, assets/js/site.r[0-9]*.js, and assets/js/contrib/.

#### Javascript
By default we include the [jQuery form plugin](http://github.com/malsup/form), a [Google Analytics plugin written by SquareFACTOR](http://squarefactor.com/words/2009/feb/13/google-analytics-jquery-plugin/), and a script that automatically adds CSRF tokens to ajax requests. Note that we do not include jQuery itself. base.phtml instead links [Google's non-minified jQuery.js file](http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.js) when in debug mode and [Google's minified jQuery.js file](http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.min.js) when DEBUG==False.

#### assets/robots.txt, assets/img/favicon.ico
When you deploy your application, you'll want to configure your web server to serve both of these files at the root of your application. Follow the links for a brief explanation of what they are:

* [robots.txt](http://en.wikipedia.org/wiki/Robots_exclusion_standard)
* [assets/img/favicion.ico](http://en.wikipedia.org/wiki/Favicon)

### templates/
We use *.phtml* instead of *.html* for our templates so that we can tell our text editors to use different syntax highlighting rules for django templates. If that bothers you, all you need to do is rename the files to *.html, change home.phtml in urls.py, an the you should be good to go.

base.phtml has markup in it that displays a warning message to users using IE 6 or below (see [ie6 no more](http://www.ie6nomore.com/) for additional information). If you intend to support IE 6, you'll need to remove that markup.

Aside from that, there isn't too much else to note. Be sure to read the comments in the templates (in particular, look at the big one at the end of base.phtml) and look to home.phtml for a nice example of using base.phtml to it's fullest.

## Step by step:
1. Export project_template to wherever you need it to be.
3. In settings.py change:
	* *ADMINS*
	* *SITE\_NAME*
	* *INSTALLED\_APPS*
	* *DEFAULT\_FROM\_EMAIL*
5. Tell your repository to ignore local\_settings.py, assets/css/site.r[0-9]*.css, assets/js/site.r[0-9]*.js, and assets/js/contrib/
6. By default, your app will generate a log called site.log when you use the logging library, and it will use site.css and site.js. I like to rename those to something that reflects the name of my application. For example, for a site where SITE\_NAME="Match Strike", I'd rename those files to matchstrike.css, matchstrike.js, and matchstrike.log. If you'd like to do the same, rename site.css and site.js. Then change those file names in setting.py's COMPRESS_CSS and COMPRESS_JS vars. To change the name of the log file your site will create, change the filename property of the logging configuration in local_settings.py
7. Replace img/favicon.ico with something more appropriate.
8. Update the copyright information in base.phtml
9. Develop!

## Copyright
Copyright (c) 2010-2011 Thomas Welfley. See [LICENSE](http://github.com/thomasw/matchstrike_django/blob/master/LICENSE) for details.