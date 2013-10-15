#!/bin/bash

BACKUP_DIR=/opt/Webwork_AdaptiveHints/db_backups

echo """ 
################################################################################
If you get a 'Can't create/write to file...' error with running backups, add:
  ${BACKUP_DIR} r,
  ${BACKUP_DIR}/* rw,

to 

/usr/sbin/mysqld {} in /etc/apparmor.d/usr.sbin.mysqld

then run

/etc/init.d/apparmor reload

See stack overflow response http://stackoverflow.com/a/2986764
################################################################################
"""

# Backup all webwork tables to $BACKUP_DIR
sudo mysqldump -u root -T $BACKUP_DIR -p webwork