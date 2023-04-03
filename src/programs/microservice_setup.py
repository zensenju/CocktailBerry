from typing import Optional
import re

import typer

from src.filepath import LOCAL_MICROSERVICE_FILE, DEFAULT_MICROSERVICE_FILE

# defining pattern in file, where env is stored in 2nd grp
_HOOK_EP_REGEX = r"(HOOK_ENDPOINT=)(.+)"
_HOOK_HEADERS_REGEX = r"(HOOK_HEADERS=)(.+)"
_API_KEY_REGEX = r"(API_KEY=)(.+)"

_DEFAULT_HOOK_EP = "enpointforhook"
_DEFAULT_HOOK_HEADERS = "header1:value1,header2:value2"
_DEFAULT_API_KEY = "readdocshowtoget"

_SKIP_DIALOG = "Keep empty to skip (just press enter), enter 'd' to set back to default"


def setup_service(
    api_key: Optional[str] = None,
    hook_endpoint: Optional[str] = None,
    hook_header: Optional[str] = None,
):
    """Setup the microservice if any of args is given skip input,
    else prompt user for data.
    If user let prompt empty, keep current value.
    """
    # copies the default file if there is no local one
    if not LOCAL_MICROSERVICE_FILE.exists():
        LOCAL_MICROSERVICE_FILE.write_text(
            DEFAULT_MICROSERVICE_FILE.read_text(encoding="utf-8"),
            encoding="utf-8"
        )
    # Gets compose file content
    compose_setup = LOCAL_MICROSERVICE_FILE.read_text(encoding="utf-8")

    # Get the current variables, prompt user for variable if not provided
    if not all([api_key, hook_endpoint, hook_header]):
        typer.echo(typer.style(_SKIP_DIALOG, fg=typer.colors.GREEN, bold=True))
    if api_key is None:
        current_api_key = _get_env_var(_API_KEY_REGEX, compose_setup)
        api_key = _user_prompt(current_api_key, _DEFAULT_API_KEY, "API key")
    if hook_endpoint is None:
        current_hook_endpoint = _get_env_var(_HOOK_EP_REGEX, compose_setup)
        hook_endpoint = _user_prompt(current_hook_endpoint, _DEFAULT_HOOK_EP, "hook endpoint")
    if hook_header is None:
        current_hook_header = _get_env_var(_HOOK_HEADERS_REGEX, compose_setup)
        hook_header = _user_prompt(current_hook_header, _DEFAULT_HOOK_HEADERS, "hook header")

    # replace the values in the file
    compose_setup = _replace_env_var(_API_KEY_REGEX, compose_setup, api_key)
    compose_setup = _replace_env_var(_HOOK_EP_REGEX, compose_setup, hook_endpoint)
    compose_setup = _replace_env_var(_HOOK_HEADERS_REGEX, compose_setup, hook_header)

    # Write to the file the changes
    LOCAL_MICROSERVICE_FILE.write_text(compose_setup, encoding="utf-8")


def _get_env_var(regex: str, compose_setup: str):
    """The the according matched value from the file"""
    match = re.search(regex, compose_setup)
    key = "" if match is None else match[2]
    return key


def _replace_env_var(regex: str, compose_setup: str, value: str):
    """Replace the value in the file"""
    compose_setup = re.sub(regex, r"\1" + value, compose_setup)
    return compose_setup


def _user_prompt(current_value: str, default_value: str, display_name: str) -> str:
    """Prompt the user for the new value, returns new value"""
    current_part = f"the current value is: {current_value}"
    if current_value == default_value:
        current_part = "not set currently, it's the default"
    user_input = typer.prompt(
        f"Enter the {display_name}, {current_part}",
        default="",
        show_default=False,
    )
    if not user_input:
        user_input = current_value
    if user_input == "d":
        user_input = default_value
    return user_input
