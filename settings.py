from os import environ

import datetime

SESSION_CONFIGS = [
    dict(
        name = 'full_experiment_norms',
        display_name = "Full Experiment Norms",
        num_demo_participants = 6,
        app_sequence= ['big_five', 'risk_lottery_eg', 'norm_compliance', 'questionnaire', 'svotree', 'non_linear_cpr_game', 'pun_prefs', 'payment'],
        use_browser_bots = False,
        start_datetime = datetime.datetime.utcnow(),#datetime.datetime(2021, 3, 23, 15, 44),
        seconds_per_round = 86400,
        inactive_threshold = 10,
        email = 'cnr.ibsen@gmail.com',
        num_subjects_win = 2,
        win_multiplier = 10,
        days = 36
    ),
    dict(
        name='CPR',
        display_name="CPR",
        num_demo_participants=6,
        app_sequence=['non_linear_cpr_game'],
        use_browser_bots=False,
        start_datetime=datetime.datetime(2021, 9, 14, 22, 31),
        seconds_per_round=60,
        inactive_threshold=10,
        email='cnr.ibsen@gmail.com',
        num_subjects_win=1,
        win_multiplier=10,
    )

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '&rj0$*gv-#56#r02dxt#-m!kkc8_0i8c_u=@8ev8ot=_2zhw_&'

INSTALLED_APPS = ['otree']
