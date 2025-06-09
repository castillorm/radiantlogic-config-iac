
import subprocess
import sys
import os
from radiant.env_loader import load_env

def rollback_view(view_name, backup_file, env_file):
    load_env(env_file)

    vds_host = os.environ["VDS_HOST"]
    vds_port = os.environ["VDS_PORT"]
    vds_user = os.environ["VDS_USER"]
    vds_pass = os.environ["VDS_PASS"]

    print(f"🔁 Rolling back view: {view_name}")

    subprocess.run([
        "vdsctl", "delete", "view",
        "--name", view_name,
        "--host", vds_host,
        "--port", vds_port,
        "--user", vds_user,
        "--password", vds_pass
    ])

    subprocess.run([
        "vdsctl", "import", "view",
        "--file", backup_file,
        "--host", vds_host,
        "--port", vds_port,
        "--user", vds_user,
        "--password", vds_pass
    ])

    print("✅ Rollback completed")
