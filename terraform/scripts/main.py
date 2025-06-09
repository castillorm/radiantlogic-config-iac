
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'radiant')))

from deploy_view import deploy_view
from rollback_view import rollback_view
from validate_view import validate_view

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "deploy":
        deploy_view(sys.argv[2], sys.argv[3])
    elif command == "rollback":
        rollback_view(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "validate":
        validate_view(sys.argv[2], sys.argv[3])
    else:
        print("Usage:")
        print("  python main.py deploy <.orx file> <env file>")
        print("  python main.py rollback <view_name> <backup.orx> <env file>")
        print("  python main.py validate <view_base_dn> <env file>")
