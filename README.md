# WAR File Generator

This Python script automates the creation of a WAR file based on a specified profile (dev, test, prod) for a react app. It also offers the option to generate a version file and deploy the WAR file to a Tomcat server. The script allows for customization via command-line arguments or a createWar.config.json configuration file. Command-line arguments take precedence over the configuration file values if both are provided.
## Features

  Create WAR files based on different profiles (dev, test, prod). (Includes one **sample_package.json** to help you understand how to build different profile)
     
  Generate a version file based on the versiongen setting.
  
  Deploy the WAR file to a specified Tomcat server automatically.
  
  Customize settings using command-line arguments or a configuration file (createWar.config.json).
  
  Automatically create the createWar.config.json file with default values if it doesn't exist.
  
  Clean-up temporary files after creating the WAR file.
  
