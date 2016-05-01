#!/bin/sh

python setup.py sdist
curl -F package=@dist/`ls dist` https://$GEMFURY_KEY@push.fury.io/silver-saas/
