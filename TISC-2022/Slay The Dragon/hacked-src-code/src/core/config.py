from os import path

######################
#     GAME CONFIG    #
######################

# Player
BASE_ATTACK = 99999999

# Item
SWORD_PRICE = 5
SWORD_ATTACK_BONUS = 2
POTION_PRICE = 1
POTION_POTENCY = 10

# Work
WORK_SALARY = 5

# Boss
BOSS_DATA_FILE = path.join(path.dirname(__file__), "boss.json")

######################
#   NETWORK CONFIG   #
######################

# Protocol
EOF_MARKER = "#"
