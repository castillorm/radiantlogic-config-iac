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
- Scalable structure for managing Radiant Logic as code

---

## 🔧 Supported Radiant Logic Components for IaC

| Component                        | Managed via Config Files           |
|----------------------------------|------------------------------------|
| **Views (Join, Proxy, GIB)**     | `.orx`                             |
| **Data Sources**                 | `.json` or `.properties`           |
| **HDAP Stores**                  | `.json`                            |
| **Persistent Cache Settings**    | `.json`, `.xml`                    |
| **Global ID Rules**              | `.xml`, `.json`                    |
| **Namespace Tree Mapping**       | `.json`, `.ldif`                   |
| **Access Control (ACI)**         | `.aci`, `.json`                    |
| **Interception Scripts**         | `.js`, `.groovy`                   |

---

## 🗂 Recommended Project Structure

```plaintext
radiantlogic-config-iac/
├── views/                 # .orx view definitions
├── data-sources/          # JSON source configs (AD, DB)
├── hdap/                  # HDAP store setup
├── cache/                 # View caching rules
├── global-id/             # GIB correlation & match rules
├── aci/                   # Access control policies
├── env/                   # Environment variables
├── scripts/               # Python CLI automation
├── terraform/             # Terraform IaC wrapper
├── Dockerfile             # Runtime container
└── README.md
