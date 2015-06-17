import tgl
from telex import plugin
import xkcd


class XKCDPlugin(plugin.TelexPlugin):
    """
    Get xkcd's from xkcd.com
    """

    patterns = {
        "^!xkcd$": "xkcd_random",
        "^!xkcd (latest|newest|new)$": "xkcd_latest",
        "^!xkcd (\d+)$": "xkcd_by_number"
    }

    usage = [
        "!xkcd"
    ]

    def __init__(self):
        super().__init__()

    def xkcd_random(self, msg, matches):
        comic = xkcd.getRandomComic()
        return self.return_comic(msg, comic)

    def xkcd_latest(self, msg, matches):
        comic = xkcd.getLatestComic()
        return self.return_comic(msg, comic)

    def xkcd_by_number(self, msg, matches):
        comic = xkcd.getComic(int(matches.group(1)))
        return self.return_comic(msg, comic)

    def return_comic(self, msg, comic):
        filename = self.bot.download_to_file(comic.getImageLink(), "png")
        peer = self.bot.get_peer_to_send(msg)
        tgl.send_photo(peer, filename)
        return comic.getTitle() + ". " + comic.getExplanation()
