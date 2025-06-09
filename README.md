# radiantlogic-config-iac

🚀 Infrastructure-as-Code toolkit for managing and deploying Radiant Logic Virtual Directory Server (VDS) configurations — including `.orx` view definitions, HDAP stores, and related metadata — across environments using Python, Docker, and optionally Terraform.

---

## 📦 Features

- Deploy `.orx` view definitions programmatically
- Rollback view deployments using backups
- Validate deployed views via LDAP queries
- Environment-specific configuration via `.env` files
- Dockerized CLI for consistent runtime
- Terraform-compatible for declarative view deployment

---

## 🧱 Folder Structure

```plaintext
radiantlogic-config-iac/
├── radiant/            # Python deployment logic
├── views/              # Environment-specific .orx files
├── env/                # Environment config (.env) files
├── terraform/          # Terraform module for deployment
├── scripts/            # CLI entry points and Docker wrapper
├── main.py             # Main Python runner
├── Dockerfile          # Dockerized deployment runtime
└── README.md
