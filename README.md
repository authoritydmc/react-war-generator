WAR File Generator
This Python script creates a WAR file based on a specified profile (dev, test, prod), with options for version file generation and deployment to a Tomcat server. The script can be customized via command-line arguments or a configuration file (createWar.config.json). Command-line arguments take precedence over the configuration file if both are provided.

Features
Generate WAR files from frontend assets (e.g., a built project).
Specify different profiles (dev, test, prod) for different environments.
Optionally generate a version file.
Optionally deploy the WAR file to a specified Tomcat server.
Customize settings via the createWar.config.json configuration file or command-line arguments.
Automatically creates a createWar.config.json file with default values if it doesn’t exist.
How to Use
1. Command-line Arguments
You can run the script by providing command-line arguments. Below is a list of the available arguments:

Argument	Short Flag	Description	Default
--profile	-p	Specify the profile to use (dev, test, prod).	prod
--tomcatpath	-tp	Specify the path to the Tomcat webapps folder.	Configured path in JSON file
--deploy	-d	Deploy the WAR file to the Tomcat server (True for deployment).	False
--name	-n	Specify the name of the WAR file to generate.	Folder name of the project
--versiongen	-vg	Set True to generate a version file. Use False to skip version generation.	True
Example Usage
Generate a WAR file with the dev profile:

bash
Copy code
python create_war.py --profile dev
Generate and deploy a WAR file to a custom Tomcat path:

bash
Copy code
python create_war.py --profile prod --tomcatpath "/opt/tomcat/webapps" --deploy
Skip version file generation:

bash
Copy code
python create_war.py --versiongen False
2. Configuration File (createWar.config.json)
If the configuration file does not exist, the script will automatically create it with default values. You can manually edit this file to configure the script’s behavior.

Example createWar.config.json:
json
Copy code
{
  "profile": "prod",
  "tomcatpath": "C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps",
  "deploy": false,
  "name": "myapp.war",
  "versiongen": true
}
Configuration Options
Key	Description	Default
profile	The build profile to use (dev, test, or prod).	prod
tomcatpath	The path to the Tomcat webapps folder where the WAR file will be deployed (if deploy is True).	C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps
deploy	Set to true if you want to automatically deploy the generated WAR file to Tomcat.	false
name	The name of the WAR file to be generated.	"myapp.war"
versiongen	Set to true if you want to generate a version file. Set to false to skip version generation.	true
Example Usage with Configuration File
If you run the script without any command-line arguments, the script will use the values specified in the createWar.config.json file.

bash
Copy code
python create_war.py
In this case, the script will:

Use the prod profile.
Create a WAR file named myapp.war.
Deploy it to the C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps directory.
Generate a version file.
3. Precedence of Command-line Arguments Over Config File
If command-line arguments are provided, they take precedence over the values in createWar.config.json.

For example, if createWar.config.json has the profile set to prod, but you run the script with --profile dev, the dev profile will be used instead of the prod profile.

bash
Copy code
python create_war.py --profile dev
4. How the Script Works
Profile Selection:

You can specify the profile (dev, test, or prod) using --profile. This profile is used in the build process.
Version File Generation:

If versiongen is True, the script will generate a version file by calling versionGenerator.generateVersionFile().
If versiongen is False, version generation is skipped.
Building the WAR File:

The script will run the frontend build command npm run build:<profile> based on the selected profile.
The built assets are then copied to a temporary directory (war_temp).
WAR File Creation:

The script will package the assets and a web.xml file into a WAR file. If no name is provided, the folder name of the project is used as the default WAR file name.
Deployment (Optional):

If deploy is set to True, the WAR file is automatically copied to the Tomcat webapps folder specified by tomcatpath.
Clean-up:

After generating the WAR file, the temporary files are cleaned up by deleting the war_temp directory.
5. Error Handling
If an error occurs during the deployment process, the script will print an error message.

bash
Copy code
Error occurred while copying to Tomcat: <error_message>