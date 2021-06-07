# Rocksdb-backup

A simple script to backup and restore rocksDB instances.

## Installation

1. Copy the script somewhere
2. Install dependencies

```
 pip3 install -r requirements.txt
```

## Usage

```
$ python3 backup.py backup ./my_rocks_db ./backup/my_rocks_db
$ python3 backup.py restore ./backup/my_rocks_db ./my_rocks_db
```
