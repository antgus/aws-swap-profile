#!/usr/bin/env python
# Assumes that credentials file is at ~/.aws/credentials

import argparse
import configparser
from configparser import ConfigParser
import os
from shutil import copyfile

config = ConfigParser()
config.read(os.path.expanduser('~/.aws/credentials'))

DEFAULT_PROFILE_BACKUP_NAME = 'old_default_backup'


def check_profile_exists(profile):
    sections = config.sections()
    if profile in sections:
        return profile
    else:
        all_profiles = "\n".join(sections)
        raise ValueError(
            "The profile '%s' is not in your credentials file. \n"
            "Profiles found:\n{\n%s\n}" % (profile, all_profiles)
        )


def create_backup_of_default_profile():
    """
    Moves the current profile in [default] to [DEFAULT_PROFILE_BACKUP_NAME]
    (for backup)
    """
    config.remove_section(DEFAULT_PROFILE_BACKUP_NAME)
    config.add_section(DEFAULT_PROFILE_BACKUP_NAME)
    for (k, v) in config.items('default'):
        config.set(DEFAULT_PROFILE_BACKUP_NAME, k, v)


def swap_profile(new_default_profile):
    create_backup_of_default_profile()

    config.remove_section('default')
    config.add_section('default')
    for (k, v) in config.items(new_default_profile):
        config.set('default', k, v)

    with open(os.path.expanduser('~/.aws/credentials'), 'w') as configfile:
        config.write(configfile)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", help="profile to set as default")
    args = parser.parse_args()
    profile = args.profile
    check_profile_exists(profile)
    swap_profile(profile)
    print('Swapped to profile: %s' % profile)

if __name__ == "__main__":
    main()
