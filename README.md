# esb

## Git-Aggregator & Click-Odoo-Contrib

```

1. Prepare file
- custom-addons
| - <custom_module>
- repository
| - repos.yaml
- .gitignore
- addons-link.py
- addons.yaml
- README.md

2. Install and run git-aggregator
# sudo pip install git-aggregator
# gitaggregate -c repos.yaml

3. Run addons-link.py
# python3 addons-link.py

4. Edit addons-path in config file

5. Entry container odoo
# sudo docker exec -it -u 0 odoo bash

6. Install click-odoo-contrib
# pip3 install click-odoo-contrib

7. Test run click-odoo-contrib
# click-odoo-update -c /etc/odoo/odoo.conf -d <database_name> --ignore-core-addons --list-only --logfile /var/log/odoo-update.log

8. Check log
# tail /var/log/odoo-update.log

9. If all log not error or warning, run click-odoo-contrib
# click-odoo-update -c /etc/odoo/ -d <database_name> --ignore-core-addons --logfile /var/log/odoo-update.log

```
