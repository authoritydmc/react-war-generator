# WAR File Generator

This Python script automates the creation of a WAR file based on a specified profile (`dev`, `test`, `prod`). It also offers the option to generate a version file and deploy the WAR file to a Tomcat server. The script allows for customization via command-line arguments or a `createWar.config.json` configuration file. Command-line arguments take precedence over the configuration file values if both are provided.

## Features

- **Create WAR files** based on different profiles (`dev`, `test`, `prod`). [ for info on what is profile check `sample_package.json` file.]
- **Generate a version file** based on the `versiongen` setting.
- **Deploy the WAR file** to a specified Tomcat server automatically.
- **Customize settings** using command-line arguments or a configuration file (`createWar.config.json`).
- **Automatically create** the `createWar.config.json` file with default values if it doesn't exist.
- **Clean-up temporary files** after creating the WAR file.

## How to Use

### 1. Using `createWar.exe`

To make the process even simpler, the entire Python script has been converted into an executable file (`createWar.exe`). This allows you to use the tool without needing to have Python or the dependencies installed on your system. Simply follow the steps below to generate a WAR file for your project with minimal effort.

### How to Use the `createWar.exe` File

1. **Download or Copy the `createWar.exe` file** into the root folder of your project, where the `package.json` file is located. This is essential as the script looks for `npm` commands to build the project.

2. **Run the `createWar.exe`**:
   - **Double-click the `createWar.exe`** file to run it.
   - Alternatively, you can **invoke it via the command line** (especially useful for passing arguments):
     ```bash
     ./createWar.exe
     ```

3. Once executed, the tool will:
   - **Read the configuration file** (`createWar.config.json`) or create one if it doesn't exist.
   - **Build the project** using the profile specified in the configuration file or command-line arguments.
   - **Create the WAR file** and, if enabled, **deploy it** to the Tomcat server.

### Command-line Arguments (Optional)

If you want to pass command-line arguments while running the executable (instead of using the default values from the configuration file), you can invoke the `.exe` file from the terminal or command prompt with the necessary options:

#### Example Usage:

```bash
./createWar.exe --profile dev --tomcatpath "/opt/tomcat/webapps" --deploy True --versiongen False
```

This will:
- Use the `dev` profile to build the project.
- Deploy the WAR file to `/opt/tomcat/webapps`.
- Skip the version file generation (`--versiongen False`).

### Benefits of Using `createWar.exe`

- **No Python required**: You don't need Python or additional libraries installed to use the script.
- **Simplified Process**: Just place the executable in the project root, double-click, and let it do the work for you.
- **Configuration Flexibility**: Either edit the `createWar.config.json` file or pass arguments when invoking the `.exe` file via the command line.
- **Fast and Easy Deployment**: If the `deploy` option is enabled, the WAR file is automatically deployed to Tomcat.

---

### 2. Command-line Arguments

The script can be executed with command-line arguments for flexibility. Here are the available arguments:

| Argument          | Short Flag | Description                                                                                     | Default    |
|-------------------|------------|-------------------------------------------------------------------------------------------------|------------|
| `--profile`       | `-p`       | Specify the profile to use (`dev`, `test`, `prod`).                                              | `prod`     |
| `--tomcatpath`    | `-tp`      | Specify the path to the Tomcat `webapps` folder.                                                 | Configured path in JSON file |
| `--deploy`        | `-d`       | Deploy the WAR file to the Tomcat server (`True` for deployment).                                | `False`    |
| `--name`          | `-n`       | Specify the name of the WAR file to generate.                                                    | Folder name of the project |
| `--versiongen`    | `-vg`      | Set `True` to generate a version file. Use `False` to skip version generation.                   | `True`     |

#### Example Usage

1. **Generate a WAR file with the `dev` profile:**

   ```bash
   python create_war.py --profile dev
   ```

2. **Generate and deploy a WAR file to a custom Tomcat path:**

   ```bash
   python create_war.py --profile prod --tomcatpath "/opt/tomcat/webapps" --deploy
   ```

3. **Skip version file generation:**

   ```bash
   python create_war.py --versiongen False
   ```

### 2. Configuration File (`createWar.config.json`)

The script uses a `createWar.config.json` file to store configuration values. If the file doesn't exist, the script will create one with default values. You can edit this file to customize the behavior of the script.

#### Example `createWar.config.json`:

```json
{
  "profile": "prod",
  "tomcatpath": "C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps",
  "deploy": false,
  "name": "myapp.war",
  "versiongen": true
}
```

#### Configuration Options

| Key           | Description                                                                                       | Default                                      |
|---------------|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| `profile`     | The build profile to use (`dev`, `test`, or `prod`).                                               | `prod`                                       |
| `tomcatpath`  | The path to the Tomcat `webapps` folder where the WAR file will be deployed (if `deploy` is `True`).| `C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps` |
| `deploy`      | Set to `true` if you want to automatically deploy the generated WAR file to Tomcat.                | `false`                                      |
| `name`        | The name of the WAR file to be generated.                                                          | `"myapp.war"`                                |
| `versiongen`  | Set to `true` if you want to generate a version file. Set to `false` to skip version generation.    | `true`                                       |

#### Example Usage with Configuration File

If you run the script without any command-line arguments, it will use the values from the `createWar.config.json` file:

```bash
python create_war.py
```

In this case, the script will:
- Use the `prod` profile.
- Create a WAR file named `myapp.war`.
- Deploy the WAR file to `C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps` if `deploy` is set to `true`.
- Generate a version file if `versiongen` is `true`.

### 3. Command-line Arguments Take Precedence

When both command-line arguments and configuration file values are available, the command-line arguments take precedence.

For example, if `createWar.config.json` sets the profile to `prod` but you run the script with the `--profile dev` flag, the `dev` profile will be used:

```bash
python create_war.py --profile dev
```

### 4. Script Workflow

1. **Profile Selection**:
   - The script uses the `profile` (either from the config file or command-line) to run the build command: `npm run build:<profile>`.

2. **Version File Generation**:
   - If `versiongen` is `True`, the script generates a version file using the function `versionGenerator.generateVersionFile()`.
   - If `versiongen` is `False`, version generation is skipped.

3. **WAR File Creation**:
   - The script copies frontend assets from the build directory into a temporary directory (`war_temp`).
   - A `WEB-INF/web.xml` file is added, which includes a 404 error page redirect.
   - All files in the temporary directory are zipped into a WAR file with the specified name.

4. **Deployment (Optional)**:
   - If `deploy` is set to `True`, the WAR file is copied to the Tomcat `webapps` folder.

5. **Clean-up**:
   - The script deletes the temporary directory (`war_temp`) after creating the WAR file.

### 5. Error Handling

If an error occurs during the deployment process, the script will output an error message.

```bash
Error occurred while copying to Tomcat: <error_message>
```
