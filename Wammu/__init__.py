"""Wammu modules
"""

import sys
import gettext
__version__ = '0.4'

gettext.install('wammu')

# FIXME: these definitions probably should be part of gammu module and not this...
# First is used as default
Models = ['at', 'alcatel', 'nauto', 'obex', 'seobex']
Connections = ['at19200', 'at115200', 'fbus', 'fbusirda', 'fbusdlr3', 'fbusdku5', 'fbusblue', 'phonetblue', 'mrouterblue', 'mbus', 'irdaphonet', 'irdaat', 'irdaobex', 'bluephonet', 'bluefbus', 'blueat', 'blueobex']
if sys.platform == 'win32':
    Devices = ['com1:', 'com2:']
# FIXME: support more platforms?
else:
    Devices = ['/dev/ttyS0', '/dev/ttyS1', '/dev/ttyUSB0', '/dev/ircomm0']

ContactMemoryTypes = ['ME', 'SM']

SMSIDs = {
    'Text':                 ['Text', 'ConcatenatedTextLong', 'ConcatenatedAutoTextLong', 'ConcatenatedTextLong16bit', 'ConcatenatedAutoTextLong16bit'],
    'Sound':                [
        'NokiaProfileLong',
        'EMSSound10',
        'EMSSound12',
        'EMSSonyEricssonSound',
        'EMSSound10Long',
        'EMSSound12Long',
        'EMSSonyEricssonSoundLong',
        ],
    'Animation':            [
        'NokiaProfileLong',
        'EMSAnimation',
        'AlcatelMonoAnimationLong',
        'NokiaScreenSaverLong',
        ],
    'Bitmap':               [
        'NokiaProfileLong',
        'NokiaPictureImageLong',
        'NokiaRingtone',
        'NokiaRingtoneLong',
        'NokiaOperatorLogo',
        'NokiaOperatorLogoLong',
        'NokiaCallerLogo',
        'EMSFixedBitmap',
        'EMSVariableBitmap',
        'EMSVariableBitmapLong',
        'AlcatelMonoBitmapLong',
        'AlcatelSMSTemplateName',
        ],
    'PredefinedAnimation':  ['EMSPredefinedAnimation'],
    'PredefinedSound':      ['EMSPredefinedSound'],
    }



MemoryValueTypes = [
    'Number_General',
    'Number_Mobile',
    'Number_Work',
    'Number_Fax',
    'Number_Home',
    'Number_Pager',
    'Number_Other',
    'Text_Note',
    'Text_Postal',
    'Text_Email',
    'Text_Email2',
    'Text_URL',
    'Date',
    'Caller_Group',
    'Text_Name',
    'Text_LastName',
    'Text_FirstName',
    'Text_Company',
    'Text_JobTitle',
    'Category',
    'Private',
    'Text_StreetAddress',
    'Text_City',
    'Text_State',
    'Text_Zip',
    'Text_Country',
    'Text_Custom1',
    'Text_Custom2',
    'Text_Custom3',
    'Text_Custom4',
    'RingtoneID',
    'PictureID',
    ]

CalendarTypes = [
    'REMINDER',
    'CALL',
    'MEETING',
    'BIRTHDAY',
    'MEMO',
    'TRAVEL',
    'VACATION',
    'T_ATHL',
    'T_BALL',
    'T_CYCL',
    'T_BUDO',
    'T_DANC',
    'T_EXTR',
    'T_FOOT',
    'T_GOLF',
    'T_GYM',
    'T_HORS',
    'T_HOCK',
    'T_RACE',
    'T_RUGB',
    'T_SAIL',
    'T_STRE',
    'T_SWIM',
    'T_TENN',
    'T_TRAV',
    'T_WINT',
    'ALARM',
    'DAILY_ALARM',
    ]

CalendarValueTypes = [
    'START_DATETIME',
    'END_DATETIME',
    'ALARM_DATETIME',
    'SILENT_ALARM_DATETIME',
    'RECURRANCE',
    'TEXT',
    'LOCATION',
    'PHONE',
    'PRIVATE',
    'CONTACTID',
    'REPEAT_DAYOFWEEK',
    'REPEAT_DAY',
    'REPEAT_WEEKOFMONTH',
    'REPEAT_MONTH',
    'REPEAT_FREQUENCY',
    'REPEAT_STARTDATE',
    'REPEAT_STOPDATE',
    ]

TodoPriorities = ['High', 'Medium', 'Low']

TodoValueTypes = [
    'END_DATETIME',
    'COMPLETED',
    'ALARM_DATETIME',
    'SILENT_ALARM_DATETIME',
    'TEXT',
    'PRIVATE',
    'CATEGORY',
    'CONTACTID',
    'PHONE',
    ]

TextFormats = [
    [(_('Alignment'), _('None')), ('Left', _('Left'), '<div align="left">%s</div>'), ('Right', _('Right'), '<div align="right">%s</div>'), ('Center', _('Center'), '<div align="center">%s</div>')],
    
    [(_('Text Size'), _('Normal')), ('Large', _('Large'), '<font size="+2">%s</font>'), ('Small', _('Small'), '<font size="-2">%s</font>')],

    ['', ('Bold', _('Bold'), '<b>%s</b>')],
    ['', ('Italic', _('Italic'), '<i>%s</i>')],
    ['', ('Underlined', _('Underlined'), '<u>%s</u>')],
    ['', ('Strikethrough', _('Strikethrough'), '<strike>%s</strike>')],
]


