from enum import Enum, unique, IntEnum

__all__ = (
    'MasterServer',
    'RegionCode',
)


class MasterServer(Enum):
    """
    An enumeration of current :valve-wiki:`master query server <Master_Server_Query_Protocol#Master_servers>` hosts.
    """

    GOLDSRC = ('hl1master.steampowered.com', 27013)
    """
    A host pointing to the outdated IPs for querying :valve-wiki:`Half-Life 1 <Half-Life_1>` master servers.
    
    .. note::
        The port numbers used by ``hl1master.steampowered.com`` can be anything between 27010 and 27013.
    """
    GOLDSOURCE = GOLDSRC
    """An alias for :attr:`GOLDSRC`"""
    HALF_LIFE_1 = GOLDSRC
    """An alias for :attr:`GOLDSRC`"""
    SOURCE = ('hl2master.steampowered.com', 27011)
    """
    This domain name points to 3 A records (IPs), one of them using a different port (27015) according to the
    |MasterServer2.vdf|_.
    """
    HALF_LIFE_2 = SOURCE
    """An alias for :attr:`SOURCE`"""
    RED_ORCHESTRA = SOURCE
    # TODO: verify if this is true
    """Master query server for :steam-app:`Red Orchestra <1200>` (same as :attr:`SOURCE`)"""
    RAG_DOLL_KUNG_FU = ('68.142.72.250', 27012)
    """Master query server for :steam-app:`Rag Doll Kung Fu <1002>`"""
    SIN_1_MULTIPLAYER = ('69.28.151.162', 27010)
    # TODO: verify if this is true
    """Master query server for :steam-app:`SiN 1 Multiplayer <1300>`"""


@unique
class RegionCode(IntEnum):
    """Enumeration of different regions of the world that you wish to find servers in."""

    US_EAST_COAST = 0x00
    """:wikipedia:`US East coast <East_Coast_of_the_United_States>`"""
    US_WEST_COAST = 0x01
    """:wikipedia:`US West coast <West_Coast_of_the_United_States>`"""
    SOUTH_AMERICA = 0x02
    """:wikipedia:`South America <South_America>`"""
    EUROPE = 0x03
    """:wikipedia:`Europe <Europe>`"""
    ASIA = 0x04
    """:wikipedia:`Asia <Asia>`"""
    AUSTRALIA = 0x05
    """:wikipedia:`Australia <Australia>`"""
    MIDDLE_EAST = 0x06
    """:wikipedia:`Middle East <Middle_East>`"""
    AFRICA = 0x07
    """:wikipedia:`Africa <Africa>`"""
    REST_OF_THE_WORLD = 0xFF
    """Rest of the world"""
