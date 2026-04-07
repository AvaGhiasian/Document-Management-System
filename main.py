from data_access.directories import Directories
from logic.management import Management
from presentation.interface import Interface

if __name__ == "__main__":
    directories = Directories()
    manage = Management(directories)
    interface = Interface(manage)

    interface.run()
