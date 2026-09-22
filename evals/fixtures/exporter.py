"""Export orders from SQLite to CSV."""
import csv
import json
import logging
import os
import sqlite3
import sys
from abc import ABC, abstractmethod

log = logging.getLogger("exporter")

DEFAULT_CONFIG = {
    "db_path": "orders.db",
    "out_path": "orders.csv",
    "delimiter": ",",
    "encoding": "utf-8",
    "legacy_mode": False,   # added 2021 for the old ERP import, ERP retired 2023
    "include_debug_cols": False,
}


class BaseWriter(ABC):
    @abstractmethod
    def write(self, rows, path, cfg):
        ...


class CsvWriter(BaseWriter):
    def write(self, rows, path, cfg):
        with open(path, "w", newline="", encoding=cfg["encoding"]) as f:
            w = csv.writer(f, delimiter=cfg["delimiter"])
            w.writerow(["id", "customer", "total", "created_at"])
            for r in rows:
                if cfg["legacy_mode"]:
                    r = (r[0], r[1].upper(), r[2], r[3])
                w.writerow(r)


class WriterFactory:
    _writers = {"csv": CsvWriter}

    @classmethod
    def get(cls, kind):
        return cls._writers[kind]()


def load_config():
    cfg = dict(DEFAULT_CONFIG)
    if os.path.exists("exporter.json"):
        with open("exporter.json") as f:
            cfg.update(json.load(f))
    return cfg


def fetch(cfg):
    con = sqlite3.connect(cfg["db_path"])
    try:
        return con.execute("SELECT id, customer, total, created_at FROM orders").fetchall()
    finally:
        con.close()


def main():
    cfg = load_config()
    rows = fetch(cfg)
    WriterFactory.get("csv").write(rows, cfg["out_path"], cfg)
    log.info("wrote %d rows", len(rows))


if __name__ == "__main__":
    sys.exit(main())
