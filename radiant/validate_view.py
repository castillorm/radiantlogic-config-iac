
import subprocess
import os
import sys
from radiant.env_loader import load_env

def validate_view(base_dn, env_file):
    load_env(env_file)

    ldap_host = os.environ["VDS_HOST"]
    ldap_port = os.environ["LDAP_PORT"]
    ldap_user = os.environ["LDAP_BIND_DN"]
    ldap_pass = os.environ["LDAP_PASS"]

    print(f"🔍 Validating view at {base_dn}...")

    result = subprocess.run([
        "ldapsearch", "-x",
        "-H", f"ldap://{ldap_host}:{ldap_port}",
        "-D", ldap_user,
        "-w", ldap_pass,
        "-b", base_dn,
        "(objectClass=*)"
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ View is responsive")
    else:
        print("❌ Validation failed")
        print(result.stderr)
        sys.exit(1)
