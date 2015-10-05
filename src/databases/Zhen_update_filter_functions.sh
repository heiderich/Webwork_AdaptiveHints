#!/bin/bash
echo "Adding assigned(hint sent or not) to hint tables for $1"
./render_hint_tables.py add_assigned_hint_table.sql $1 | mysql webwork -u webworkWrite -p
echo "Adding filter type to filter functions"
./render_hint_tables.py add_type_to_filter_functions.sql $1 | mysql webwork -u webworkWrite -p
echo "Dropping hint id from filter functions"
./render_hint_tables.py drop_hint_id_from_filter_functions.sql $1 | mysql webwork -u webworkWrite -p