# site Tawala project

## Quick Start

- Install dependencies (e.g. `uv sync`).
- Run the development server (`uv run tawala runserver`).
- To configure the project, see the configuration section below.

## Configuration

Settings can be provided via three mechanisms, in order of precedence:

1. **Environment variable** — set in your `.env` file (e.g. `MY_VAR=value`)
2. **`pyproject.toml`** — set as a key under the `[tool.tawala]` (e.g. `my_var = "value"`)
3. **Default** — the built-in fallback value used when nothing else is provided

### 01. Security and Deployment Configuration

| Environment Variable    | TOML Key                | Accepted Values        | Default                                                    |
| ----------------------- | ----------------------- | ---------------------- | ---------------------------------------------------------- |
| `SECRET_KEY`            | `secret-key`            | string                 | `django-insecure-change-me-in-production-via-env-variable` |
| `DEBUG`                 | `debug`                 | `true` \| `false`      | `true`                                                     |
| `ALLOWED_HOSTS`         | `allowed-hosts`         | comma-separated values | `localhost,127.0.0.1`                                      |
| `SECURE_SSL_REDIRECT`   | `secure-ssl-redirect`   | `true` \| `false`      | `false`                                                    |
| `SESSION_COOKIE_SECURE` | `session-cookie-secure` | `true` \| `false`      | `false`                                                    |
| `CSRF_COOKIE_SECURE`    | `csrf-cookie-secure`    | `true` \| `false`      | `false`                                                    |
| `SECURE_HSTS_SECONDS`   | `secure-hsts-seconds`   | integer                | `0`                                                        |
| `WORK_IN_PROGRESS`      | `work-in-progress`      | `true` \| `false`      | `false`                                                    |

### 02. Server (ASGI/WSGI) Configuration

| Environment Variable | TOML Key          | Accepted Values   | Default |
| -------------------- | ----------------- | ----------------- | ------- |
| `SERVER_USE_ASGI`    | `server.use-asgi` | `true` \| `false` | `false` |

### 03. Database Configuration

| Environment Variable | TOML Key      | Accepted Values                                                               | Default     |
| -------------------- | ------------- | ----------------------------------------------------------------------------- | ----------- |
| `DB_BACKEND`         | `db.backend`  | `sqlite` \| `postgresql`                                                      | `sqlite`    |
| `DB_USE_VARS`        | `db.use-vars` | `true` \| `false`                                                             | `false`     |
| `DB_SERVICE`         | `db.service`  | string                                                                        | ``          |
| `DB_USER`            | `db.user`     | string                                                                        | ``          |
| `DB_PASSWORD`        | `db.password` | string                                                                        | ``          |
| `DB_NAME`            | `db.name`     | string                                                                        | ``          |
| `DB_HOST`            | `db.host`     | string                                                                        | `localhost` |
| `DB_PORT`            | `db.port`     | integer                                                                       | `5432`      |
| `DB_POOL`            | `db.pool`     | `true` \| `false`                                                             | `false`     |
| `DB_SSLMODE`         | `db.sslmode`  | `prefer` \| `require` \| `disable` \| `allow` \| `verify-ca` \| `verify-full` | `prefer`    |

### 04. Files and Storage Configuration

| Environment Variable    | TOML Key             | Accepted Values              | Default      |
| ----------------------- | -------------------- | ---------------------------- | ------------ |
| `STORAGE_BACKEND`       | `storage.backend`    | `filesystem` \| `vercelblob` | `filesystem` |
| `BLOB_READ_WRITE_TOKEN` | `storage.blob-token` | string                       | ``           |

### 05. Internationalization Configuration

| Environment Variable | TOML Key                             | Accepted Values   | Default |
| -------------------- | ------------------------------------ | ----------------- | ------- |
| `LANGUAGE_CODE`      | `internationalization.language-code` | string            | `en-us` |
| `TIME_ZONE`          | `internationalization.time-zone`     | string            | `UTC`   |
| `USE_I18N`           | `internationalization.use-i18n`      | `true` \| `false` | `true`  |
| `USE_TZ`             | `internationalization.use-tz`        | `true` \| `false` | `true`  |

### 06. Runcommands Configuration

| Environment Variable  | TOML Key              | Accepted Values        | Default                                                                      |
| --------------------- | --------------------- | ---------------------- | ---------------------------------------------------------------------------- |
| `RUNCOMMANDS_INSTALL` | `runcommands.install` | comma-separated values | _(empty)_                                                                    |
| `RUNCOMMANDS_BUILD`   | `runcommands.build`   | comma-separated values | `makemigrations,migrate,compilescss,collectstatic --noinput --ignore=*.scss` |

### 07. Installed Apps Configuration

| Environment Variable | TOML Key      | Accepted Values        | Default   |
| -------------------- | ------------- | ---------------------- | --------- |
| `APPS_EXTEND`        | `apps.extend` | comma-separated values | _(empty)_ |
| `APPS_REMOVE`        | `apps.remove` | comma-separated values | _(empty)_ |

### 08. Middleware Configuration

| Environment Variable | TOML Key            | Accepted Values        | Default   |
| -------------------- | ------------------- | ---------------------- | --------- |
| `MIDDLEWARE_EXTEND`  | `middleware.extend` | comma-separated values | _(empty)_ |
| `MIDDLEWARE_REMOVE`  | `middleware.remove` | comma-separated values | _(empty)_ |

### 09. Context Processors Configuration

| Environment Variable        | TOML Key                    | Accepted Values        | Default   |
| --------------------------- | --------------------------- | ---------------------- | --------- |
| `CONTEXT_PROCESSORS_EXTEND` | `context-processors.extend` | comma-separated values | _(empty)_ |
| `CONTEXT_PROCESSORS_REMOVE` | `context-processors.remove` | comma-separated values | _(empty)_ |

### 10. Staticfile Finders Configuration

| Environment Variable        | TOML Key                    | Accepted Values        | Default   |
| --------------------------- | --------------------------- | ---------------------- | --------- |
| `STATICFILE_FINDERS_EXTEND` | `staticfile_finders.extend` | comma-separated values | _(empty)_ |
| `STATICFILE_FINDERS_REMOVE` | `staticfile_finders.remove` | comma-separated values | _(empty)_ |

### 11. Password Validators Configuration

| Environment Variable              | TOML Key                          | Accepted Values        | Default   |
| --------------------------------- | --------------------------------- | ---------------------- | --------- |
| `AUTH_PASSWORD_VALIDATORS_EXTEND` | `auth.password-validators.extend` | comma-separated values | _(empty)_ |
| `AUTH_PASSWORD_VALIDATORS_REMOVE` | `auth.password-validators.remove` | comma-separated values | _(empty)_ |

---

> This file was generated by `tawala generate readme`. Re-run the command to refresh it.
