# Changelog

## [0.3.9] - 2024-08-07
### Added
- scroll_and_find_element()

## [0.3.8] - 2024-08-06
### Added
- mimic_human()
- undetected-chromedriver as a dependency
- Support for python 3.12 (distutils)
- Better logging (capture events)

## [0.2.3] - 2024-08-06
### Added
- USER_AGENT_LIST (randomly select a User Agent if not passed explicitly)

## [0.2.2] - 2024-06-29
### Added
- headless=True to run headless

## [0.2.1] - 2024-06-19
### Added
- clean_error_str(): Returns error message without the Selenium Stacktrace

## [0.2.0] - 2024-04-03
### Added
- use_undetected=True uses undetected-chromedriver
- mobile_emulation=True opens in a mobile screen

## [0.1.0] - 2024-02-12
### Added
- Initial setup of repository (refactored from a private repo)
- Implemented `selenium_utils.py` with WebDriver helper functions
- Added `logging_utils.py` for logging support
- Created `tests/` directory with automated tests using `pytest`
- Added example scripts in `examples/` for web scraping and automation
- Configured GitHub Actions for automated testing

## [Unreleased]
- Upcoming features and improvements
