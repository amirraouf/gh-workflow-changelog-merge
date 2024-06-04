# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Types of changes
* **Added** for new features.
* **Changed** for changes in existing functionality.
* **Deprecated** for soon-to-be removed features.
* **Removed** for now removed features.
* **Fixed** for any bug fixes.
* **Security** in case of vulnerabilities.

### *Don't forget to update app/config/base.py with the latest application version number


## [0.95.4] - 2024-05-21
### Changed
- Updated requests to version 2.32.0
- Updated tqdm to version 4.66.3
- Updated pydantic to version 2.4.0
- Updated pydantic_core to version 2.10.0
- Updated gunicorn to version 22.0.0
- Updated dnspython to version 2.6.1
- Updated idna to version 3.7
- Updated pymysql to version 1.1.1

## [0.95.3] - 2024-05-24
### Fixed
- Fraud counts missing from the dashboard
- Query in SecuritiesClaim where it was joining all on master_claim_id = claim.id which doesn't work for legacy cases and creates incorrect joins
- Uncaught exception if user is not logged in on UserAccessObj
- Issue where SecuritiesClaim was triggering a check on exported at due to partial match on `Claim+`

## [0.95.2] - 2024-05-23
### Changed
- Permissions to Organizations to allow Leadership role to also be able to edit

## [0.95.1] - 2024-05-23
### Fixed
- Update form field bug impacting changing fields