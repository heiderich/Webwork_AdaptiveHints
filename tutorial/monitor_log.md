## Monitor Live Log Info ##
###log in to server###
```
ssh [username]@webwork.cse.ucsd.edu
```
###monitor log from all log files###
```
sudo multitail --mergeall /var/log/hint/rest-*.log
```
### type b for going up in multitail ###
### type h for help in multitail ###