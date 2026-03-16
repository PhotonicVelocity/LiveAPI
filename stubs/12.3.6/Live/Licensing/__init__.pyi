from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable


class ProgressDialog:
    """A modal dialog showing a message and a progress animation."""

    def end_modal_loop(self) -> None:
        ...

    def run_in_modal_loop(self) -> None:
        ...

    def set_status_message(self, msg: str | None) -> None:
        ...

class PythonLicensingBridge:
    """Interface to the internal licensing services."""

    def authorize_with_sassafras(self) -> None:
        ...

    @property
    def base_product_id(self) -> int:
        """Returns Live's current base product ID."""
        ...

    def create_new_live_set(self) -> None:
        """Creates a new live set and discards unsaved changes."""
        ...

    def deauthenticate_user(self) -> None:
        """Deletes the current session ID."""
        ...

    def get_progress_dialog(self) -> ProgressDialog:
        """Retrieves an instance of ProgressDialog."""
        ...

    def get_session_id(self) -> str:
        """Retrieve stored session ID."""
        ...

    def get_startup_dialog(self, authorize_callable: Callable | None, authorize_later_callable: Callable | None) -> StartupDialog:
        """Retrieves an instance of the startup dialog with the passed callables connected to its buttons."""
        ...

    def get_trial_time_left(self) -> str:
        """Returns remaining time on a trial as a formatted string."""
        ...

    @property
    def in_sassafras_mode(self) -> bool:
        ...

    def invoke_pack_installation_callback(self) -> None:
        """Call package installation callback."""
        ...

    @property
    def license_must_match_variant(self) -> bool:
        """Returns a bool indicating if we require the license information returned by the server to match the variant of Live."""
        ...

    def load_and_convert_legacy_unlock_cfg(self) -> dict:
        """Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData object."""
        ...

    def process_license_response(self, license_response_lines: list[str] | None) -> UnlockStatus:
        """Processes a list of strings, each representing a server response to a product authorization."""
        ...

    def process_trial_response(self, trial_response_line: str | None) -> bool:
        """Process the server's response to a Trial authorization."""
        ...

    @property
    def random_number_for_trial_authorization(self) -> int:
        """Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed)."""
        ...

    def request_exit(self, exit_code: int = 0) -> None:
        ...

    def save_current_set(self) -> None:
        """Saves the current Live session."""
        ...

    @property
    def set_has_unsaved_changes(self) -> bool:
        """Returns true if the set has unsaved changes."""
        ...

    def set_network_timer(self, callback: Callable | None, interval_in_ms: int | None) -> None:
        """Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped."""
        ...

    def store_session_id(self, session_id: str | None) -> None:
        """Securely stores the user's session ID (aka cookie, aka credentials)."""
        ...

class StartupDialog:
    """Serves as an entry point for the user to authorize Live on first launch."""

    def end_modal_loop(self) -> None:
        ...

    def run_in_modal_loop(self, show_only_offline_auth_instructions: bool | None) -> None:
        ...

    def set_notification_message(self, notification_text: str | None, show_progress_bar: bool | None) -> None:
        ...

class TrialContext:
    SAVE: int = 0
    FORCE_UPDATE: int = 2
    STARTUP: int = 3

class UnlockStatus:
    """Returns relevant information after unlock"""

    def __init__(self) -> None: ...

    @property
    def authorization_deactivated(self) -> bool:
        ...

    @property
    def authorization_expired(self) -> bool:
        ...

    @property
    def has_max_unlock_products(self) -> bool:
        ...

    @property
    def temp_demo_mode(self) -> bool:
        ...

    @property
    def time_limited(self) -> bool:
        ...

    @property
    def unlock_error(self) -> bool:
        ...

    @property
    def unlocked(self) -> bool:
        ...

def authorization_clock_days_ahead() -> int:
    """Advances the current date by the number of days specified by _AuthClockDaysAhead"""
    ...

def get_authorization_page_url(reauthorize: bool | None, is_trial: bool | None) -> str:
    """Retrieves the appopriate URL on ableton.com where the unser can initiate the authorization."""
    ...

def get_purchase_live_url() -> str:
    """Returns the environment-aware purchase URL for purchasing Live licenses"""
    ...

def get_services_url() -> str:
    """Returns the URL against which service calls (e.g. for authorization) can be performed."""
    ...

def get_unlock_dir() -> tuple[str, bool]:
    """Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain."""
    ...

def launch_web_browser(url: str | None) -> None:
    """Opens a web browser at the specified URL on the user's computer."""
    ...

__all__ = ['ProgressDialog', 'PythonLicensingBridge', 'StartupDialog', 'TrialContext', 'UnlockStatus', 'authorization_clock_days_ahead', 'get_authorization_page_url', 'get_purchase_live_url', 'get_services_url', 'get_unlock_dir', 'launch_web_browser']
