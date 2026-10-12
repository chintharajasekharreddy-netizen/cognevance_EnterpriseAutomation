-- Enterprise Automation & Data Processing System - SQLite schema

CREATE TABLE IF NOT EXISTS processed_files (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    filename       TEXT NOT NULL,
    total_rows     INTEGER DEFAULT 0,
    valid_rows     INTEGER DEFAULT 0,
    invalid_rows   INTEGER DEFAULT 0,
    duplicate_rows INTEGER DEFAULT 0,
    status         TEXT NOT NULL,              -- success | failed
    error          TEXT,
    duration_sec   REAL,
    processed_at   TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS api_records (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    source      TEXT NOT NULL,
    external_id INTEGER NOT NULL,
    title       TEXT,
    body        TEXT,
    fetched_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (source, external_id)
);

CREATE TABLE IF NOT EXISTS job_runs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name     TEXT NOT NULL,
    status       TEXT NOT NULL,                -- success | failed
    message      TEXT,
    duration_sec REAL,
    started_at   TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS notifications (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    channel    TEXT NOT NULL,                  -- email | log
    subject    TEXT NOT NULL,
    message    TEXT,
    status     TEXT NOT NULL,                  -- sent | logged | failed
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
