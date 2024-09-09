# WAR File Generator

This utility automates the creation of WAR files for different environments (`dev`, `test`, `prod`), allowing for version file generation and optional deployment to a Tomcat server. It supports customization via a `createWar.config.json` configuration file, with command-line arguments taking precedence.

## Features

- **WAR File Creation**: Build WAR files for `dev`, `test`, or `prod` profiles.
- **Version File Generation**: Optionally generate a version file.
- **Tomcat Deployment**: Deploy the WAR file to a Tomcat server.
- **Configuration Flexibility**: Use command-line arguments or a JSON config file.
- **Automatic Config File Creation**: Generates a default `createWar.config.json` if not present.

---

## Usage Options

### 1. Using `createWar.exe`

Simplified execution is available via the `createWar.exe` file.

1. **Copy `createWar.exe`** to the root of your project (where `package.json` is located).
2. **Run**:
   - **Double-click** `createWar.exe` or
   - **Run via terminal** for argument passing:
     ```bash
     ./createWar.exe --profile dev --deploy True
     ```
3. The executable will:
   - Read `createWar.config.json` or create it with default settings.
   - Build and optionally deploy the WAR file.

#### Example:
```bash
./createWar.exe --profile prod --tomcatpath "/opt/tomcat/webapps" --deploy True
```

---

### 2. Running the Python Script

The Python version of the tool allows more flexibility with command-line arguments:

| Argument          | Description                                                    | Default      |
|-------------------|----------------------------------------------------------------|--------------|
| `--profile`       | Specify profile (`dev`, `test`, `prod`)                        | `prod`       |
| `--tomcatpath`    | Tomcat `webapps` folder path                                   | Config file  |
| `--deploy`        | Set to `True` to deploy the WAR file                           | `False`      |
| `--name`          | Name of the WAR file                                           | Project name |
| `--versiongen`    | Set `True` to generate version file                            | `True`       |

#### Examples:

- Generate WAR for `dev`:
  ```bash
  python create_war.py --profile dev
  ```

- Deploy WAR to Tomcat:
  ```bash
  python create_war.py --profile prod --deploy True
  ```

---

## Configuration File (`createWar.config.json`)

The configuration file is automatically created if missing. It provides default settings for WAR file generation and deployment.

#### Sample `createWar.config.json`:

```json
{
  "profile": "prod",
  "tomcatpath": "C:/Program Files/Apache Software Foundation/Tomcat 10.1/webapps",
  "deploy": false,
  "name": "myapp.war",
  "versiongen": true
}
```

| Key           | Description                                                   | Default      |
|---------------|---------------------------------------------------------------|--------------|
| `profile`     | Build profile (`dev`, `test`, `prod`)                         | `prod`       |
| `tomcatpath`  | Tomcat `webapps` deployment path                              | Configured path |
| `deploy`      | Deploy to Tomcat (`true` or `false`)                          | `false`      |
| `name`        | WAR file name                                                 | Project name |
| `versiongen`  | Generate version file (`true` or `false`)                     | `true`       |

---

## Workflow

1. **Build**: Runs `npm run build:<profile>` based on the profile.
2. **Version Generation**: Generates a version file if enabled.
3. **WAR Creation**: Packages files into a WAR with optional `web.xml` for custom error handling.
4. **Deployment**: Copies WAR to Tomcat `webapps` if enabled.
5. **Clean-up**: Temporary directories are removed post-WAR creation.

---

## Notes

- **Command-line overrides config**: Arguments passed via CLI take precedence over the JSON config file.
- **Error Handling**: Errors during deployment will display the message `Error occurred while copying to Tomcat: <error_message>`.
