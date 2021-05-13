[![Doodba deployment](https://img.shields.io/badge/deployment-doodba-informational)](https://github.com/Tecnativa/doodba)
[![Last template update](https://img.shields.io/badge/last%20template%20update-v2.7.1-informational)](https://github.com/Tecnativa/doodba-copier-template/tree/v2.7.1)
[![Odoo](https://img.shields.io/badge/odoo-v13.0-a3478a)](https://github.com/odoo/odoo/tree/13.0)
[![BSL-1.0 license](https://img.shields.io/badge/license-BSL--1.0-success})](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

# esb - a Doodba deployment

**2021-13-05**

Change from normal project structure to doodby style. But still not use doodba docker image yet, still use the original docke container.

* Download this new esb, and change original odoo.conf addons path to ~/esb/odoo/auto/addons/odoo.conf

```
> sudo docker exec -it -u 0 odoo bash
> click-odoo-update -c /etc/odoo/odoo.conf -d <database_name> --ignore-core-addons --list-only --logfile /var/log/odoo-update.log
> tail /var/log/odoo-update.log
# Do the real update!
> click-odoo-update -c /etc/odoo/odoo.conf -d <database_name> --ignore-core-addons --logfile /var/log/odoo-update.log
```
