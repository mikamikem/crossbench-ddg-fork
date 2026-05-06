# Copyright 2023 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

import logging
import os
import shutil
from typing import TYPE_CHECKING

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from typing_extensions import override

from crossbench.browsers.attributes import BrowserAttributes
from crossbench.browsers.ddg.base import DDGBaseMixin
from crossbench.browsers.chromium.webdriver import ChromiumBasedWebDriver, \
    ChromiumWebDriverAndroid, ChromiumWebDriverChromeOsSsh, \
    ChromiumWebDriverSsh, LocalChromiumWebDriverAndroid
from crossbench.browsers.chromium_based import helper
from crossbench.browsers.settings import Settings
from crossbench.browsers.webdriver import DriverException
from crossbench.flags.base import Flags
from crossbench.flags.chrome import ChromeFlags

if TYPE_CHECKING:
  from selenium.webdriver.chromium.options import ChromiumOptions
  from selenium.webdriver.chromium.service import ChromiumService
  from selenium.webdriver.chromium.webdriver import ChromiumDriver


class DDGWebDriver(DDGBaseMixin, ChromiumBasedWebDriver):

  WEB_DRIVER_OPTIONS = ChromeOptions
  WEB_DRIVER_SERVICE = ChromeService

  @classmethod
  @override
  def attributes(cls) -> BrowserAttributes:
    return (BrowserAttributes.DDG | BrowserAttributes.CHROMIUM_BASED
            | BrowserAttributes.WEBDRIVER)

  @override
  def _init_flags(self, settings: Settings) -> ChromeFlags:
    flags: Flags = super()._init_flags(settings)

    if os.path.exists('remoteConfigOverride.json'):
        self._flags.set("--force-remote-config-source",
                        os.path.join(os.getcwd(), 'remoteConfigOverride.json'))

    return self._flags

  @override
  def _create_driver(self, options: ChromiumOptions,
                     service: ChromiumService) -> ChromiumDriver:
    assert isinstance(options, ChromeOptions)
    assert isinstance(service, ChromeService)
    try:
        # try:
        #     import subprocess
        #
        #     subprocess.run("--terminate-on-running", executable=options.binary_location)
        # except Exception:
        #     pass

        # if os.path.exists('remoteConfigOverride.json'):
        #     shutil.copyfile('remoteConfigOverride.json',
        #                     os.path.join(os.path.dirname(options.binary_location),
        #                                  'forcedRemoteConfig.json'))

        return webdriver.Chrome(options=options, service=service)
    except selenium.common.exceptions.WebDriverException as e:
      msg: list[str] = [f"Could not start WebDriver: {e.msg}"]
      if self.is_locally_compiled():
        msg.append(helper.BUILD_CHROMEDRIVER_INSTRUCTIONS)
      msg_str = "\n".join(msg)
      logging.error(msg_str)
      raise DriverException(msg_str) from e

