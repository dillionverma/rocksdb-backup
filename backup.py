#!/usr/bin/env python3

"""
This script is used to backup and restore RocksDB database instances

Example:
    $ python3 backup.py backup ./my_live_db ./backup/
    $ python3 backup.py restore ./backup ./my_live_db

"""

__author__ = "Dillion Verma"

import os
import argparse
from pathlib import Path
import rocksdb
import sys


# https://pyrocksdb.readthedocs.io/en/v0.4/tutorial/index.html#backup-and-restore


def backup(from_path: str, to_path: str) -> None:
    from_path = os.path.abspath(os.path.expanduser(from_path))
    to_path = os.path.abspath(os.path.expanduser(to_path))

    # Get db instance
    db = rocksdb.DB(from_path, rocksdb.Options(create_if_missing=True))

    # Create backup dir if doesn't exist
    Path(to_path).mkdir(parents=True, exist_ok=True)

    # Backup db
    backup = rocksdb.BackupEngine(to_path)
    backup.create_backup(db, flush_before_backup=True)

    print("Backup complete: ", os.path.basename(from_path))


def restore(from_path: str, to_path: str) -> None:
    from_path = os.path.abspath(os.path.expanduser(from_path))
    to_path = os.path.abspath(os.path.expanduser(to_path))

    # restore db
    backup = rocksdb.BackupEngine(from_path)
    backup.restore_latest_backup(to_path, to_path)

    print("Restore complete: ",  os.path.basename(to_path))


def main(args=None):
    if args.command == "backup":
        backup(args.from_path, args.to_path)
    elif args.command == "restore":
        restore(args.from_path, args.to_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('command', help='operation',
                        choices=['backup', 'restore'])
    parser.add_argument('from_path', help='path to perform operation from')
    parser.add_argument('to_path', help='path to perform operation to')

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    args = parser.parse_args()

    main(args)
