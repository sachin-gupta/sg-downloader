#!/bin/bash

# Try to delete tag, Continue on error
echo git tag -d \"$(git log --format=%h -1)\"
set +ev
git tag -d "$(git log --format=%h -1)"
set -e

# Try to create tag locally with commit id
#git tag "$(date +'%Y%m%d%H%M%S')-$(git log --format=%h -1)"
echo git tag \"$(git log --format=%h -1)\"
git tag "$(git log --format=%h -1)"
