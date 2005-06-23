#!/usr/bin/python
# -*- coding: utf-8  -*-

import re
import wikipedia

class SinglePageGenerator:
    '''
    Pseudo-generator
    '''
    def __init__(self, page):
        self.page = page

    def generate(self):
        yield self.page

class AllpagesPageGenerator:
    '''
    Using the Allpages special page, retrieves all articles, loads them (60 at
    a time) using XML export, and yields title/text pairs.
    '''
    def __init__(self, start ='!'):
        self.start = start

    def generate(self):
        for page in wikipedia.allpages(start = self.start):
            yield page

class ReferringPageGenerator:
    '''
    Yields all pages referring to a specific page.
    '''
    def __init__(self, referredPage, followRedirects = False):
        self.referredPage = referredPage
        self.followRedirects = followRedirects

    def generate(self):
        for page in self.referredPage.getReferences(follow_redirects = self.followRedirects):
            yield page

class CategorizedPageGenerator:
    '''
    Yields all pages in a specific category.
    '''
    def __init__(self, category, recurse = False):
        self.category = category
        self.recurse = recurse

    def generate(self):
        for page in self.category.articles(recurse = self.recurse):
            yield page

class LinkedPageGenerator:
    '''
    Yields all pages linked from a specific page.
    '''
    def __init__(self, linkingPage):
        self.linkingPage = linkingPage

    def generate(self):
        for page in self.linkingPage.linkedPages():
            yield page

class TextfilePageGenerator:
    '''
    Read a file of page links between double-square-brackets, and return
    them as a list of Page objects. 'filename' is the name of the file that
    should be read.
    '''
    def __init__(self, filename):
        self.filename = filename

    def generate(self):
        site = wikipedia.getSite()
        f = open(self.filename, 'r')
        R = re.compile(r'\[\[(.+?)\]\]')
        for pageTitle in R.findall(f.read()):
            parts = pageTitle.split(':')
            i = 0
            try:
                fam = wikipedia.Family(parts[i], fatal = False)
                i += 1
            except:
                fam = site.family
            if parts[i] in fam.langs:
                code = parts[i]
                i += 1
            else:
                code = site.lang
            pagename = ':'.join(parts[i:])
            site = wikipedia.getSite(code = code, fam = fam)
            yield wikipedia.Page(site, pagename)
        f.close()

class PreloadingGenerator:
    """
    Wraps around another generator. Retrieves as many pages as stated by pageNumber
    from that generator, loads them using Special:Export, and yields them one after
    the other. Then retrieves more pages, etc.
    """
    def __init__(self, generator, pageNumber = 60):
        self.generator = generator
        self.pageNumber = pageNumber

    def preload(self, pages):
        try:
            wikipedia.getall(wikipedia.getSite(), pages, throttle=False)
        except wikipedia.SaxError:
            # Ignore this error, and get the pages the traditional way later.
            pass

    def generate(self):
        # this array will contain up to pageNumber pages and will be flushed
        # after these pages have been preloaded.
        somePages = []
        i = 0
        for page in self.generator.generate():
            i += 1
            somePages.append(page)
            # We don't want to load too many pages at once using XML export.
            # We only get 20 at a time.
            if i >= self.pageNumber:
                self.preload(somePages)
                for refpage in somePages:
                    yield refpage
                i = 0
                somePages = []
        # preload remaining pages
        self.preload(somePages)
        for refpage in somePages:
            yield refpage

