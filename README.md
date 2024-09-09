# WAR File Generator

This tool automates the creation of a WAR file for Java web applications, using a specified profile (`dev`, `test`, `prod`, `default`). It supports generating a version file and deploying the WAR file to a Tomcat server. The configuration can be customized using either command-line arguments or a `createWar.config.json` configuration file. Command-line arguments take precedence over configuration file values if both are provided.

## Features

- **Create WAR files** based on different profiles (`dev`, `test`, `prod`, `default`).
- **Generate a version file** based on the `versiongen` setting.
- **Deploy the WAR file** to a specified Tomcat server.
- **Automatic Configuration**: The `createWar.config.json` file is automatically created with default values if it doesn’t exist.
- **Clean-Up**: Temporary files are automatically cleaned up after the WAR file is created.

## How to Use

### 1. Using `createWar.exe`

To simplify the process, the Python script has been converted into an executable file (`createWar.exe`). This allows you to use the tool without needing Python or its dependencies.

#### Steps:

1. **Download or Copy the `createWar.exe` file** into the root folder of your project, where `package.json` is located.

2. **Run the `createWar.exe`**:
   - **Double-click the `createWar.exe` file** to run it.
   - **Alternatively, invoke it via the command line** (useful for passing arguments):
     ```bash
     ./createWar.exe
     ```

3. The executable will:
   - **Read the `createWar.config.json` file** or create it with default values if it doesn’t exist.
   - **Build the project** using the specified profile or default profile.
   - **Create the WAR file** and optionally **deploy it** to Tomcat.

### Command-line Arguments (Optional)

You can pass command-line arguments to override default settings. Here’s how to use them:

#### Example Usage:

```bash
./createWar.exe --profile dev --tomcatpath "/opt/tomcat/webapps" --deploy --versiongen False --name "customapp.war"
```

#### Arguments:

| Argument        | Short Flag | Description                                                                              | Default                      |
|-----------------|------------|------------------------------------------------------------------------------------------|------------------------------|
| `--profile`     | `-p`       | Specify the profile to use (`dev`, `test`, `prod`, `default`).                           | `default`                     |
| `--tomcatpath`  | `-tp`      | Specify the path to the Tomcat `webapps` folder.                                          | Configured path in JSON file |
| `--deploy`      | `-d`       | Deploy the WAR file to Tomcat.                                                            | `False`                      |
| `--name`        | `-n`       | Specify the name of the WAR file.                                                         | `"myapp.war"`                |
| `--versiongen`  | `-vg`      | Set to `True` to generate a version file. Set to `False` to skip version generation.      | `True`                       |

#### Examples:

1. **Generate a WAR file with the `dev` profile:**

   ```bash
   ./createWar.exe --profile dev
   ```

2. **Generate and deploy a WAR file to a custom Tomcat path:**

   ```bash
   ./createWar.exe --profile prod --tomcatpath "/opt/tomcat/webapps" --deploy
   ```

3. **Skip version file generation:**

   ```bash
   ./createWar.exe --versiongen False
   ```

### 2. Configuration File (`createWar.config.json`)

The script uses a configuration file (`createWar.config.json`) to store default values. If the file doesn’t exist, it will be created with default values.

#### Example `createWar.config.json`:

```json
{
  "profile": "default",
  "tomcatpath": "C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps",
  "deploy": false,
  "name": "myapp.war",
  "versiongen": true
}
```

#### Configuration Options:

| Key           | Description                                                                                       | Default                                      |
|---------------|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| `profile`     | The build profile to use (`dev`, `test`, `prod`, `default`).                                      | `default`                                    |
| `tomcatpath`  | The path to the Tomcat `webapps` folder for deployment (if `deploy` is `True`).                     | `C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps` |
| `deploy`      | Set to `true` to automatically deploy the generated WAR file to Tomcat.                            | `false`                                      |
| `name`        | The name of the WAR file to be generated.                                                          | `"myapp.war"`                                |
| `versiongen`  | Set to `true` to generate a version file. Set to `false` to skip version generation.                | `true`                                       |

### 3. Default Profile

If the `profile` is set to `"default"`, the script runs the build command without specifying a profile:

```bash
npm run build
```

### 4. Command-line Arguments Take Precedence

Command-line arguments override the values in the configuration file. For example, running:

```bash
./createWar.exe --profile dev
```

will use the `dev` profile, even if the configuration file specifies a different profile.

### 5. Script Workflow

1. **Profile Selection**:
   - The script builds the project using the specified or default profile.

2. **Version File Generation**:
   - Generates a version file if `versiongen` is `True`.
   - Skips version generation if `versiongen` is `False`.

3. **WAR File Creation**:
   - Copies frontend assets from the `dist` directory into a temporary directory.
   - Creates a `WEB-INF/web.xml` file.
   - Zips all files into a WAR file.

4. **Deployment (Optional)**:
   - Copies the WAR file to the Tomcat `webapps` folder if `deploy` is `True`.

5. **Clean-Up**:
   - Deletes the temporary directory after creating the WAR file.

### 6. Error Handling

If an error occurs during deployment, an error message is displayed.

```bash
Error occurred while copying to Tomcat: <error_message>
```

---
