activate_this = '/var/www/vhosts/random-oracles.org/lwc.random-oracles.org/venvVisuMark/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys  # noqa: E402

PROJECT_DIR = '/var/www/vhosts/random-oracles.org/lwc.random-oracles.org/httpdocs'
sys.path.append(PROJECT_DIR)

from webapp import create_app # noqa: E402

application = create_app()
