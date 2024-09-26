#!/bin/bash

# Use entr to monitor changes in ids.py and rebuild on change
while true; do
    echo "Monitoring changes in ids.py..."
    echo ids.py | entr -r ./run_ids.sh
done
