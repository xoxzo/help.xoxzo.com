import os

from pelican import signals


def write_redirects_file(sender):
    if not "NETLIFY_REDIRECTS" in sender.settings:
        raise ValueError("NETLIFY_REDIRECTS setting not found in Pelican settings")

    rows = []
    for from_path, to_path, *options in sender.settings["NETLIFY_REDIRECTS"]:
        rows.append(" ".join(map(str, [from_path, to_path] + options)))

    with open(os.path.join(sender.output_path, "_redirects"), "w") as f:
        f.write("\n".join(rows))


def register():
    signals.finalized.connect(write_redirects_file)
