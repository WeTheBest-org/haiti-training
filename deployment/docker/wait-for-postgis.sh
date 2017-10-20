#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until psql -U "docker" -h "$host" gis -c '\l'; do
  >&2 echo "Postgis is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgis is up - executing command"
exec $cmd
