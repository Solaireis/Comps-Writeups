from enum import Enum


class Result(Enum):
    PLAYER_WIN_BATTLE = "PLAYER_WIN_BATTLE"
    BOSS_WIN_BATTLE = "BOSS_WIN_BATTLE"
    VALIDATED_OK = "VALIDATED_OK"
    CANNOT_AFFORD = "CANNOT_AFFORD"
    PURCHASE_OK = "PURCHASE_OK"
    OBTAINED_FLAG = "OBTAINED_FLAG"
    WORK_OK = "WORK_OK"