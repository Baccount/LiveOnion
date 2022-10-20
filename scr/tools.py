import os


def clear_screen():
    print("\n" * 25)

# Append ControlPort 9051 to the torrc file /Users/brandon/Library/Application Support/TorBrowser-Data/Tor/torrc
def set_torrc():
    # get the path to the torrc file
    torrc_path = os.path.join(
        os.path.expanduser("~"),
        "Library/Application Support/TorBrowser-Data/Tor/torrc",
    )
    with open(torrc_path, "a") as torrc:
        torrc.write("ControlPort 9051")