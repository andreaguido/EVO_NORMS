import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings
import datetime

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ['OTREE_PRODUCTION'] = "1"
os.environ['OTREE_AUTH_LEVEL'] = "STUDY"
os.environ['OTREE_ADMIN_PASSWORD'] = "0eqv6lrj"

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True


ADMIN_USERNAME = 'oxford'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
# Change this to something unique (e.g. mash your keyboard),
# and then delete this comment.
SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzz'

PAGE_FOOTER = ''

#DATABASES = {
#    'default': dj_database_url.config(
#        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
#    )
#}
SERVER_URL = 'http://ibsenb.lineex.es/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'oxford_otree',
        'USER': 'oxford',
        'PASSWORD': '0eqv6lrj',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '5432',
    }
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# ACCESS_CODE_FOR_DEFAULT_SESSION:
# If you have a "default session" set,
# then an access code will be appended to the URL for authentication.
# You can change this as frequently as you'd like,
# to prevent unauthorized server access.

ACCESS_CODE_FOR_DEFAULT_SESSION = 'my_access_code'

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR' ############################## MARIA EDIT
USE_POINTS = True
POINTS_DECIMAL_PLACES = 0  ############################## MARIA EDIT
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0 ############################## MARIA EDIT


# e.g. en-gb, de-de, it-it, fr-fr.
# see: https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'es-ES'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = []

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            Source code
        </a> for the below games.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Below are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish to create your own variations.
    Click one to learn more and play.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        qualification.LocaleRequirement("EqualTo", "US"),
        qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        #qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 2,
    'participation_fee': 5.00,
    'num_bots': 24,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
    'random_start_order': False,
    'USE_POINTS': True,
}

#ROOT_URLCONF = 'neighbor_choice.urls'

SESSION_CONFIGS = [
    {
        'name': 'lowhigh_norms',
        'display_name': "LowHigh",
        'num_demo_participants': 2,
        'app_sequence': ['big_five'],
        'use_browser_bots': False,
        'start_datetime': datetime.datetime(2020,6,8,8,0),
        'seconds_per_round': 86400,
        'inactive_threshold': 4,
        'roundstart_timeout': 3,
        #divides seconds_per_round to determine roundstart timeout. e.g. if seconds_per_round = 60 and roundstart_timeout = 3 then subjects have 20s on RoundStart.html
        'email': 'ibsen.gisc@gmail.com',
        'num_subjects_win': 1,
        'win_multiplier': 10,
        'real_world_currency_per_point': 0.0333333, # EXCHANGE RATE
        'participation_fee': 5,
    },
    dict(
        name='full_experiment_norms',
        display_name="Full Experiment Norms",
        num_demo_participants=6,
        app_sequence=['big_five', 'risk_lottery_eg', 'norm_compliance', 'questionnaire', 'svotree',
                      'non_linear_cpr_game', 'pun_prefs', 'payment'],
        use_browser_bots=False,
        start_datetime=datetime.datetime(2021, 4, 8, 23,0), # datetime.datetime.utcnow() # UCT time -2hr recall time diff
        seconds_per_round=86400,
        inactive_threshold=5,
        email='cnr.ibsen@gmail.com',
        num_subjects_win=2,
        win_multiplier=10,
        days=36,
        treatment="N",
        doc=""" <h1>Checklist</h1><ul> <li>Treatmet setup: N if baseline, A if authority message; </li> 
                       <li> seconds per round should be set to 86400 (1 day); </li>
                       <li> inactive threshold should be set to 5 </li>
                       <li> days should be set to 36 </li>
                       <li> number subjects win ?? </li>
                   </ul>"""
    )
]
    #    {
#        'name': 'highlow_norms',
#        'display_name': "HighLow",
#        'num_demo_participants': 2,
#        'app_sequence': ['big_five', 'risk_lottery_eg', 'autism_spectrum', 'questionnaire', 'svotree', 'climate_change_game', 'pun_prefs', 'payment'],
#        'use_browser_bots': False,
#        'start_datetime': datetime.datetime(2018,5,19,13,33),
#        'seconds_per_round': 100,
#        'inactive_threshold': 40,
#        'roundstart_timeout': 3,
        #divides seconds_per_round to determine roundstart timeout. e.g. if seconds_per_round = 60 and roundstart_timeout = 3 then subjects have 20s on RoundStart.html
#        'email': 'cnr.ibsen@gmail.com',
#        'num_subjects_win': 1,
#        'win_multiplier': 10,
#        'real_world_currency_per_point': 0.0333333, # EXCHANGE RATE
#        'participation_fee': 5,
#    },


