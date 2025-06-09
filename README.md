
# radiantlogic-config-iac

Infrastructure-as-Code toolkit for managing and deploying Radiant Logic Virtual Directory Server (VDS) configurations.

## Features
- Deploy `.orx` view definitions
- Rollback and validate views
- Environment-based config support
- Docker and CI/CD compatible

## Usage

```bash
# Deploy a view
python main.py deploy views/dev/employee_view.orx env/dev.env

# Rollback a view
python main.py rollback employee_view views/dev/employee_view_backup.orx env/dev.env

# Validate a view
python main.py validate "ou=employees,dc=example,dc=com" env/dev.env
```
