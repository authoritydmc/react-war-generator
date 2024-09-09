import os
import shutil
import zipfile
import argparse
import json
import versionGenerator

# Step 0: Define valid profiles
valid_profiles = ["dev", "test", "prod"]

# Default config
default_config = {
    "profile": "prod",
    "tomcatpath": "C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps",
    "deploy": False,
    "name": "myapp.war",
    "versiongen": True
}

# Step 1: Check if createWar.config.json exists, if not create it with default values
config_file = 'createWar.config.json'
if not os.path.exists(config_file):
    print(f"{config_file} not found, creating with default values.")
    with open(config_file, 'w') as file:
        json.dump(default_config, file, indent=4)
else:
    print(f"{config_file} found, loading configuration.")

# Step 2: Load configuration from createWar.config.json
with open(config_file, 'r') as file:
    config = json.load(file)

# Step 3: Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Create a WAR file for a specific profile.")
parser.add_argument(
    "--profile", "-p", choices=valid_profiles,
    help="Specify the profile (dev/test/prod). Default is 'prod'.")
parser.add_argument(
    "--tomcatpath", "-tp",
    help="Specify the path to the Tomcat webapps folder.")
parser.add_argument(
    "--deploy", "-d", action='store_true',
    help="Set True if you want to deploy, default is False.")
parser.add_argument(
    "--name", "-n",
    help="Specify the name of the WAR file.")
parser.add_argument(
    "--versiongen", "-vg", action='store_true',
    help="Set True to generate a version file, default is True.")
args = parser.parse_args()

# Step 4: Override config with command-line arguments (args take precedence)
profile = args.profile if args.profile else config.get("profile")
tomcat_path = args.tomcatpath if args.tomcatpath else config.get("tomcatpath")
should_deploy = args.deploy if args.deploy else config.get("deploy", False)
war_filename = args.name if args.name else config.get("name")
generate_version = args.versiongen if args.versiongen else config.get("versiongen", True)

current_directory = os.getcwd()

print(f"Building {profile} profile")
print("Current working directory:", current_directory)

# Step 5: Generate the version information if versiongen is True
if generate_version:
    print("Generating version file...")
    versionInfo = versionGenerator.generateVersionFile()
else:
    print("Skipping version file generation.")

# Step 6: Build the frontend assets with the specified profile
build_command = f"npm run build:{profile}"
os.system(build_command)

# Step 7: Create a temporary directory
temp_dir = "war_temp"
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
os.makedirs(temp_dir)

# Step 8: Copy frontend assets to the temporary directory
dist_dir = "dist"
for item in os.listdir(dist_dir):
    item_path = os.path.join(dist_dir, item)
    if os.path.isfile(item_path):
        shutil.copy2(item_path, temp_dir)
    else:
        shutil.copytree(item_path, os.path.join(temp_dir, item))

# Step 9: Create the WEB-INF directory
os.makedirs(os.path.join(temp_dir, "WEB-INF"))

# Step 10: Create the web.xml file (optional)
web_xml_content = '''<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
         http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">

  <error-page>
    <error-code>404</error-code>
    <location>/index.html</location>
  </error-page>
</web-app>
'''
with open(os.path.join(temp_dir, "WEB-INF", "web.xml"), "w") as f:
    f.write(web_xml_content)

# Step 11: Create the WAR file
if not war_filename:
    current_folder_name = os.path.basename(current_directory)
    war_filename = f"{current_folder_name}.war"

if not war_filename.endswith(".war"):
    war_filename += ".war"

with zipfile.ZipFile(war_filename, "w") as war_file:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = file_path.replace(temp_dir + os.sep, "")
            war_file.write(file_path, arcname)

print("WAR file generated:", war_filename)

# Step 12: Cleanup temporary directory
shutil.rmtree(temp_dir)

# Step 13: Copy the WAR file to the Tomcat webapps folder if deploy is True
if should_deploy:
    print("Deploying to Tomcat")
    try:
        if not tomcat_path:
            tomcat_path = r"C:\Program Files\Apache Software Foundation\Tomcat 10.1\webapps"
        shutil.copy2(war_filename, os.path.join(tomcat_path, war_filename))

        print(f"WAR file '{war_filename}' deployed to '{tomcat_path}'.")
    except Exception as e:
        print(f"Error occurred while copying to Tomcat: {str(e)}")
