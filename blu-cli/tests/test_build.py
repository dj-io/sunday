import subprocess
from unittest.mock import patch
from blu.commands.build  import build


@patch("blu.commands.build.run_command")
@patch("blu.commands.build.os.path.exists")
@patch("blu.commands.build.load_config")
@patch("blu.commands.build.cache_apollo_path")
@patch("blu.commands.build.Halo")
def test_build_retry(
    mock_halo, mock_cache_apollo_path, mock_load_config, mock_exists, mock_run_command
):
    """
    Test the `build` function when the user chooses to retry after a failure.
    """
    # Mock configuration and path setup
    mock_load_config.return_value = {"blu_path": "/tmp/blu"}
    mock_exists.side_effect = lambda path: True  # Mock requirements.txt existence

    # Simulate a failure and retry during the build process
    mock_run_command.side_effect = [
        None,
        None,
        subprocess.CalledProcessError(1, "python3 -m build"),
        None,
        None,
        None,
    ]

    # Call the build function with a retry
    with patch("builtins.input", side_effect=["yes", "no"]):
        build(skip_lint=True)

    # Assertions
    mock_load_config.assert_called_once()
    mock_cache_apollo_path.assert_called_once()
    mock_halo.return_value.start.assert_called_with(
        "Waiting for fixes... Please resolve the issues before retrying."
    )