"""
    {
        'name': 'trading_networks',
        'display_name': "Trading Networks Game",
        'num_demo_participants': 12,
        'real_world_currency_per_point': 2,
        'budget': 24000,
        'app_sequence': [
            'trading_networks','payment_info'
        ],
    },
    {
        'name': 'forecast',
        'display_name': "Forecast Game",
        'num_demo_participants': 24,
        'use_browser_bots':True,
        'real_world_currency_per_point': 0.000384615,
        'app_sequence': [
            'forecast'
        ],
    },
    {
        'name': 'trading_networks_with_treatments',
        'display_name': "Trading Networks (different treatments)",
        'num_demo_participants': 12,
        'real_world_currency_per_point': 2,
        #'use_browser_bots':True,
        'budget': 312,
        'treatment': 'random',
        'app_sequence': [
            'trading_networks_with_treatments'
        ],
        'doc': 
        Values for treatment: <br>
        'regular': participants play regular network <br>
        'sw': participants play small world network <br>
        'random': participants play a random network
    },
    {
        'name': 'public_goods',
        'display_name': "Public Goods",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods', 'payment_info'],
    },
    {
        'name': 'public_goods_simple',
        'display_name': "Public Goods (simple version from tutorial)",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_simple', 'survey', 'payment_info'],
    },
    {
        'name': 'trust',
        'display_name': "Trust Game",
        'num_demo_participants': 2,
        'app_sequence': ['trust', 'payment_info'],
    },
    {
        'name': 'trust_simple',
        'display_name': "Trust Game (simple version from tutorial)",
        'num_demo_participants': 2,
        'app_sequence': ['trust_simple'],
    },
    {
        'name': 'beauty',
        'display_name': "Beauty Contest",
        'num_demo_participants': 5,
        'num_bots': 5,
        'app_sequence': ['beauty', 'payment_info'],
    },
    {
        'name': 'survey',
        'display_name': "Survey",
        'num_demo_participants': 1,
        'app_sequence': ['survey', 'payment_info'],
    },
    {
        'name': 'quiz',
        'display_name': "Quiz",
        'num_demo_participants': 1,
        'app_sequence': ['quiz'],
    },
    {
        'name': 'prisoner',
        'display_name': "Prisoner's Dilemma",
        'num_demo_participants': 4,
        'app_sequence': ['prisoner', 'payment_info'],
    },
    {
        'name': 'ultimatum',
        'display_name': "Ultimatum (randomized: strategy vs. direct response)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
    },
    {
        'name': 'ultimatum_strategy',
        'display_name': "Ultimatum (strategy method treatment)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
        'treatment': 'strategy',
    },
    {
        'name': 'ultimatum_non_strategy',
        'display_name': "Ultimatum (direct response treatment)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
        'treatment': 'direct_response',
    },
    {
        'name': 'battle_of_the_sexes',
        'display_name': "Battle of the Sexes",
        'num_demo_participants': 2,
        'app_sequence': [
            'battle_of_the_sexes', 'payment_info'
        ],
    },
    {
        'name': 'vickrey_auction',
        'display_name': "Vickrey Auction",
        'num_demo_participants': 3,
        'app_sequence': ['vickrey_auction', 'payment_info'],
    },
    {
        'name': 'volunteer_dilemma',
        'display_name': "Volunteer's Dilemma",
        'num_demo_participants': 3,
        'app_sequence': ['volunteer_dilemma', 'payment_info'],
    },
    {
        'name': 'cournot_competition',
        'display_name': "Cournot Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'cournot_competition', 'payment_info'
        ],
    },
    {
        'name': 'principal_agent',
        'display_name': "Principal Agent",
        'num_demo_participants': 2,
        'app_sequence': ['principal_agent', 'payment_info'],
    },
    {
        'name': 'dictator',
        'display_name': "Dictator Game",
        'num_demo_participants': 2,
        'app_sequence': ['dictator', 'payment_info'],
    },
    {
        'name': 'matching_pennies',
        'display_name': "Matching Pennies",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies', 'payment_info'
        ],
    },
    {
        'name': 'matching_pennies_tutorial',
        'display_name': "Matching Pennies (tutorial version)",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies_tutorial',
        ],
    },
    {
        'name': 'traveler_dilemma',
        'display_name': "Traveler's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['traveler_dilemma', 'payment_info'],
    },
    {
        'name': 'bargaining',
        'display_name': "Bargaining Game",
        'num_demo_participants': 2,
        'app_sequence': ['bargaining', 'payment_info'],
    },
    {
        'name': 'stackelberg_competition',
        'display_name': "Stackelberg Competition",
        'real_world_currency_per_point': 0.01,
        'num_demo_participants': 2,
        'app_sequence': [
            'stackelberg_competition', 'payment_info'
        ],
    },
    {
        'name': 'bertrand_competition',
        'display_name': "Bertrand Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'bertrand_competition', 'payment_info'
        ],
    },
    {
        'name': 'stag_hunt',
        'display_name': "Stag Hunt",
        'num_demo_participants': 2,
        'app_sequence': ['stag_hunt', 'payment_info'],
    },
    {
        'name': 'real_effort',
        'display_name': "Real-effort transcription task",
        'num_demo_participants': 1,
        'app_sequence': [
            'real_effort',
        ],
    },
    {
        'name': 'lemon_market',
        'display_name': "Lemon Market Game",
        'num_demo_participants': 3,
        'app_sequence': [
            'lemon_market', 'payment_info'
        ],
    },
    {
        'name': 'asset_market',
        'display_name': "Asset Market Game",
        'num_demo_participants': 3,
        'app_sequence': [
            'asset_market', 'payment_info'
        ],
    },
    {
        'name': 'pgg',
        'display_name': "pgg UC3M",
        'num_demo_participants': 6,
        'app_sequence': ['pgg'],
    },

    {
        'name': 'apd',
        'display_name': "Asymetric Prisoner's Dilemma",
        'num_demo_participants': 6,
        'app_sequence': ['apd'],
    },

    {
        'name': 'pgg2',
        'display_name': "pgg2 UC3M",
        'num_demo_participants': 6,
        'app_sequence': ['pgg2'],
    },

    {
        'name': 'apd2',
        'display_name': "Asymetric Prisoner's Dilemma 2",
        'num_demo_participants': 6,
        'app_sequence': ['apd2'],
    },
    {
        'name': 'experiment',
        'display_name': "Experiment Both treatments UC3M",
        'num_demo_participants': 6,
        'app_sequence': ['experiment'],

    },
    {
        'name': 'Experiment',
        'display_name': "Experiment Both treatments UC3M",
        'num_demo_participants': 24,
        'repetitions':1,
        'app_sequence': ['experiment','pgg', 'apd'],

    },
    {
        'name': 'Experiment_Group',
        'display_name': "Experiment Group UC3M",
        'num_demo_participants': 6,
        'repetitions':1,
        'treatment':'group',
        'app_sequence': ['experiment','pgg', 'apd', 'my_payments'],
    },
    {
        'name': 'Experiment_Individual',
        'display_name': "Experiment Individual UC3M",
        'num_demo_participants': 6,
        'treatment':'individual',
        'repetitions':1,
        'app_sequence': ['experiment','pgg', 'apd', 'my_payments'],
    },
    {
        'name': 'Experiment_Group_2rep',
        'display_name': "Experiment Group UC3M 2",
        'num_demo_participants': 24,
        'treatment':'group',
        'repetitions':2,
        'app_sequence': ['experiment','pgg', 'apd', 'pgg2', 'apd2', 'my_payments'],
    },
    {
        'name': 'Experiment_Individual_2rep',
        'display_name': "Experiment Individual UC3M 2",
        'num_demo_participants': 24,
        'treatment':'individual',
        'repetitions':2,
        'app_sequence': ['experiment','pgg', 'apd','pgg2', 'apd2','my_payments'],
    },
    {
        'name': 'my_payments',
        'display_name': "Experiment UC3M payments",
        'num_demo_participants': 24,
        'app_sequence': ['my_payments'],
    },
"""

CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = '/home/oxford/static'
# SENTRY DSN settings
#SENTRY_DSN='http://22a6513c2beb44778cba4fa982cda172:87a64968d79a40a48c20019009677982@155.210.135.56:9000/4'
sentry_sdk.init(
    dsn="http://8fba51a7f0984566b110eac3672123c2@155.210.135.56:9000/7",
    integrations=[DjangoIntegration()]
)
# Redis settings
_PASSWORD = '0WfZXD1QfJ9Rnsancr0JrRHI8ov1JQ1YxAvy6g9bE8GMHS0bTmiBbs0G2LmurT9gkdSNu8ZmMikFi9TecGrE0OCgbzZQb0CrURsJWa6M8bnEEDeQywhItJrHJAW1T39Q'
REDIS_DATABASE = '12'
REDIS_URL = 'redis://:{0}@localhost:6379/{1}'.format(_PASSWORD,REDIS_DATABASE)
#_REDIS_URL = 'redis://localhost:6379/3'

os.environ['REDIS_URL'] = REDIS_URL
otree.settings.augment_settings(globals())




