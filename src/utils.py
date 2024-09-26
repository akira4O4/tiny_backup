import os
import yaml
import shutil


def load_yaml(path: str):
    with open(path, encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def check_dir(path: str, clean: bool = False) -> None:
    if os.path.exists(path):
        if clean:
            shutil.rmtree(path)
            os.makedirs(path)
    else:
        os.makedirs(path)


def read_version(path: str):
    with open(path, 'r') as txt:
        return txt.readline()
