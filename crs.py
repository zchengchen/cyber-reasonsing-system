import argparse
import json
import subprocess
import re
import os
from enum import Enum


cpv_commit = ["Commit 165","Commit 12", "Commit 153", "Commit 184", "Commit 45", "Commit 89", "Commit 35", "Commit 112", "Commit 123", "Commit 75", "Commit 172", "Commit 1", "Initial Commit", "Commit 102"]

class LLMOutState(Enum):
    INITAL_STATE = 0
    TRIGGER_SUCCESS = 1
    TRIGGER_FAILED = 2
    NEED_FUNC_INFO = 3
    NEED_HARNESS_CODE = 4

repo_owner = "aixcc-public"
repo_name = "challenge-004-nginx-source"

project_yaml_path = "nginx-cp/project.yaml"
pov_harness_impl_path = "nginx-cp/src/harnesses/pov_harness.cc"
mail_harness_impl_path = "nginx-cp/src/harnesses/mail_request_harness.cc"
smtp_harness_impl_path = "nginx-cp/src/harnesses/smtp_harness.cc"

