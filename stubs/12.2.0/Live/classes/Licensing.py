from types import ModuleType
from typing import Callable


class Licensing(ModuleType):

    @staticmethod
    def authorization_clock_days_ahead() -> int:
        """
        Advances the current date by the number of days specified by _AuthClockDaysAhead
        """
        ...

    @staticmethod
    def get_authorization_page_url(reauthorize: bool, is_trial: bool) -> str:
        """
        Retrieves the appopriate URL on ableton.com where the unser can initiate the authorization.
        """
        ...

    @staticmethod
    def get_services_url() -> str:
        """
        Returns the URL against which service calls (e.g. for authorization) can be performed.
        """
        ...

    @staticmethod
    def get_unlock_dir() -> tuple:
        """
        Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain.
        """
        ...

    @staticmethod
    def launch_web_browser(url: str) -> None:
        """
        Opens a web browser at the specified URL on the user's computer.
        """
        ...

    class ProgressDialog(object):
        def __init__(self, *a, **k):
            """
            A modal dialog showing a message and a progress animation.
            """
            ...

        def end_modal_loop(self) -> None:
            ...

        def run_in_modal_loop(self) -> None:
            ...

        def set_status_message(self, msg: str) -> None:
            ...

    class PythonLicensingBridge(object):
        def __init__(self, *a, **k):
            """
            Interface to the internal licensing services.
            """
            ...

        @property
        def base_product_id(self):
            """
            Returns Live's current base product ID.
            """
            ...

        @property
        def in_sassafras_mode(self):
            ...

        @property
        def license_must_match_variant(self):
            """
            Returns a bool indicating if we require the license information returned by the server to match the variant of Live.
            """
            ...

        @property
        def random_number_for_trial_authorization(self):
            """
            Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed).
            """
            ...

        @property
        def set_has_unsaved_changes(self):
            """
            Returns true if the set has unsaved changes.
            """
            ...

        def authorize_with_sassafras(self) -> None:
            ...

        def create_new_live_set(self) -> None:
            """
            Creates a new live set and discards unsaved changes.
            """
            ...

        def deauthenticate_user(self) -> None:
            """
            Deletes the current session ID.
            """
            ...

        def get_progress_dialog(self) -> ProgressDialog:
            """
            Retrieves an instance of ProgressDialog.
            """
            ...

        def get_session_id(self) -> str:
            """
            Retrieve stored session ID.
            """
            ...

        def get_startup_dialog(self, authorize_callable: object, authorize_later_callable: object) -> StartupDialog:
            """
            Retrieves an instance of the startup dialog with the passed callables connected to its buttons.
            """
            ...

        def get_trial_time_left(self) -> str:
            """
            Returns remaining time on a trial as a formatted string.
            """
            ...

        def load_and_convert_legacy_unlock_cfg(self) -> dict:
            """
            Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData object.
            """
            ...

        def process_license_response(self, license_response_lines: list) -> UnlockStatus:
            """
            Processes a list of strings, each representing a server response to a product authorization.
            """
            ...

        def process_trial_response(self, trial_response_line: str) -> bool:
            """
            Process the server's response to a Trial authorization.
            """
            ...

        def request_exit(self, exit_code: int=0) -> None:
            ...

        def save_current_set(self) -> None:
            """
            Saves the current Live session.
            """
            ...

        def set_network_timer(self, callback: object, interval_in_ms: int) -> None:
            """
            Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped.
            """
            ...

        def store_session_id(self, session_id: str) -> None:
            """
            Securely stores the user's session ID (aka cookie, aka credentials).
            """
            ...

    class StartupDialog(object):
        def __init__(self, *a, **k):
            """
            Serves as an entry point for the user to authorize Live on first launch
            """
            ...

        def end_modal_loop(self) -> None:
            ...

        def run_in_modal_loop(self) -> None:
            ...

        def set_notification_message(self, show_progress_bar: bool) -> None:
            ...

    class TrialContext:
        SAVE: int = 0
        FORCE_UPDATE: int = 2
        STARTUP: int = 3

    class UnlockStatus(object):
        def __init__(self, *a, **k):
            """
            Returns relevant information after unlock
            """
            ...

        @property
        def authorization_expired(self):
            ...

        @property
        def has_max_unlock_products(self):
            ...

        @property
        def temp_demo_mode(self):
            ...

        @property
        def time_limited(self):
            ...

        @property
        def unlock_error(self):
            ...

        @property
        def unlocked(self):
            ...
