import subprocess
import re
import datetime


def get_build_information():
    try:
        # Execute the git describe command and capture the output
        version_info = subprocess.check_output(
            ['git', 'describe', '--tags', '--long']
        ).decode().strip()
        current_branch = subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
        ).decode().strip()
        print(version_info)
        # Parse the output to extract versionCode and versionName
        vname, commit_count, git_hash = version_info.split('-')

        # Remove any characters except dots and digits from vname
        vname = re.sub(r'[^0-9.]', '', vname)

        # Parse the versionName into major, minor, and patch versions
        major_version, minor_version, patch_version = map(
            int, vname.split('.')
        )

        version_code = (
            major_version * 1000000 +
            minor_version * 100000 +
            patch_version * 10000 +
            int(commit_count)
        )

        version_name = vname
        current_time = datetime.datetime.now()

        updation_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        full_version_name = f"{version_info}@{current_branch}"

        return {
            "versionCode": version_code,
            "versionName": version_name,
            "fullVersionName": full_version_name,
            "updated": updation_time
        }

    except subprocess.CalledProcessError as e:
        print(f"Error running Git command: {e}")
        return None


def write_to_typescript(version_info):
    try:
        with open('src/version.tsx', 'w') as file:
            file.write('export const versionInfo = ')
            file.write(str(version_info))
            file.write(';\n')
            print("Generated VersionInfo file as src/version.tsx")
    except IOError as e:
        print(f"Error writing to TypeScript file: {e}")


def generateVersionFile():
    version_info = get_build_information()
    if version_info:
        write_to_typescript(version_info)


if __name__ == "__main__":
    version_info = get_build_information()
    if version_info:
        write_to_typescript(version_info)
        print("Generated versionCode:", version_info["versionCode"])
        print("Generated versionName:", version_info["versionName"])
        print("Generated Full version:", version_info["fullVersionName"])
