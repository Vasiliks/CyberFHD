# -*- coding: utf-8 -*-
# created by Vasiliks 28.12.2025

from os import environ
from Components.Language import language
from gettext import bindtextdomain, dgettext, gettext
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

def localeInit():
    environ["LANGUAGE"] = language.getLanguage()[:2]
    bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, "Extensions/%s/locale" % PluginLanguageDomain))


def _(txt):
    return (dgettext(PluginLanguageDomain, txt), '')[txt == '']

PluginLanguageDomain = "SetupCyberFHD"
localeInit()
language.addCallback(localeInit)
