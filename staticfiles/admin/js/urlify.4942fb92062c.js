/*global XRegExp*/
'use strict';
{
    const LATIN_MAP = {
        'Ã': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'A', 'Ã': 'AE',
        'Ã': 'C', 'Ã': 'E', 'Ã': 'E', 'Ã': 'E', 'Ã': 'E', 'Ã': 'I', 'Ã': 'I',
        'Ã': 'I', 'Ã': 'I', 'Ã': 'D', 'Ã': 'N', 'Ã': 'O', 'Ã': 'O', 'Ã': 'O',
        'Ã': 'O', 'Ã': 'O', 'Å': 'O', 'Ã': 'O', 'Ã': 'U', 'Ã': 'U', 'Ã': 'U',
        'Ã': 'U', 'Å°': 'U', 'Ã': 'Y', 'Ã': 'TH', 'Å¸': 'Y', 'Ã': 'ss', 'Ã ': 'a',
        'Ã¡': 'a', 'Ã¢': 'a', 'Ã£': 'a', 'Ã¤': 'a', 'Ã¥': 'a', 'Ã¦': 'ae', 'Ã§': 'c',
        'Ã¨': 'e', 'Ã©': 'e', 'Ãª': 'e', 'Ã«': 'e', 'Ã¬': 'i', 'Ã­': 'i', 'Ã®': 'i',
        'Ã¯': 'i', 'Ã°': 'd', 'Ã±': 'n', 'Ã²': 'o', 'Ã³': 'o', 'Ã´': 'o', 'Ãµ': 'o',
        'Ã¶': 'o', 'Å': 'o', 'Ã¸': 'o', 'Ã¹': 'u', 'Ãº': 'u', 'Ã»': 'u', 'Ã¼': 'u',
        'Å±': 'u', 'Ã½': 'y', 'Ã¾': 'th', 'Ã¿': 'y'
    };
    const LATIN_SYMBOLS_MAP = {
        'Â©': '(c)'
    };
    const GREEK_MAP = {
        'Î±': 'a', 'Î²': 'b', 'Î³': 'g', 'Î´': 'd', 'Îµ': 'e', 'Î¶': 'z', 'Î·': 'h',
        'Î¸': '8', 'Î¹': 'i', 'Îº': 'k', 'Î»': 'l', 'Î¼': 'm', 'Î½': 'n', 'Î¾': '3',
        'Î¿': 'o', 'Ï': 'p', 'Ï': 'r', 'Ï': 's', 'Ï': 't', 'Ï': 'y', 'Ï': 'f',
        'Ï': 'x', 'Ï': 'ps', 'Ï': 'w', 'Î¬': 'a', 'Î­': 'e', 'Î¯': 'i', 'Ï': 'o',
        'Ï': 'y', 'Î®': 'h', 'Ï': 'w', 'Ï': 's', 'Ï': 'i', 'Î°': 'y', 'Ï': 'y',
        'Î': 'i', 'Î': 'A', 'Î': 'B', 'Î': 'G', 'Î': 'D', 'Î': 'E', 'Î': 'Z',
        'Î': 'H', 'Î': '8', 'Î': 'I', 'Î': 'K', 'Î': 'L', 'Î': 'M', 'Î': 'N',
        'Î': '3', 'Î': 'O', 'Î ': 'P', 'Î¡': 'R', 'Î£': 'S', 'Î¤': 'T', 'Î¥': 'Y',
        'Î¦': 'F', 'Î§': 'X', 'Î¨': 'PS', 'Î©': 'W', 'Î': 'A', 'Î': 'E', 'Î': 'I',
        'Î': 'O', 'Î': 'Y', 'Î': 'H', 'Î': 'W', 'Îª': 'I', 'Î«': 'Y'
    };
    const TURKISH_MAP = {
        'Å': 's', 'Å': 'S', 'Ä±': 'i', 'Ä°': 'I', 'Ã§': 'c', 'Ã': 'C', 'Ã¼': 'u',
        'Ã': 'U', 'Ã¶': 'o', 'Ã': 'O', 'Ä': 'g', 'Ä': 'G'
    };
    const ROMANIAN_MAP = {
        'Ä': 'a', 'Ã®': 'i', 'È': 's', 'È': 't', 'Ã¢': 'a',
        'Ä': 'A', 'Ã': 'I', 'È': 'S', 'È': 'T', 'Ã': 'A'
    };
    const RUSSIAN_MAP = {
        'Ð°': 'a', 'Ð±': 'b', 'Ð²': 'v', 'Ð³': 'g', 'Ð´': 'd', 'Ðµ': 'e', 'Ñ': 'yo',
        'Ð¶': 'zh', 'Ð·': 'z', 'Ð¸': 'i', 'Ð¹': 'j', 'Ðº': 'k', 'Ð»': 'l', 'Ð¼': 'm',
        'Ð½': 'n', 'Ð¾': 'o', 'Ð¿': 'p', 'Ñ': 'r', 'Ñ': 's', 'Ñ': 't', 'Ñ': 'u',
        'Ñ': 'f', 'Ñ': 'h', 'Ñ': 'c', 'Ñ': 'ch', 'Ñ': 'sh', 'Ñ': 'sh', 'Ñ': '',
        'Ñ': 'y', 'Ñ': '', 'Ñ': 'e', 'Ñ': 'yu', 'Ñ': 'ya',
        'Ð': 'A', 'Ð': 'B', 'Ð': 'V', 'Ð': 'G', 'Ð': 'D', 'Ð': 'E', 'Ð': 'Yo',
        'Ð': 'Zh', 'Ð': 'Z', 'Ð': 'I', 'Ð': 'J', 'Ð': 'K', 'Ð': 'L', 'Ð': 'M',
        'Ð': 'N', 'Ð': 'O', 'Ð': 'P', 'Ð ': 'R', 'Ð¡': 'S', 'Ð¢': 'T', 'Ð£': 'U',
        'Ð¤': 'F', 'Ð¥': 'H', 'Ð¦': 'C', 'Ð§': 'Ch', 'Ð¨': 'Sh', 'Ð©': 'Sh', 'Ðª': '',
        'Ð«': 'Y', 'Ð¬': '', 'Ð­': 'E', 'Ð®': 'Yu', 'Ð¯': 'Ya'
    };
    const UKRAINIAN_MAP = {
        'Ð': 'Ye', 'Ð': 'I', 'Ð': 'Yi', 'Ò': 'G', 'Ñ': 'ye', 'Ñ': 'i',
        'Ñ': 'yi', 'Ò': 'g'
    };
    const CZECH_MAP = {
        'Ä': 'c', 'Ä': 'd', 'Ä': 'e', 'Å': 'n', 'Å': 'r', 'Å¡': 's', 'Å¥': 't',
        'Å¯': 'u', 'Å¾': 'z', 'Ä': 'C', 'Ä': 'D', 'Ä': 'E', 'Å': 'N', 'Å': 'R',
        'Å ': 'S', 'Å¤': 'T', 'Å®': 'U', 'Å½': 'Z'
    };
    const SLOVAK_MAP = {
        'Ã¡': 'a', 'Ã¤': 'a', 'Ä': 'c', 'Ä': 'd', 'Ã©': 'e', 'Ã­': 'i', 'Ä¾': 'l',
        'Äº': 'l', 'Å': 'n', 'Ã³': 'o', 'Ã´': 'o', 'Å': 'r', 'Å¡': 's', 'Å¥': 't',
        'Ãº': 'u', 'Ã½': 'y', 'Å¾': 'z',
        'Ã': 'a', 'Ã': 'A', 'Ä': 'C', 'Ä': 'D', 'Ã': 'E', 'Ã': 'I', 'Ä½': 'L',
        'Ä¹': 'L', 'Å': 'N', 'Ã': 'O', 'Ã': 'O', 'Å': 'R', 'Å ': 'S', 'Å¤': 'T',
        'Ã': 'U', 'Ã': 'Y', 'Å½': 'Z'
    };
    const POLISH_MAP = {
        'Ä': 'a', 'Ä': 'c', 'Ä': 'e', 'Å': 'l', 'Å': 'n', 'Ã³': 'o', 'Å': 's',
        'Åº': 'z', 'Å¼': 'z',
        'Ä': 'A', 'Ä': 'C', 'Ä': 'E', 'Å': 'L', 'Å': 'N', 'Ã': 'O', 'Å': 'S',
        'Å¹': 'Z', 'Å»': 'Z'
    };
    const LATVIAN_MAP = {
        'Ä': 'a', 'Ä': 'c', 'Ä': 'e', 'Ä£': 'g', 'Ä«': 'i', 'Ä·': 'k', 'Ä¼': 'l',
        'Å': 'n', 'Å¡': 's', 'Å«': 'u', 'Å¾': 'z',
        'Ä': 'A', 'Ä': 'C', 'Ä': 'E', 'Ä¢': 'G', 'Äª': 'I', 'Ä¶': 'K', 'Ä»': 'L',
        'Å': 'N', 'Å ': 'S', 'Åª': 'U', 'Å½': 'Z'
    };
    const ARABIC_MAP = {
        'Ø£': 'a', 'Ø¨': 'b', 'Øª': 't', 'Ø«': 'th', 'Ø¬': 'g', 'Ø­': 'h', 'Ø®': 'kh', 'Ø¯': 'd',
        'Ø°': 'th', 'Ø±': 'r', 'Ø²': 'z', 'Ø³': 's', 'Ø´': 'sh', 'Øµ': 's', 'Ø¶': 'd', 'Ø·': 't',
        'Ø¸': 'th', 'Ø¹': 'aa', 'Øº': 'gh', 'Ù': 'f', 'Ù': 'k', 'Ù': 'k', 'Ù': 'l', 'Ù': 'm',
        'Ù': 'n', 'Ù': 'h', 'Ù': 'o', 'Ù': 'y'
    };
    const LITHUANIAN_MAP = {
        'Ä': 'a', 'Ä': 'c', 'Ä': 'e', 'Ä': 'e', 'Ä¯': 'i', 'Å¡': 's', 'Å³': 'u',
        'Å«': 'u', 'Å¾': 'z',
        'Ä': 'A', 'Ä': 'C', 'Ä': 'E', 'Ä': 'E', 'Ä®': 'I', 'Å ': 'S', 'Å²': 'U',
        'Åª': 'U', 'Å½': 'Z'
    };
    const SERBIAN_MAP = {
        'Ñ': 'dj', 'Ñ': 'j', 'Ñ': 'lj', 'Ñ': 'nj', 'Ñ': 'c', 'Ñ': 'dz',
        'Ä': 'dj', 'Ð': 'Dj', 'Ð': 'j', 'Ð': 'Lj', 'Ð': 'Nj', 'Ð': 'C',
        'Ð': 'Dz', 'Ä': 'Dj'
    };
    const AZERBAIJANI_MAP = {
        'Ã§': 'c', 'É': 'e', 'Ä': 'g', 'Ä±': 'i', 'Ã¶': 'o', 'Å': 's', 'Ã¼': 'u',
        'Ã': 'C', 'Æ': 'E', 'Ä': 'G', 'Ä°': 'I', 'Ã': 'O', 'Å': 'S', 'Ã': 'U'
    };
    const GEORGIAN_MAP = {
        'á': 'a', 'á': 'b', 'á': 'g', 'á': 'd', 'á': 'e', 'á': 'v', 'á': 'z',
        'á': 't', 'á': 'i', 'á': 'k', 'á': 'l', 'á': 'm', 'á': 'n', 'á': 'o',
        'á': 'p', 'á': 'j', 'á ': 'r', 'á¡': 's', 'á¢': 't', 'á£': 'u', 'á¤': 'f',
        'á¥': 'q', 'á¦': 'g', 'á§': 'y', 'á¨': 'sh', 'á©': 'ch', 'áª': 'c', 'á«': 'dz',
        'á¬': 'w', 'á­': 'ch', 'á®': 'x', 'á¯': 'j', 'á°': 'h'
    };

    const ALL_DOWNCODE_MAPS = [
        LATIN_MAP,
        LATIN_SYMBOLS_MAP,
        GREEK_MAP,
        TURKISH_MAP,
        ROMANIAN_MAP,
        RUSSIAN_MAP,
        UKRAINIAN_MAP,
        CZECH_MAP,
        SLOVAK_MAP,
        POLISH_MAP,
        LATVIAN_MAP,
        ARABIC_MAP,
        LITHUANIAN_MAP,
        SERBIAN_MAP,
        AZERBAIJANI_MAP,
        GEORGIAN_MAP
    ];

    const Downcoder = {
        'Initialize': function() {
            if (Downcoder.map) { // already made
                return;
            }
            Downcoder.map = {};
            for (const lookup of ALL_DOWNCODE_MAPS) {
                Object.assign(Downcoder.map, lookup);
            }
            Downcoder.regex = new RegExp(Object.keys(Downcoder.map).join('|'), 'g');
        }
    };

    function downcode(slug) {
        Downcoder.Initialize();
        return slug.replace(Downcoder.regex, function(m) {
            return Downcoder.map[m];
        });
    }


    function URLify(s, num_chars, allowUnicode) {
        // changes, e.g., "Petty theft" to "petty-theft"
        if (!allowUnicode) {
            s = downcode(s);
        }
        s = s.toLowerCase(); // convert to lowercase
        // if downcode doesn't hit, the char will be stripped here
        if (allowUnicode) {
            // Keep Unicode letters including both lowercase and uppercase
            // characters, whitespace, and dash; remove other characters.
            s = XRegExp.replace(s, XRegExp('[^-_\\p{L}\\p{N}\\s]', 'g'), '');
        } else {
            s = s.replace(/[^-\w\s]/g, ''); // remove unneeded chars
        }
        s = s.replace(/^\s+|\s+$/g, ''); // trim leading/trailing spaces
        s = s.replace(/[-\s]+/g, '-'); // convert spaces to hyphens
        s = s.substring(0, num_chars); // trim to first num_chars chars
        s = s.replace(/-+$/g, ''); // trim any trailing hyphens
        return s;
    }
    window.URLify = URLify;
}
