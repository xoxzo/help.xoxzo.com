# README
Xoxzo's Help Center

This document serves as a quick guide and reminder on how to work with Xoxzo's
help center using Markdown and Pelican.

## Quickstart

### Preparing your environment

    virtualenv -p python3.4 venv
    source venv/bin/activate
    pip install -r requirements.txt
    make build

### Creating the html

After preparing your environment, you can create contents by creating .md files
in the content directory. Before you start working, pull the latest from GitHub
first:

    git pull origin master

Once you've written your articles,

    make html
    make serve
    OR 
    make devserver # that will do make html and make serve

and access *localhost:8000* via your browser to make sure everything looks ok.

### Pushing to GitHub

If everything looks good, commit and push it to GitHub:

    git add <file>
    git commit
    git push origin master
    make github

## Writing contents

### Filename

Please follow the format of the filenames that you see, i.e append the language
at the end of the file name after the filename itself:

    i-have-forgotten-my-password-en.md
    i-have-forgotten-my-password-ja.md

### Category / Subcategory

Categories are decided by the directory which you have your .md files in. Basically
this means we'll want only one category for an article, so choose carefully
which category your article can be in and only create a new directory (category)
when there are no suitable categories.

You need to specify metadata for subcategory like this:

    Category: category/subcategory

### Metadata

These metadata is required for all articles

    Title: 
    Date: 
    Slug:
    Lang:
    Category:

#### Translations

It is mandatory to specify **Lang** metadata for each article,
like this:

    Title: I have forgotten my password
    Date: 2017-03-13 11:21
    Slug: i-have-forgotten-my-password
    Lang: en
    Category: Xoxzo Cloud Telephony Platform/Account

#### Theme Translations
To translate string in templates, make the string translatable:

    {% trans %}Who we are ?{% endtrans %}

Then run:

    make pot_translation
    make update_translation

This will create translation file in `locales/ja/LC_MESSAGES/messages.po`. Translate
the string and then run:
    
    make compile_translation
    make html
