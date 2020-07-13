import functools
import os

from ansible import constants as C
from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import merge_hash


DOCUMENTATION = """
vars: project_vars
short_description: Load global variables from files
options:
  path:
    type: str
    ini:
      - key: path
        section: project_vars
    env:
      - name: ANSIBLE_PROJECT_VARS_PATH
"""

CONFIG_SECTION = "project_vars"
CONFIG_DEFAULTS = {
    "path": "vars"
}


def get_plugin_option(key):
    # This function is a hack against Ansible 2.9. Use VarsModule.get_option()
    # on Ansible 2.10 and above.

    env_key = "ANSIBLE_" + CONFIG_SECTION.upper() + "_" + key.upper()
    env_value = os.getenv(env_key)
    if env_value:
        return env_value

    section = CONFIG_SECTION
    for p in C.config._parsers.values():
        if p.has_option(CONFIG_SECTION, key):
            return p.get(CONFIG_SECTION, key)

    return CONFIG_DEFAULTS[key]


@functools.lru_cache(maxsize=16)
def find_vars_files(loader, basedir, path):
    return loader.find_vars_files(basedir, path)


class VarsModule(BaseVarsPlugin):
    def get_vars(self, loader, path, entities):
        super().get_vars(loader, path, entities)

        path = get_plugin_option("path")
        vars_files = find_vars_files(loader, self._basedir, path)

        merged_vars = {}
        for file_path in sorted(vars_files):
            loaded_vars = loader.load_from_file(file_path)
            merged_vars = merge_hash(merged_vars, loaded_vars)

        return merged_vars
