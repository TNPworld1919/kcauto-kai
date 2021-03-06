class Globals(object):
    # for the sikuli scan and observe rates (times per second)
    SIKULI_SCANRATE = 20
    # time to wait before executing another kcauto-kai loop
    LOOP_SLEEP_LENGTH = 15
    # how often to check the quests outside of other checkpoints
    QUEST_LOOP_CHECK_RATE = 5
    # the number of seconds to add to all waits
    SLEEP_MODIFIER = 0

    # similarity thresholds for various asset types
    DEFAULT_SIMILARITY = 0.8
    DAMAGE_SIMILARITY = 0.85
    FATIGUE_SIMILARITY = 0.85
    SHIP_LIST_SIMILARITY = 0.96
    FLEET_ICON_SIMILARITY = 0.8
    SHIP_LIST_FLEET_ICON_SIMILARITY = 0.75

    # how many minutes to wait between sorties to allow for natural fatigue
    # recovery
    COMBAT_BUFFER_MINUTES = 0
    # how many combat sorties to conduct when sparkling
    SPARKLING_RUN_COUNT = 3

    # area expansion presets; format is in [left, right, up, down] relative to
    # the center of the match
    EXPAND = {
        'repair_list': [-325, 35, -10, 6],
        'arrow_navigation': [-10, 10, -5, 5],
        'shiplist_sort': [-4, 36, -10, 10]
    }
