# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename

**What I did:**
Renamed the function `save_to_watchlist()` to `add_to_watchlist()` in `watchlist_service.py` and updated call sites in `watchlist.py` to reflect the name change.

**How I verified:**
`test_collection.py` was used to confirm that the renamed function still worked and that the rename did not negatively impact the code. 

## Comment 2 — Deduplication

**What I did:**
Modified `watchlist_service.py` to include deduplication logic, changes including additional docstring, exception class, and the check block added to `add_to_watchlist()`.

**How I verified:**
`test_watchlist.py` was used to confirm that the new deduplication logic did not negatively impact the code. 

## Comment 3 — Missing test

**What I did:**
Created `test_watchlist.py` to test the functions in `watchlist_service.py`. Added `test_add_to_watchlist_nonexistent_film_raises()` function to test code response for when a non-existent film is used in the function

**How I verified:**
`test_watchlist.py` was used to confirm that the new function returned an error when an invalid film ID was used and did not negatively impact the code.

## Comment 4 — Default visibility

**My position:**
Public visibility should remain `True`.

**Reasoning:**
Social apps, including CineLog, typically make their collection features, such as watchlists, visible on a user's profile by default as a common product pattern. Also, for users who prefer public watchlists, it streamlines the process and reduces friction between users and the app, and makes the app's features more useful out of the box.

**Tradeoff acknowledged:**
Some users prefer their watchlists to be private. They will have to take additional steps to set them to private access only, which will increase friction with the app and make its features less intuitive.

## Comment 5 — Sort order

**My position:**
Change `get_watchlist()`'s the sort order to `date added`.

**Reasoning:**
It is to provide consistency with the rest of the project code, as `get_collection()` in `collection_service.py` already sorts by "date added". It is also more practical. Recently added films are what users are most likely looking for, making them easier to find.

**Engagement with reviewer's point:**
An alphabetical sort is more convenient in specific use cases, such as when a user is scanning a list rather than reviewing. So, the best solution would be to provide options for users to sort by "data added" or "title".

## Comment 6 — 

**What conflicted:**
My local branch and the `origin/main` branch had their own `.gitignore`, which conflicted with each other.

**How I resolved it:**
I resolved the conflict by using my local branch's `.gitignore` config because it has a more thorough ignore list. 

**How I verified no conflict remains:**
I verified that there is no conflict by checking the git status and confirming the rebase has succeeded.  

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->