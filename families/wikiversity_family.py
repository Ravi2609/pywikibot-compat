# -*- coding: utf-8  -*-
import family

__version__ = '$Id$'

# The Wikimedia family that is known as Wikiversity

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikiversity'

        self.languages_by_size = [
            'en', 'fr', 'ru', 'beta', 'de', 'cs', 'it', 'pt', 'es', 'ar', 'el',
            'sv', 'fi', 'ja',
        ]

        if family.config.SSL_connection:
            self.langs = dict([(lang, None) for lang in self.languages_by_size])
        else:
            self.langs = dict([(lang, '%s.wikiversity.org' % lang) for lang in self.languages_by_size])


        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': [u'Wikiversity', self.namespaces[4]['_default']],
            'ar': u'ويكي الجامعة',
            'cs': u'Wikiverzita',
            'el': u'Βικιεπιστήμιο',
            'es': u'Wikiversidad',
            'fi': u'Wikiopisto',
            'fr': u'Wikiversité',
            'it': u'Wikiversità',
            'pt': u'Wikiversidade',
            'ru': u'Викиверситет',
        }
        self.namespaces[5] = {
            '_default': [u'Wikiversity talk', self.namespaces[5]['_default']],
            'ar': u'نقاش ويكي الجامعة',
            'cs': u'Diskuse k Wikiverzitě',
            'de': u'Wikiversity Diskussion',
            'el': u'Συζήτηση Βικιεπιστημίου',
            'es': u'Wikiversidad discusión',
            'fi': u'Keskustelu Wikiopistosta',
            'fr': u'Discussion Wikiversité',
            'it': u'Discussioni Wikiversità',
            'ja': u'Wikiversity・トーク',
            'pt': u'Wikiversidade Discussão',
            'ru': u'Обсуждение Викиверситета',
            'sv': u'Wikiversitydiskussion',
        }

        self.namespaces[100] = {
            'ar': u'مدرسة',
            'cs': u'Fórum',
            'el': u'Σχολή',
            'en': u'School',
            'it': u'Facoltà',
            'ja': u'School',
            'sv': u'Portal',
        }
        self.namespaces[101] = {
            'ar': u'نقاش المدرسة',
            'cs': u'Diskuse k fóru',
            'el': u'Συζήτηση Σχολής',
            'en': u'School talk',
            'it': u'Discussioni facoltà',
            'ja': u'School‐ノート',
            'sv': u'Portaldiskussion',
        }
        self.namespaces[102] = {
            'ar': u'بوابة',
            'el': u'Τμήμα',
            'en': u'Portal',
            'fr': u'Projet',
            'it': u'Corso',
            'ja': u'Portal',
        }
        self.namespaces[103] = {
            'ar': u'نقاش البوابة',
            'el': u'Συζήτηση Τμήματος',
            'en': u'Portal talk',
            'fr': u'Discussion Projet',
            'it': u'Discussioni corso',
            'ja': u'Portal‐ノート',
        }
        self.namespaces[104] = {
            'ar': u'موضوع',
            'en': u'Topic',
            'fr': u'Recherche',
            'it': u'Materia',
            'ja': u'Topic',
        }
        self.namespaces[105] = {
            'ar': u'نقاش الموضوع',
            'en': u'Topic talk',
            'fr': u'Discussion Recherche',
            'it': u'Discussioni materia',
            'ja': u'Topic‐ノート',
        }
        self.namespaces[106] = {
            'ar': u'مجموعة',
            'de': u'Kurs',
            'en': u'Collection',
            'fr': u'Faculté',
            'it': u'Dipartimento',
        }
        self.namespaces[107] = {
            'ar': u'نقاش المجموعة',
            'de': u'Kurs Diskussion',
            'en': u'Collection talk',
            'fr': u'Discussion Faculté',
            'it': u'Discussioni dipartimento',
        }
        self.namespaces[108] = {
            'de': u'Projekt',
            'fr': u'Département',
        }
        self.namespaces[109] = {
            'de': u'Projekt Diskussion',
            'fr': u'Discussion Département',
        }
        self.namespaces[110] = {
            'fr': u'Transwiki',
            'ja': u'Transwiki',
        }
        self.namespaces[111] = {
            'fr': u'Discussion Transwiki',
            'ja': u'Transwiki‐ノート',
        }
        self.cross_allowed = [
            'ja',
        ]
        # CentralAuth cross avaliable projects.
        self.cross_projects = [
            'wikipedia', 'wiktionary', 'wikibooks', 'wikiquote', 'wikisource', 'wikinews',
            'meta', 'mediawiki', 'test', 'incubator', 'commons', 'species'
        ]

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if family.config.SSL_connection:
        def hostname(self, code):
            return 'secure.wikimedia.org'

        def protocol(self, code):
            return 'https'

        def scriptpath(self, code):
            return '/%s/%s/w' % (self.name, code)

        def nicepath(self, code):
            return '/%s/%s/wiki/' % (self.name, code)
