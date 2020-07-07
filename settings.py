from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    # use_browser_bots=True,
    real_world_currency_per_point=(1/250),
    participation_fee=5.00,
    doc=""
)

SESSION_CONFIGS = [
    dict(
       name='brockEquality',
       display_name="Inequality and punishment (equality treatment)",
       num_demo_participants=4,
       app_sequence=[
           'part1',
           'part2intro',
           'part2game',
           'part3'
       ],
       treatment='equality'
    ),
    dict(
       name='brockSkill',
       display_name="Inequality and punishment (skill treatment)",
       num_demo_participants=4,
       app_sequence=[
           'part1',
           'part2intro',
           'part2game',
           'part3'
       ],
       treatment='skill'
    ),
    dict(
       name='brockLuck',
       display_name="Inequality and punishment (luck treatment)",
       num_demo_participants=4,
       app_sequence=[
           'part1',
           'part2intro',
           'part2game',
           'part3'
       ],
       treatment='luck'
    ),
    dict(
       name='brockUncertain',
       display_name="Inequality and punishment (uncertain treatment)",
       num_demo_participants=4,
       app_sequence=[
           'part1',
           'part2intro',
           'part2game',
           'part3'
       ],
       treatment='uncertain'
    ),
    dict(
       name='brockRandom',
       display_name="Inequality and punishment (randomly-allocated treatment)",
       num_demo_participants=4,
       app_sequence=[
           'part1',
           'part2intro',
           'part2game',
           'part3'
       ],
       treatment='random'
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'tokens'

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '70^a32-h0rg)o65uxe_f(%&eteheah8pkv#4+o&dcexk4lqjfi'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
