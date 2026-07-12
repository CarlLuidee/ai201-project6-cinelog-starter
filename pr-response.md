# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename

**What I did:**
Renamed the function `save_to_watchlist()` to `add_to_watchlist()` in `watchlist_service.py` and updated call sites in `watchlist.py` to reflect the name change.

**How I verified:**
The full test suite was used to confirm that the function rename did not negativeley impact the code. 

## Comment 2 — Deduplication

**What I did:**
Modified `watchlist_service.py` to include deduplication logic, changes including additional docstring, exception class, and the check block added to `add_to_watchlist()`.

**How I verified:**
The full test suite was used to confirm that the new deduplication logic did not negativeley impact the code. 

## Comment 3 — Missing test

**What I did:**


**How I verified:**


## Comment 4 — Default visibility
**My position:**
**Reasoning:**
**Tradeoff acknowledged:**

## Comment 5 — Sort order
**My position:**
**Reasoning:**
**Engagement with reviewer's point:**

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->