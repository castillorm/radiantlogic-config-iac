
import subprocess
import sys
import os
from radiant.env_loader import load_env

def deploy_view(orx_file, env_file):
    load_env(env_file)

    vds_host = os.environ["VDS_HOST"]
    vds_port = os.environ["VDS_PORT"]
    vds_user = os.environ["VDS_USER"]
    vds_pass = os.environ["VDS_PASS"]

    print(f"📦 Deploying view: {orx_file} to {vds_host}")
    result = subprocess.run([
        "vdsctl", "import", "view",
        "--file", orx_file,
        "--host", vds_host,
        "--port", vds_port,
        "--user", vds_user,
        "--password", vds_pass
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ View deployed successfully")
    else:
        print("❌ Deployment failed")
        print(result.stderr)
        sys.exit(1)
