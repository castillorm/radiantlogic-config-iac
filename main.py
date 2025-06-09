
import sys
from radiant.deploy_view import deploy_view
from radiant.rollback_view import rollback_view
from radiant.validate_view import validate_view

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
