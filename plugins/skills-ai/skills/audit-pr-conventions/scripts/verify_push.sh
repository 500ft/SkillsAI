#!/usr/bin/env bash
# Confirm a push landed by comparing SHAs, not by trusting exit codes through a pipe.
# usage: verify_push.sh <remote-url-with-token> <branch>
set -u
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
url="$1"; branch="$2"
local_sha=$(git rev-parse HEAD)
git fetch -q "$url" "$branch" 2>/dev/null || { echo "fetch failed"; exit 2; }
remote_sha=$(git rev-parse FETCH_HEAD)
echo "local  $local_sha"
echo "remote $remote_sha"
if [ "$local_sha" = "$remote_sha" ]; then echo "IN SYNC"; exit 0; fi
echo "NOT IN SYNC"; exit 1
