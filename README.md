# MFront Sublime Text syntax
Sublime Text configuration files for syntax highlight, commenting and completions of [MFront](https://github.com/thelfer/tfel) code.

Files description:
* `MFront*`: paste these files in your User folder.
* `scrap_mfront_keywords.py`: generates the list of keywords used in the syntax file by extracting them from the TFEL website.

# UTF-8 support
MFront [supports UTF-8](https://thelfer.github.io/tfel/web/unicode.html).

* Pros: improved readability and closer to mathematical notation
* Cons: harder to edit and debug (non-ASCII characters are replaced by "`tfel_unicode_mangling_****`" in debug messages)

The provided syntax file defines a custom scope named "`aesthetics`". You can then stylize this scope in your `*.sublime-color-scheme` (Preferences > Customize Color Scheme):
```json
{
    "variables": {},
    "globals": {},
    "rules":
    [
        {
            "name": "MFront > Del",
            "scope": "aesthetics.partial-derivative.mfront",
            "foreground": "#a9c4fc",
            "font_style": "italic"
        }
    ]
}
```
which will display `∂²I3_∂C²` as $${\color{SkyBlue}\partial^2}\texttt{I3}{\color{gray}\\_}{\\!\color{SkyBlue}\partial\\!}\texttt{C}{\color{SkyBlue}{}^2}$$.

