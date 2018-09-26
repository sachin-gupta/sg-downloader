#!/bin/bash

# Try to delete tag, Continue on error
echo git tag -d \"$(git log --format=%h -1)\"
set +ev
git tag -d "$(git log --format=%h -1)"
# Commenting as this may cause unexpected TravisCI behavious
#set -ev
