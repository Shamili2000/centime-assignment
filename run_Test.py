# run_tests.py

# Import test modules
import pytest

# Run pytest with test discovery
if __name__ == "__main__":
    pytest.main(["-v", "tests/shipping.py"])
