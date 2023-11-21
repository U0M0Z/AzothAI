from pathlib import Path
import os
#import frontend_azoth

# Project Directories
#PACKAGE_ROOT = Path(frontend_azoth.__file__).resolve().parent
PACKAGE_ROOT = Path(os.path.dirname(os.path.abspath(__file__)).split('/config')[0])
ROOT = PACKAGE_ROOT.parent
UTILS_DIR = PACKAGE_ROOT / "utils"
WEBPAGES_DIR = PACKAGE_ROOT / "webpages"
IMAGES_DIR = PACKAGE_ROOT / "images"
DATASETS_DIR = PACKAGE_ROOT / "datasets"