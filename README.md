# WAR File Generator

This tool automates the creation of a WAR file for Java web applications. It supports multiple profiles (`dev`, `test`, `prod`, `default`), optional version file generation, and deployment to a Tomcat server. The tool can handle different frontend build directories such as React’s `dist` or Next.js’s `out`.

## Features

- **Profile-Based Builds**: Create WAR files based on specified profiles (`dev`, `test`, `prod`, `default`).
- **Version File Generation**: Optionally generate a version file.
- **Deployment**: Optionally deploy the WAR file to a Tomcat server.
- **Configurable Frontend Directory**: Specify the directory for frontend build assets.
- **Automatic Configuration**: `createWar.config.json` is created with default values if not present.
- **Clean-Up**: Automatically cleans up temporary files after creating the WAR file.

## Prerequisites

- Ensure you have Node.js installed for building frontend assets.
- Have Python installed if using the script directly.

## How to Use

### Using `createWar.exe`

For convenience, the Python script is packaged into an executable (`createWar.exe`) for easy use without needing Python or its dependencies.

#### Steps:

1. **Download or copy** the `createWar.exe` file into the root folder of your project, where `package.json` is located.

2. **Run the `createWar.exe`**:
   - **Double-click the `createWar.exe` file** to run it.
   - **Or, use the command line** (useful for passing arguments):
     ```bash
     ./createWar.exe
     ```

3. The executable will:
   - **Read or create** the `createWar.config.json` file with default values if it does not exist.
   - **Build the project** using the specified profile or the default profile.
   - **Create the WAR file** and optionally **deploy it** to Tomcat.

### Command-Line Arguments

You can pass command-line arguments to customize the behavior. Here’s how to use them:

#### Example Usage:

```bash
./createWar.exe --profile dev --tomcatpath "/opt/tomcat/webapps" --deploy --versiongen False --name "customapp.war" --distdir "build"
```

#### Arguments:

| Argument        | Short Flag | Description                                                                              | Default                      |
|-----------------|------------|------------------------------------------------------------------------------------------|------------------------------|
| `--profile`     | `-p`       | Specify the profile to use (`dev`, `test`, `prod`, `default`).                           | `default`                     |
| `--tomcatpath`  | `-tp`      | Specify the path to the Tomcat `webapps` folder.                                          | Configured path in JSON file |
| `--deploy`      | `-d`       | Deploy the WAR file to Tomcat.                                                            | `False`                      |
| `--name`        | `-n`       | Specify the name of the WAR file.                                                         | `"myapp.war"`                |
| `--versiongen`  | `-vg`      | Set to `True` to generate a version file. Set to `False` to skip version generation.      | `True`                       |
| `--distdir`     | `-dd`      | Specify the directory for frontend build assets (e.g., `dist` for React, `out` for Next.js). | `"dist"`                     |

#### Examples:

1. **Generate a WAR file with the `dev` profile:**

   ```bash
   ./createWar.exe --profile dev
   ```

2. **Generate and deploy a WAR file to a custom Tomcat path:**

   ```bash
   ./createWar.exe --profile prod --tomcatpath "/opt/tomcat/webapps" --deploy
   ```

3. **Skip version file generation and use a custom assets directory:**

   ```bash
   ./createWar.exe --versiongen False --distdir "build"
   ```

### Configuration File (`createWar.config.json`)

The script uses a configuration file (`createWar.config.json`) to store default values. If the file does not exist, it will be created with default values.

#### Example `createWar.config.json`:

```json
{
  "profile": "default",
  "tomcatpath": "C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps", # Set your TOMCAT webapps folder location 
  "deploy": false,
  "name": "myapp.war", # this must match the uri path of your app . i.e check baseName in your package.json
  "versiongen": true,
  "distdir": "dist"  # Configurable directory for frontend build assets
}
```

#### Configuration Options:

| Key           | Description                                                                                       | Default                                      |
|---------------|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| `profile`     | The build profile to use (`dev`, `test`, `prod`, `default`).                                      | `default`                                    |
| `tomcatpath`  | The path to the Tomcat `webapps` folder for deployment (if `deploy` is `True`).                     | `C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps` |
| `deploy`      | Whether to deploy the WAR file to Tomcat.                                                          | `False`                                     |
| `name`        | The name of the WAR file.                                                                         | `"myapp.war"`                               |
| `versiongen`  | Whether to generate a version file.                                                               | `True`                                      |
| `distdir`     | The directory for frontend build assets (e.g., `dist` for React or `out` for Next.js).              | `"dist"`                                    |

## Frontend Build Directories

The `distdir` configuration allows you to specify the directory where your frontend build assets are located:

- **React**: Typically `dist` (default), but can be configured.
- **Next.js**: Typically `out` for static exports.

Ensure that the `distdir` matches the directory used by your frontend framework to store build outputs.

---
