import sys
import os

sys.path.append(os.getcwd())

import app.controller.server as server


if __name__ == '__main__':
     server.start_server()

