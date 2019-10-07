from enum import Enum

__all__ = (
    'MasterServer',
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
